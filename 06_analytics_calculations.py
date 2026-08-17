import pandas as pd
import numpy as np
import os

def calculate_analytics():
    print("Mulai proses kalkulasi analitik (Lag Time & KRS)...")
    base_dir = r"f:\KAMPUS\KP & Skripsi\KP\Project-KP-CimanukHEAD"
    ch_path = os.path.join(base_dir, "master_curah_hujan_ready.csv")
    da_path = os.path.join(base_dir, "master_duga_air_ready.csv")
    out_path = os.path.join(base_dir, "analytics_results.csv")

    # 1. Baca Data
    df_ch = pd.read_csv(ch_path)
    df_da = pd.read_csv(da_path)

    df_ch['DateTime'] = pd.to_datetime(df_ch['DateTime'])
    df_da['DateTime'] = pd.to_datetime(df_da['DateTime'])

    # Filter data VALID
    df_ch_valid = df_ch[df_ch['data_status'] == 'VALID']
    df_da_valid = df_da[df_da['data_status'] == 'VALID']

    # ==========================================
    # SUB-TASK 4.1: KALKULASI LAG TIME
    # ==========================================
    print("Menghitung Lag Time (JATIGEDE -> CIMANUK-RENTANG)...")
    hulu_ch = df_ch_valid[df_ch_valid['Nama_Stasiun'].str.contains('JATIGEDE', case=False, na=False)][['DateTime', 'Curah Hujan (mm)']]
    hilir_da = df_da_valid[df_da_valid['Nama_Stasiun'].str.contains('RENTANG', case=False, na=False)][['DateTime', 'Ketinggian Air (m)']]

    # Gabungkan berdasarkan waktu
    df_lag = pd.merge(hulu_ch, hilir_da, on='DateTime', how='inner').sort_values('DateTime')

    best_lag = 0
    best_corr = -1
    
    # Geser (shift) data CH untuk mensimulasikan waktu perjalanan air
    for lag in range(1, 25):
        # Shift duga air ke belakang (artinya mencocokkan hujan masa lalu dengan tinggi air saat ini)
        shifted_da = df_lag['Ketinggian Air (m)'].shift(-lag)
        corr = df_lag['Curah Hujan (mm)'].corr(shifted_da)
        if pd.notna(corr) and corr > best_corr:
            best_corr = corr
            best_lag = lag

    print(f"✅ Lag Time Terbaik: {best_lag} Jam (Korelasi Pearson: {best_corr:.4f})")

    # ==========================================
    # SUB-TASK 4.2: KALKULASI KRS
    # ==========================================
    print("Menghitung KRS Bulanan untuk CIMANUK-RENTANG...")
    hilir_da_full = df_da_valid[df_da_valid['Nama_Stasiun'].str.contains('RENTANG', case=False, na=False)].copy()
    hilir_da_full['YearMonth'] = hilir_da_full['DateTime'].dt.to_period('M')

    krs_results = []
    
    # Group per bulan
    grouped = hilir_da_full.groupby('YearMonth')
    for name, group in grouped:
        max_level = group['Ketinggian Air (m)'].max()
        min_level = group['Ketinggian Air (m)'].min()
        
        # Hindari pembagian dengan nol
        if pd.isna(max_level) or pd.isna(min_level) or min_level <= 0:
            continue
            
        krs = max_level / min_level
        
        # Klasifikasi status
        if krs <= 50:
            status = "Sangat Baik/Normal"
        elif 50 < krs <= 80:
            status = "Sedang/Mulai Kritis"
        else:
            status = "Sangat Kritis"
            
        krs_results.append({
            'Periode': str(name),
            'Stasiun': 'CIMANUK-RENTANG',
            'Max_Level (m)': max_level,
            'Min_Level (m)': min_level,
            'KRS': round(krs, 2),
            'Status': status,
            'Lag_Time_Jam': best_lag
        })

    # Simpan Hasil
    df_results = pd.DataFrame(krs_results)
    if not df_results.empty:
        df_results.to_csv(out_path, index=False)
        print(f"✅ Hasil analitik berhasil disimpan ke: {out_path}")
    else:
        print("Peringatan: Tidak ada data KRS yang dapat dihitung.")

if __name__ == "__main__":
    calculate_analytics()
