import pandas as pd
import os

base_dir = r"f:\KAMPUS\KP & Skripsi\KP\Project-KP-CimanukHEAD"
air_parquet = os.path.join(base_dir, "data", "processed", "master_duga_air_ready.parquet")
output_parquet = os.path.join(base_dir, "data", "processed", "analytics_results.parquet")

print(" Membaca data Muka Air dari Parquet...")
try:
    df_air = pd.read_parquet(air_parquet)
    
    # Ekstrak Tahun-Bulan untuk agregasi
    df_air['Periode'] = df_air['DateTime'].dt.to_period('M')
    
    print(" Menghitung Koefisien Rezim Sungai (KRS) per bulan...")
    krs_data = []
    
    # Kelompokkan data berdasarkan Stasiun dan Bulan
    for (stasiun, periode), group in df_air.groupby(['Nama_Stasiun', 'Periode']):
        max_val = group['clean_value'].max()
        min_val = group['clean_value'].min()
        
        if min_val > 0:  # Mencegah pembagian dengan Nol (ZeroDivisionError)
            krs = max_val / min_val
            
            # Klasifikasi Standar Kehutanan/Hidrologi
            if krs <= 50:
                status = 'Sangat Baik/Normal'
            elif 50 < krs <= 80:
                status = 'Sedang/Mulai Kritis'
            elif 80 < krs <= 120:
                status = 'Buruk'
            else:
                status = 'Sangat Buruk/Kritis'
                
            krs_data.append({
                'Stasiun': stasiun,
                'Periode': str(periode), # Format menjadi string agar mudah dibaca Streamlit
                'Max_Level': round(max_val, 2),
                'Min_Level': round(min_val, 2),
                'KRS': round(krs, 2),
                'Status': status
            })
    
    df_krs = pd.DataFrame(krs_data)
    
    # Urutkan berdasarkan Waktu
    df_krs = df_krs.sort_values(by=['Stasiun', 'Periode'])
    
    # Simpan hasil akhir (Overwrite file analytics yang lama)
    df_krs.to_parquet(output_parquet, index=False)
    
    print(f" Selesai! Data analisis KRS untuk {len(df_krs)} bulan berhasil dihitung.")
    print(f" Tersimpan di: {output_parquet}")
    print(" SILAKAN REFRESH DASHBOARD STREAMLIT ANDA!")

except Exception as e:
    print(f" Terjadi kesalahan: {e}")
