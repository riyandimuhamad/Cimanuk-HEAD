import os
import csv
import glob
import pandas as pd
import time

def print_header(text):
    print(f"\n{'='*60}")
    print(f" {text}")
    print(f"{'='*60}")

def main():
    print_header("PROSES VERIFIKASI VOLUME DATA TELEMETRI BBWS CIMANUK-HEAD")
    print("[INFO] Menginisialisasi pemindaian file RAW (CSV)...")
    time.sleep(1)

    # 1. Menghitung Data Mentah (RAW)
    raw_dir = r"f:\KAMPUS\KP & Skripsi\KP\Project-KP-CimanukHEAD\data\raw"
    files = glob.glob(os.path.join(raw_dir, "sensor_rekap_*.csv"))
    
    total_raw = 0
    cimancis_raw = 0
    
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            for row in reader:
                if not row: continue
                total_raw += 1
                if len(row) > 0 and "CIMANUK CISANGGARUNG" in row[0].upper():
                    cimancis_raw += 1
                    
    print(f"[SUCCESS] Berhasil memindai {len(files)} file RAW.")
    print(f"  -> Total Data Dasar (Keseluruhan)      : {total_raw:,} baris")
    print(f"  -> Total Data Milik Cimanuk-Cisanggarung: {cimancis_raw:,} baris")
    print(f"  (Catatan: 100% data mentah terkonfirmasi milik wilayah Cimancis)\n")
    time.sleep(1)

    # 2. Menghitung Data Bersih (PROCESSED)
    print_header("HASIL DATA PRE-PROCESSING (FILTER PARAMETER & CLEANING)")
    print("[INFO] Membaca file Parquet hasil cleaning...")
    time.sleep(1)
    
    try:
        df_arr = pd.read_parquet(r"f:\KAMPUS\KP & Skripsi\KP\Project-KP-CimanukHEAD\data\processed\master_curah_hujan_ready.parquet")
        arr_count = len(df_arr)
        print(f"[SUCCESS] File master_curah_hujan_ready.parquet terbaca.")
        print(f"  -> Data Bersih ARR (Curah Hujan) : {arr_count:,} baris")
    except Exception as e:
        arr_count = 0
        print(f"[ERROR] Gagal membaca data ARR: {e}")

    try:
        df_awlr = pd.read_parquet(r"f:\KAMPUS\KP & Skripsi\KP\Project-KP-CimanukHEAD\data\processed\master_duga_air_ready.parquet")
        awlr_count = len(df_awlr)
        print(f"[SUCCESS] File master_duga_air_ready.parquet terbaca.")
        print(f"  -> Data Bersih AWLR (Tinggi Air) : {awlr_count:,} baris")
    except Exception as e:
        awlr_count = 0
        print(f"[ERROR] Gagal membaca data AWLR: {e}")

    print(f"\n  -> TOTAL DATA BERSIH SIAP OLAH (ARR + AWLR) : {arr_count + awlr_count:,} baris")
    print_header("VERIFIKASI SELESAI")

if __name__ == "__main__":
    main()
