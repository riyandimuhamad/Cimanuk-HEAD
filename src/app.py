import streamlit as st
import pandas as pd
import plotly.express as px
import os
import folium
from streamlit_folium import st_folium
import geopandas as gpd

# Konfigurasi Halaman (Harus diletakkan paling atas)
st.set_page_config(
    page_title="Cimanuk-HEAD | Hydrological DSS",
    layout="wide",
    initial_sidebar_state="expanded"
)
# Menyembunyikan elemen bawaan Streamlit (Header, Footer, Hamburger Menu)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Judul Aplikasi
st.title("Cimanuk-HEAD")
st.subheader("Hydrological Early Warning & Analytics Dashboard")
st.markdown("Sistem Pendukung Keputusan Pemantauan Hidrologi & Mitigasi Bencana BBWS Cimanuk Cisanggarung")
st.markdown("---")

# Fungsi untuk load data (Menggunakan cache agar ngebut)
@st.cache_data
def load_data():
    try:
        df_hujan = pd.read_parquet("data/processed/master_curah_hujan_ready.parquet")
        df_air = pd.read_parquet("data/processed/master_duga_air_ready.parquet")
        df_analytics = pd.read_parquet("data/processed/analytics_results.parquet")
        
        # Filter ketat HANYA untuk DAS Cimanuk (Sesuai Batasan Proyek)
        if 'DAS' in df_hujan.columns:
            df_hujan = df_hujan[df_hujan['DAS'].str.contains('Cimanuk', case=False, na=False)]
        if 'DAS' in df_air.columns:
            df_air = df_air[df_air['DAS'].str.contains('Cimanuk', case=False, na=False)]
        if 'Stasiun' in df_analytics.columns:
            df_analytics = df_analytics[df_analytics['Stasiun'].str.contains('CIMANUK', case=False, na=False)]
            
        return df_hujan, df_air, df_analytics
    except Exception as e:
        st.error(f"Gagal memuat data Parquet: {e}")
        return None, None, None

df_hujan, df_air, df_analytics = load_data()

# Struktur Sidebar (Menu Samping)
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Logo_PU_%28Kementerian_Pekerjaan_Umum_dan_Perumahan_Rakyat%29.png/220px-Logo_PU_%28Kementerian_Pekerjaan_Umum_dan_Perumahan_Rakyat%29.png", width=80)
st.sidebar.title("Navigasi Sistem")
menu = st.sidebar.radio("Pilih Modul Analitik:", [
    "Dashboard Overview", 
    "Lag Time Tracker", 
    "Basin Health & KRS", 
    "Peta Infrastruktur Terpadu"
])

# ==========================================
# HALAMAN 1: OVERVIEW
# ==========================================
if menu == "Dashboard Overview":
    st.header("Ringkasan Eksekutif Wilayah Sungai")
    if df_hujan is not None and df_air is not None:
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total Data Curah Hujan", f"{len(df_hujan):,} baris")
        col2.metric("Total Data Duga Air", f"{len(df_air):,} baris")
        col3.metric("Total Stasiun Hujan", df_hujan['Nama_Stasiun'].nunique())
        col4.metric("Total Stasiun Air", df_air['Nama_Stasiun'].nunique())
        
        st.markdown("---")
        st.subheader("Profil Distribusi Data Historis Sensor")
        st.markdown("Menjawab rumusan masalah ke-1 pada *Project Plan*: **Memprofilkan kualitas dan keandalan transmisi pengiriman data historis** dari seluruh perangkat *Internet of Things* (IoT) BBWS di DAS Cimanuk.")
        
        # Agregasi jumlah data per tahun
        df_h_count = df_hujan['DateTime'].dt.year.value_counts().reset_index()
        df_h_count.columns = ['Tahun', 'Volume Data Hujan']
        df_a_count = df_air['DateTime'].dt.year.value_counts().reset_index()
        df_a_count.columns = ['Tahun', 'Volume Data Air']
        
        # Menggabungkan data Hujan dan Air
        df_trend = pd.merge(df_h_count, df_a_count, on='Tahun', how='outer').fillna(0).sort_values('Tahun')
        df_trend['Tahun'] = df_trend['Tahun'].astype(int).astype(str) # Ubah ke string agar axis X tidak pakai koma (2,020)
        
        # Visualisasi menggunakan Plotly
        import plotly.graph_objects as go
        fig_trend = go.Figure()
        fig_trend.add_trace(go.Bar(x=df_trend['Tahun'], y=df_trend['Volume Data Hujan'], name='Sensor Curah Hujan', marker_color='#3498db'))
        fig_trend.add_trace(go.Bar(x=df_trend['Tahun'], y=df_trend['Volume Data Air'], name='Sensor Muka Air', marker_color='#e74c3c'))
        
        fig_trend.update_layout(
            barmode='group',
            xaxis_title="Tahun Perekaman",
            yaxis_title="Total Baris Data Terkirim",
            height=400,
            hovermode="x unified",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig_trend, use_container_width=True)
        
        st.info("Pilih modul navigasi pada panel kiri untuk masuk ke menu analisis spesifik atau pemetaan spasial.")

