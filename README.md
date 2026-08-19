# Cimanuk-HEAD: Hydro-Environmental Analytics Dashboard

[![Live Demo](https://img.shields.io/badge/Live_Demo-cimanuk--head.riyandimhmdr.my.id-blue?style=for-the-badge&logo=vercel)](https://cimanuk-head.riyandimhmdr.my.id)
[![Python](https://img.shields.io/badge/Python-3.10+-yellow?style=for-the-badge&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.22+-FF4B4B?style=for-the-badge&logo=streamlit)](https://streamlit.io/)

Sistem Pendukung Keputusan (DSS) Dual-Mitigasi Bencana Hidrometeorologi pada Balai Besar Wilayah Sungai (BBWS) Cimanuk-Cisanggarung.

## Deskripsi Proyek
Proyek ini merupakan Sistem Peringatan Dini dan Analitik Hidrologi berbasis WebGIS dan Big Data. Dibangun khusus untuk mengolah data telemetri historis (Sensor Curah Hujan & Muka Air) menjadi informasi visual operasional guna memitigasi bencana banjir jangka pendek dan degradasi ekologis DAS jangka panjang.

## Fitur Utama
1. **Arsitektur Big Data (Apache Parquet):** Mengkompresi dataset hidrologi historis menjadi format columnar untuk mempercepat proses render di dasbor secara efisien.
2. **Lag Time Tracker (Banjir):** Algoritma Cross-Correlation yang mengalkulasi waktu jeda rambat air dari hulu (gunung) ke hilir (bendung).
3. **Diagnosis Kesehatan DAS (KRS):** Menghitung secara dinamis fluktuasi Koefisien Rezim Sungai (Muka Air Tertinggi vs Terendah) sebagai indikator empiris laju deforestasi hulu.
4. **Spatial Intelligence (WebGIS):** Peta persebaran stasiun sensor yang merender otomatis geometri Daerah Aliran Sungai (DAS) tanpa memuat perangkat lunak GIS tambahan.

## Teknologi yang Digunakan
* **Frontend/UI:** Streamlit, Plotly
* **Backend/Data Engineering:** Pandas, PyArrow
* **Spatial Processing:** GeoPandas, Pyogrio, Folium
* **Deployment:** Vercel Proxy, Streamlit Community Cloud

## Panduan Instalasi Lokal

1. **Clone Repositori:**
   ```bash
   git clone https://github.com/riyandimuhamad/Cimanuk-HEAD.git
   cd Cimanuk-HEAD
   ```

2. **Install Dependensi:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Jalankan Aplikasi:**
   ```bash
   streamlit run src/app.py
   ```

4. Akses melalui browser pada alamat `http://localhost:8501`

---
*Proyek ini disusun sebagai pemenuhan syarat Kerja Praktik Program Studi Sistem Informasi.*
*Hak cipta data milik BBWS Cimanuk-Cisanggarung.*
