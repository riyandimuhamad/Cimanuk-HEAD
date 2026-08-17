import pandas as pd

file_path = r"f:\KAMPUS\KP & Skripsi\KP\Project-KP-CimanukHEAD\Dataset\raw_data\sensor_rekap_20200101_20260813_part_2.csv"

print("Membaca sample data...")
df_sample = pd.read_csv(file_path, nrows=1000)

print("\n=== DAFTAR KOLOM ===")
print(df_sample.columns.tolist())

print("\n=== TIPE HIDROLOGI YANG TERSEDIA ===")
if 'hidrologi_type' in df_sample.columns:
    print(df_sample['hidrologi_type'].unique())
else:
    print("Kolom 'hidrologi_type' tidak ditemukan.")

print("\n=== TIPE SENSOR YANG TERSEDIA ===")
if 'sensor_type' in df_sample.columns:
    print(df_sample['sensor_type'].unique())
else:
    print("Kolom 'sensor_type' tidak ditemukan.")

print("\n=== PREVIEW 5 BARIS PERTAMA ===")
cols_to_show = [col for col in ['nama pos/perangkat', 'hidrologi_type', 'sensor_name', 'value', 'last_sending_data'] if col in df_sample.columns]
print(df_sample[cols_to_show].head())