# ==========================================
# HALAMAN 2: LAG TIME TRACKER
# ==========================================
elif menu == "Lag Time Tracker":
    st.header("Pemantauan Waktu Rambat Air")
    st.markdown("Modul peringatan dini untuk menganalisis jeda waktu perjalanan air dari stasiun hulu pengukur curah hujan menuju stasiun hilir pengukur muka air.")
    
    if df_hujan is not None and df_air is not None:
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Stasiun Hulu")
            stasiun_hujan = st.selectbox("Pilih Pos Pengamatan Curah Hujan:", sorted(df_hujan['Nama_Stasiun'].dropna().unique()), index=None, placeholder="Pilih Stasiun Hulu...")
        with col2:
            st.subheader("Stasiun Hilir")
            stasiun_air = st.selectbox("Pilih Pos Pemantauan Muka Air:", sorted(df_air['Nama_Stasiun'].dropna().unique()), index=None, placeholder="Pilih Stasiun Hilir...")
            
        st.markdown("---")
        
        # Hentikan eksekusi di bawah jika belum memilih stasiun
        if not stasiun_hujan or not stasiun_air:
            st.info("Peta dan Grafik akan muncul otomatis setelah Anda memilih Stasiun Hulu dan Stasiun Hilir di atas.")
            st.stop()
            
        # Filter Data
        df_h_filtered = df_hujan[df_hujan['Nama_Stasiun'] == stasiun_hujan]
        df_a_filtered = df_air[df_air['Nama_Stasiun'] == stasiun_air]
        
        if not df_h_filtered.empty and not df_a_filtered.empty:
            # Validasi Arah Aliran Air (Topologi Geografis)
            lat_hujan = df_h_filtered['Latitude'].iloc[0]
            lat_air = df_a_filtered['Latitude'].iloc[0]
            
            # DAS Cimanuk mengalir dari Selatan (Gunung Papandayan, Garut ~ Latitude -7.3) 
            # menuju Utara (Laut Jawa, Indramayu ~ Latitude -6.2).
            # Jika Latitude stasiun hujan lebih besar (lebih mendekati nol/Utara), berarti posisinya salah (di bawah stasiun muka air).
            if lat_hujan > lat_air + 0.05: # Beri toleransi margin 0.05 derajat
                st.error(f"Pelanggaran Topografi Hidrologi: Stasiun Curah Hujan ({stasiun_hujan}) berada lebih ke Utara (Hilir) dibandingkan Stasiun Muka Air ({stasiun_air}). Secara hukum fisika, aliran air tidak mungkin bergerak dari Hilir ke Hulu.")
                st.info("Sistem menghentikan proses *rendering* grafik. Silakan pilih kombinasi stasiun Hulu-Hilir yang logis secara geografis.")
                st.stop() # Memblokir proses render grafik ke bawah
                
            # Cari rentang waktu gabungan
            min_date = max(df_h_filtered['DateTime'].min(), df_a_filtered['DateTime'].min())
            max_date = min(df_h_filtered['DateTime'].max(), df_a_filtered['DateTime'].max())
            
            st.write(f"**Rentang Waktu Tersedia:** `{min_date.strftime('%d %b %Y')}` s/d `{max_date.strftime('%d %b %Y')}`")
            
            # Input Tanggal
            date_range = st.date_input(
                "Pilih Rentang Waktu Analisis disarankan maksimum satu bulan",
                value=(min_date, min_date + pd.Timedelta(days=14)),
                min_value=min_date,
                max_value=max_date
            )
            
            if len(date_range) == 2:
                import plotly.graph_objects as go
                from plotly.subplots import make_subplots
                
                start_date, end_date = date_range
                mask_h = (df_h_filtered['DateTime'] >= pd.to_datetime(start_date)) & (df_h_filtered['DateTime'] <= pd.to_datetime(end_date) + pd.Timedelta(days=1))
                mask_a = (df_a_filtered['DateTime'] >= pd.to_datetime(start_date)) & (df_a_filtered['DateTime'] <= pd.to_datetime(end_date) + pd.Timedelta(days=1))
                
                plot_h = df_h_filtered[mask_h].sort_values('DateTime')
                plot_a = df_a_filtered[mask_a]
                # Filter error sensor (angka 0) dan urutkan waktu agar garis grafik tidak zig-zag
                plot_a = plot_a[plot_a['clean_value'] > 0].sort_values('DateTime')
                
                if not plot_h.empty and not plot_a.empty:
                    st.markdown("### 1. Visualisasi Jalur Geografis Sungai")
                    
                    # Membuat Peta dengan Folium agar bisa memuat KML Jaringan Sungai
                    lon_hujan = df_h_filtered['Longitude'].iloc[0]
                    lon_air = df_a_filtered['Longitude'].iloc[0]
                    
                    pilihan_peta = st.radio("Pilih Tampilan Peta Lapisan Bawah:", ["Peta Terang (Default)", "Mode Gelap", "Citra Satelit"], horizontal=True, key="peta_lag")
                    
                    with st.spinner("Merender KML Jaringan Sungai..."):
                        # Pusat peta berada di tengah-tengah antara Hulu dan Hilir
                        if pilihan_peta == "Citra Satelit":
                            m_lag = folium.Map(location=[(lat_hujan + lat_air)/2, (lon_hujan + lon_air)/2], zoom_start=9, tiles="https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}", attr="Google")
                        elif pilihan_peta == "Mode Gelap":
                            m_lag = folium.Map(location=[(lat_hujan + lat_air)/2, (lon_hujan + lon_air)/2], zoom_start=9, tiles="CartoDB dark_matter")
                        else:
                            m_lag = folium.Map(location=[(lat_hujan + lat_air)/2, (lon_hujan + lon_air)/2], zoom_start=9, tiles="CartoDB positron")
                        
                        # Muat Jaringan Sungai
                        kml_sungai = "assets/kml/Peta Jaringan Sungai.kml"
                        if os.path.exists(kml_sungai):
                            try:
                                gdf_sungai = gpd.read_file(kml_sungai, engine='pyogrio')
                                gdf_sungai = gdf_sungai.dropna(subset=['geometry'])
                                gdf_sungai = gdf_sungai.explode(index_parts=False)
                                
                                # Trik Geospasial Cerdas: Memotong (Clipping) aliran sungai 
                                # agar HANYA menampilkan urat air yang berada di antara titik Hulu dan Hilir
                                margin = 0.05
                                min_lon = min(lon_hujan, lon_air) - margin
                                max_lon = max(lon_hujan, lon_air) + margin
                                min_lat = min(lat_hujan, lat_air) - margin
                                max_lat = max(lat_hujan, lat_air) + margin
                                
                                # Crop data menggunakan Bounding Box
                                gdf_sungai_cropped = gdf_sungai.cx[min_lon:max_lon, min_lat:max_lat]
                                
                                # Fungsi styling untuk membedakan Sungai Utama dan Anak Sungai
                                def style_sungai(feature):
                                    name = feature['properties'].get('Name', '')
                                    if name and 'cimanuk' in name.lower():
                                        # Sungai Utama (Cimanuk): Warna Biru Tua Terang, Sangat Tebal
                                        return {'color': '#00008B', 'weight': 6, 'opacity': 1.0}
                                    else:
                                        # Anak Sungai: Warna Biru Muda/Cyan, Tipis
                                        return {'color': '#00BFFF', 'weight': 2, 'opacity': 0.6}
                                
                                folium.GeoJson(
                                    gdf_sungai_cropped,
                                    name="Aliran Sungai (Hulu-Hilir)",
                                    style_function=style_sungai,
                                    smooth_factor=0  # Memaksa render titik asli (mencegah garis nabrak rumah warga)
                                ).add_to(m_lag)
                            except:
                                pass
                                
                        # Titik Hulu (Hujan)
                        folium.Marker(
                            location=[lat_hujan, lon_hujan],
                            popup=f"Pos Hulu Hujan: {stasiun_hujan}",
                            icon=folium.Icon(color='blue', icon='info-sign')
                        ).add_to(m_lag)
                        
                        # Titik Hilir (Banjir)
                        folium.Marker(
                            location=[lat_air, lon_air],
                            popup=f"Pos Hilir Muka Air: {stasiun_air}",
                            icon=folium.Icon(color='red', icon='info-sign')
                        ).add_to(m_lag)
                        
                        st_folium(m_lag, width=900, height=400, returned_objects=[])
                    
                    st.markdown("### 2. Analisis Korelasi Deret Waktu")
                    # Membuat grafik 2 Sumbu Y
                    fig = make_subplots(specs=[[{"secondary_y": True}]])
                    
                    # Tambah Curah Hujan (Bar Chart)
                    fig.add_trace(
                        go.Bar(
                            x=plot_h['DateTime'], 
                            y=plot_h['clean_value'], 
                            name=f"Curah Hujan di {stasiun_hujan}", 
                            marker_color="rgba(52, 152, 219, 0.7)",
                            width=1000 * 3600 * 1  # Ubah ke 1 Jam agar akurat saat di-zoom
                        ),
                        secondary_y=False,
                    )
                    
                    # Tambah Muka Air (Line Chart)
                    fig.add_trace(
                        go.Scatter(x=plot_a['DateTime'], y=plot_a['clean_value'], name=f"Muka Air di {stasiun_air}", line=dict(color='red', width=3)),
                        secondary_y=True,
                    )
                    
                    fig.update_layout(
                        title_text=f"Korelasi Silang antara Curah Hujan di {stasiun_hujan} dan Muka Air di {stasiun_air}",
                        height=550, hovermode="x unified"
                    )
                    
                    # Konfigurasi Sumbu X dan Y
                    fig.update_xaxes(
                        title_text="Tanggal & Jam", 
                        tickformat="%d %b\n%H:%M",  # Memaksa tampilan Jam (HH:MM) di bawah tanggal
                        hoverformat="%d %b %Y, %H:%M" # Format saat mouse diarahkan
                    )
                    fig.update_yaxes(title_text="Intensitas Curah Hujan dalam milimeter", secondary_y=False, autorange="reversed")
                    fig.update_yaxes(title_text="Tinggi Muka Air dalam meter", secondary_y=True)
                    
                    st.plotly_chart(fig, use_container_width=True)
                    
                    # --- INTEGRASI KRS KE LAG TIME ---
                    st.markdown("### 3. Diagnosis Ekologis Kesehatan Daerah Aliran Sungai")
                    
                    # Menghitung KRS on-the-fly berdasarkan data yang sedang tampil di grafik
                    if not plot_a.empty and plot_a['clean_value'].min() > 0:
                        max_level = plot_a['clean_value'].max()
                        min_level = plot_a['clean_value'].min()
                        krs_value = max_level / min_level
                        
                        if krs_value <= 50:
                            status_krs = "Sangat Baik atau Normal dengan Hutan Hulu Aman"
                            warna = "success"
                            pesan = "Air meresap dengan baik. Pohon-pohon di hulu mampu menahan air hujan, sehingga aliran ke hilir stabil dan risiko banjir terkendali."
                        elif 50 < krs_value <= 80:
                            status_krs = "Mulai Kritis dan Perlu Waspada"
                            warna = "warning"
                            pesan = "Fluktuasi air mulai meninggi. Daya serap kawasan hutan di hulu terindikasi mulai mengalami penurunan."
                        else:
                            status_krs = "Kritis dengan Indikasi Deforestasi Ekstrem"
                            warna = "error"
                            pesan = "Perbedaan muka air sangat ekstrem! Ini adalah bukti hidrologis bahwa kawasan resapan di hulu sudah rusak. Air hujan gagal diserap tanah dan langsung meluncur menjadi banjir."
                            
                        col_k1, col_k2, col_k3 = st.columns(3)
                        col_k1.metric("Muka Air Tertinggi", f"{max_level:.2f} meter")
                        col_k2.metric("Muka Air Terendah", f"{min_level:.2f} meter")
                        col_k3.metric("Skor KRS (Periode Ini)", f"{krs_value:.1f}")
                        
                        if warna == "success":
                            st.success(f"**Status DAS:** {status_krs}  \n**Analisis:** {pesan}")
                        elif warna == "warning":
                            st.warning(f"**Status DAS:** {status_krs}  \n**Analisis:** {pesan}")
                        else:
                            st.error(f"**Status DAS:** {status_krs}  \n**Analisis:** {pesan}")
                    else:
                        st.info("Tinggi muka air terendah menyentuh angka 0, sehingga rasio fluktuasi (KRS) tidak dapat dihitung secara matematis pada periode ini.")
                        
                    st.markdown("---")
                else:
                    st.warning("Data kosong pada rentang tanggal yang dipilih.")

