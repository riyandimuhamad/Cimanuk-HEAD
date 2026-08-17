import pandas as pd
import os
import glob
import pyarrow as pa
import pyarrow.parquet as pq

# Lokasi file raksasa BBWS
base_dir = r"f:\KAMPUS\KP & Skripsi\KP\Project-KP-CimanukHEAD"
raw_dir = os.path.join(base_dir, "data", "raw")
hujan_parquet = os.path.join(base_dir, "data", "processed", "master_curah_hujan_ready.parquet")
air_parquet = os.path.join(base_dir, "data", "processed", "master_duga_air_ready.parquet")

# Hapus file lama jika ada agar tidak menumpuk
for p in [hujan_parquet, air_parquet]:
    if os.path.exists(p): os.remove(p)

# Cari semua file CSV part 1 sampai 8
all_files = sorted(glob.glob(os.path.join(raw_dir, "sensor_rekap_*_part_*.csv")))

# Inisialisasi penulis Parquet
writer_hujan = None
writer_air = None

print(" MEMULAI PROSES ETL BIG DATA BBWS (CHUNKING METHOD)...")

total_hujan = 0
total_air = 0

for file_idx, file in enumerate(all_files, 1):
    print(f"\n Sedang memproses file {file_idx}/{len(all_files)}: {os.path.basename(file)}")
    
    # Baca file suap demi suap (100.000 baris per suapan agar RAM aman)
    chunk_iterator = pd.read_csv(file, chunksize=100000, low_memory=False)
    
    for chunk_num, chunk in enumerate(chunk_iterator, 1):
        # 1. Standardisasi Nama Kolom
        chunk = chunk.rename(columns={
            'nama pos/perangkat': 'Nama_Stasiun',
            'latitude': 'Latitude',
            'longitude': 'Longitude',
            'last_sending_data': 'DateTime',
            'value': 'clean_value',
            'das name': 'DAS'
        })
        
        # 2. Filter hanya DAS Cimanuk
        if 'DAS' in chunk.columns:
            chunk = chunk[chunk['DAS'].astype(str).str.contains('CIMANUK', case=False, na=False)]
        
        # 3. Format Waktu
        chunk['DateTime'] = pd.to_datetime(chunk['DateTime'], errors='coerce')
        chunk = chunk.dropna(subset=['DateTime', 'clean_value'])
        
        # 4. Filter Data Hujan & Pembersihan Outlier
        if 'hidrologi_type' in chunk.columns:
            df_hujan = chunk[chunk['hidrologi_type'].astype(str).str.contains('HUJAN', case=False)].copy()
            df_hujan = df_hujan[(df_hujan['clean_value'] >= 0) & (df_hujan['clean_value'] < 200)]
        else:
            df_hujan = pd.DataFrame()
            
        # 5. Filter Data Air & Pembersihan Outlier
        if 'hidrologi_type' in chunk.columns:
            df_air = chunk[chunk['hidrologi_type'].astype(str).str.contains('DUGA AIR|TMA', case=False)].copy()
            df_air = df_air[(df_air['clean_value'] >= 0) & (df_air['clean_value'] < 30)]
        else:
            df_air = pd.DataFrame()
            
        # 6. Simpan langsung ke Parquet (Streaming)
        if not df_hujan.empty:
            table_h = pa.Table.from_pandas(df_hujan[['Nama_Stasiun', 'DAS', 'Latitude', 'Longitude', 'DateTime', 'clean_value']])
            if writer_hujan is None:
                writer_hujan = pq.ParquetWriter(hujan_parquet, table_h.schema, compression='snappy')
            writer_hujan.write_table(table_h)
            total_hujan += len(df_hujan)
            
        if not df_air.empty:
            table_a = pa.Table.from_pandas(df_air[['Nama_Stasiun', 'DAS', 'Latitude', 'Longitude', 'DateTime', 'clean_value']])
            if writer_air is None:
                writer_air = pq.ParquetWriter(air_parquet, table_a.schema, compression='snappy')
            writer_air.write_table(table_a)
            total_air += len(df_air)
            
        print(f"   -> Selesai memakan Chunk {chunk_num} (Hujan: {len(df_hujan)} baris, Air: {len(df_air)} baris)")

# Tutup penulis
if writer_hujan: writer_hujan.close()
if writer_air: writer_air.close()

print("\n PROSES SELESAI!")
print(f" Total Data Hujan Tersimpan : {total_hujan:,} baris")
print(f" Total Data Muka Air Tersimpan: {total_air:,} baris")
print(" Dasbor Cimanuk-HEAD siap dijalankan dengan Data Asli!")