# ==========================================
# HALAMAN 3: BASIN HEALTH & KRS
# ==========================================
elif menu == "Basin Health & KRS":
    st.header("Kesehatan Daerah Aliran Sungai dan Koefisien Rezim Sungai")
    st.markdown("Modul untuk mendeteksi tingkat kritis kesehatan hidrologis berdasarkan fluktuasi muka air bulanan.")
    
    if df_analytics is not None:
        # Menghitung agregat status
        kritis = len(df_analytics[df_analytics['Status'].str.contains('Kritis|Buruk', case=False, na=False)])
        sedang = len(df_analytics[df_analytics['Status'].str.contains('Sedang', case=False, na=False)])
        normal = len(df_analytics[df_analytics['Status'].str.contains('Normal|Baik', case=False, na=False)])
        
        c1, c2, c3 = st.columns(3)
        c1.metric("Bulan Kritis", f"{kritis} Bulan", delta="Risiko Bencana Ekstrem", delta_color="inverse")
        c2.metric("Bulan Sedang", f"{sedang} Bulan", delta="Perlu Pemantauan", delta_color="off")
        c3.metric("Bulan Normal", f"{normal} Bulan", delta="Kondisi Terkendali", delta_color="normal")
        
        st.markdown("---")
        
        # Visualisasi Bar Chart
        fig = px.bar(
            df_analytics, 
            x='Periode', 
            y='KRS', 
            color='Status',
            title="Tren Fluktuasi Koefisien Rezim Sungai",
            text_auto='.1f',
            color_discrete_map={
                'Sangat Baik/Normal': '#2ecc71',
                'Sedang/Mulai Kritis': '#f1c40f',
                'Buruk': '#e67e22',
                'Sangat Buruk/Kritis': '#e74c3c'
            }
        )
        fig.update_layout(xaxis_title="Periode Waktu", yaxis_title="Skor KRS", height=450)
        st.plotly_chart(fig, use_container_width=True)
        
        st.subheader("Data Analitik Historis")
        # Menyembunyikan kolom Lag_Time_Jam agar tidak membingungkan fokus audiens dari topik KRS
        df_display = df_analytics.drop(columns=['Lag_Time_Jam'], errors='ignore')
        st.dataframe(df_display, use_container_width=True)
        
        st.warning("Peringatan Dampak (Contextual Intelligence): Peningkatan skor KRS mengindikasikan degradasi area resapan air di hulu. Fluktuasi muka air yang ekstrem mengancam pasokan air baku bagi populasi sekitar serta kebutuhan 135.675 hektar lahan pada Daerah Irigasi Rentang.")

# ==========================================
# HALAMAN 4: PETA SPASIAL
# ==========================================
elif menu == "Peta Infrastruktur Terpadu":
    st.header("Pemetaan Stasiun Hidrologi")
    st.markdown("Peta sebaran pos pengamatan curah hujan dan duga air berdasarkan titik koordinat dari pangkalan data utama.")
    
    if df_hujan is not None and df_air is not None:
        # Ambil titik koordinat unik dari setiap stasiun di database
        loc_hujan = df_hujan[['Nama_Stasiun', 'Latitude', 'Longitude']].drop_duplicates().dropna()
        loc_hujan['Tipe'] = 'Pos Pengamatan Curah Hujan'
        
        loc_air = df_air[['Nama_Stasiun', 'Latitude', 'Longitude']].drop_duplicates().dropna()
        loc_air['Tipe'] = 'Pos Pemantauan Muka Air'
        
        # Gabungkan data stasiun
        df_map = pd.concat([loc_hujan, loc_air], ignore_index=True)
        
        if not df_map.empty:
            pilihan_peta_2 = st.radio("Pilih Tampilan Peta Dasar:", ["Peta Terang (Default)", "Mode Gelap", "Peta Jalan (OSM)"], horizontal=True, key="peta_infra")
            
            style_dict = {
                "Peta Terang (Default)": "carto-positron",
                "Mode Gelap": "carto-darkmatter",
                "Peta Jalan (OSM)": "open-street-map"
            }
            
            fig = px.scatter_mapbox(
                df_map, 
                lat="Latitude", 
                lon="Longitude", 
                color="Tipe",
                hover_name="Nama_Stasiun",
                color_discrete_map={
                    'Pos Pengamatan Curah Hujan': '#3498db', 
                    'Pos Pemantauan Muka Air': '#e74c3c'
                },
                zoom=8, 
                center={"lat": -6.83, "lon": 108.15},
                title="Peta Titik Pantau Hidrologi (Versi Ringan)"
            )
            fig.update_layout(
                mapbox_style=style_dict[pilihan_peta_2], 
                margin={"r":0,"t":40,"l":0,"b":0}, 
                height=600,
                legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01)
            )
            
            st.plotly_chart(fig, use_container_width=True)
            st.info("Peta di atas diproses secara efisien dengan merender titik koordinat yang tertanam langsung di dalam database (tanpa harus memuat file spasial eksternal yang memberatkan memori).")
        else:
            st.warning("Data koordinat Latitude/Longitude tidak ditemukan di dataset.")

st.sidebar.markdown("---")
st.sidebar.caption("Sistem Pendukung Keputusan © 2026")
