**DOKUMEN RENCANA PROYEK (PROJECT PLAN)  
KERJA PRAKTIK**

*Cimanuk Basin Hydro-Environmental Analytics Dashboard (Cimanuk-HEAD):  
Prototipe Sistem Deteksi Dinamis Berdasarkan Kerusakan Ekologis Hulu  
Sesuai Framework Bidang 8 (Warning System) FFEWES Nasional*

| **Nama Lengkap**        | [Isi Nama Lengkap Anda]                                 |
|-------------------------|-----------------------------------------------------------|
| **NIM**                 | [Isi NIM Anda]                                          |
| **Program Studi**       | Sistem Informasi                                          |
| **Peminatan**           | Data Analytics                                            |
| **Instansi Penempatan** | Direktorat Bina Teknik SDA, Kementerian Pekerjaan Umum    |
| **Sistem Studi**        | Flood Early Warning and Flood Monitoring System (FFEWFMS) |

**A. RINGKASAN EKSEKUTIF (EXECUTIVE SUMMARY)**

**1. Problem Statement (Pernyataan Masalah)**

Kabupaten Garut dan wilayah Sumedang merupakan kawasan hulu kritis bagi
Daerah Aliran Sungai (DAS) Cimanuk. Aktivitas alih fungsi hutan menjadi
lahan pertanian monokultur serta pembukaan lahan secara masif di hulu
telah mengakibatkan penurunan kapasitas resapan air alami (infiltrasi).
Akibatnya, koefisien limpasan (run-off coefficient) meningkat tajam.
Ketika hujan ekstrem terjadi di hulu, air permukaan langsung mengalir
deras sebagai banjir bandang menuju hilir di wilayah Majalengka dan
Indramayu. Hal ini ditandai dengan memendeknya waktu jeda (lag time)
rambatan air secara signifikan. Selain itu, erosi tanah hulu mengangkut
sedimentasi pekat yang mendangkalkan palung sungai di hilir, membuat
kapasitas tampung sungai menyusut dramatis. Sungai Cimanuk menjadi
sangat sensitif, di mana duga muka air (AWLR) melonjak cepat meskipun
curah hujan (ARR) tidak se-ekstrem tahun-tahun sebelumnya.

Tantangan pada sistem monitoring hidrologi FFEWFMS milik Kementerian PU
saat ini adalah sistem peringatan dininya masih bersifat reaktif
(rule-based static threshold). Garis batas bahaya (Siaga 1-4) diatur
kaku secara statis sepanjang tahun tanpa memedulikan dinamika perubahan
tutupan lahan hulu maupun perubahan musim. Tidak adanya integrasi
informasi dampak kerusakan hutan dengan ambang batas bahaya hidrologi
berpotensi memicu kepatuhan alarm palsu (false alarms) atau
keterlambatan evakuasi warga.

**2. Research Questions (Pertanyaan Penelitian)**

Berdasarkan problem statement di atas, proyek ini dirancang untuk
menjawab pertanyaan-pertanyaan terukur berikut:

> • Bagaimana memprofilkan kualitas pengiriman data sensor ARR dan AWLR
> di DAS Cimanuk untuk mendeteksi tingkat keandalan data historis?
>
> • Bagaimana menghitung nilai selisih waktu puncak hidrologi hulu-hilir
> (lag time) secara historis menggunakan pustaka Pandas guna merancang
> indikator Lead Time Forecast?
>
> • Bagaimana menghitung nilai Koefisien Rezim Sungai (KRS) Cimanuk
> untuk merepresentasikan tingkat kritis degradasi lingkungan hulu
> secara kuantitatif?
>
> • Bagaimana membangun model sistem pendukung keputusan (DSS)
> interaktif berbasis Streamlit yang mengimplementasikan fitur Threshold
> by Condition dan Dynamic Threshold guna meningkatkan kesiapsiagaan
> masyarakat awam?

**3. Latar Belakang & Urgensi Penelitian**

Daerah Aliran Sungai (DAS) Cimanuk memiliki posisi strategis nasional
karena mengalir melintasi beberapa kabupaten penting di Jawa Barat dan
menyuplai air bagi infrastruktur vital seperti Waduk Jatigede. Kerusakan
ekologis berupa deforestasi hulu yang dibuktikan secara kualitatif oleh
laporan jurnalisme lingkungan (National Geographic & dokumenter
independen) harus dibuktikan secara ilmiah dan kuantitatif melalui
sinkronisasi data sensor hidrologi telemeteri milik Kementerian PU.
Urgensi proyek ini terletak pada pentingnya menjembatani kesenjangan
antara tim teknis hidrologi kementerian dengan masyarakat awam. Angka
debit air dan duga meter air yang rumit perlu ditranslasikan menjadi
bentuk visual yang intuitif seperti lag time perjalanan air dan
indikator kesiapan DAS.

**4. Justifikasi Pemilihan Proyek**

Proyek 'Cimanuk-HEAD' dipilih karena memenuhi tiga kriteria keberhasilan
Kerja Praktik (KP) mandiri yang sangat taktis:

> • Sesuai Peminatan SI-ITG: Melatih kemampuan manipulasi data runtun
> waktu (time-series) skala besar menggunakan Pandas dan visualisasi
> spasial menggunakan Folium.
>
> • Selesai Tepat Waktu (4-6 Minggu): Membatasi ruang lingkup hanya pada
> 1 Daerah Aliran Sungai (DAS Cimanuk) dan menghindari pemodelan Deep
> Learning yang rumit (seperti LSTM/GRU) sehingga bebas dari risiko RAM
> crash atau kegagalan komputasi di perangkat lokal.
>
> • Kontribusi Ilmiah Orisinal (Bidang 8 FFEWES): Membangun fitur
> penunjang keputusan (DSS) dinamis yang statusnya masih tertulis
> 'Belum' dikerjakan oleh pihak pelaksana proyek nasional, memberikan
> daya tawar akademik tinggi di hadapan dosen penguji.

**B. CAKUPAN PROYEK DAN HASIL KERJA (SCOPE & DELIVERABLES)**

Untuk memastikan proyek selesai dalam rentang 4 hingga 6 minggu secara
mandiri, batasan cakupan proyek (Project Scope Boundaries) diatur secara
tegas dalam tabel matriks berikut:

| **Kategori**                    | **Termasuk dalam Scope (In-Scope)**                                                                                                                                    | **Tidak Termasuk (Out-of-Scope)**                                                                                                             |
|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| **Fokus Wilayah**               | Pengolahan data spasial-temporal khusus stasiun hidrologi (ARR, AWLR, AWS) yang berada di sepanjang aliran Daerah Aliran Sungai (DAS) Cimanuk.                         | Pengolahan stasiun hidrologi di luar DAS Cimanuk (seperti DAS Babakan, DAS Jragung, DAS Juwana, atau wilayah Jawa Tengah lainnya).            |
| **Metode Analitik**             | Perhitungan statistik deskriptif harian, pencarian selisih waktu puncak banjir (Lag Time), penghitungan KRS Cimanuk, serta audit data kosong (Missing Data Profiling). | Penerapan model deep learning runtun waktu (Time-Series Forecasting seperti LSTM/GRU) atau analisis korelasi spasial-temporal tingkat lanjut. |
| **Infrastruktur & Penyimpanan** | Penyimpanan dataset bersih dalam format CSV lokal, visualisasi peta interaktif berbasis Folium, dan perakitan layout dashboard multi-halaman berbasis Streamlit.       | Pembangunan pipa data otomatis real-time skala industri, database cloud enterprise berbayar, atau deployment pada hosting AWS/GCP.            |
| **Teknologi & Stack**           | Bahasa Python 3.9+ menggunakan Pandas, Plotly, Folium, missingno, dan Streamlit Community Cloud (gratis).                                                              | Pengembangan front-end berbasis framework JavaScript (React, Vue) atau integrasi backend RESTful API yang kompleks.                           |

**Hasil Kerja Nyata (Final Deliverables):**

> • Website MVP Cimanuk-HEAD: Dashboard interaktif 3 halaman (Lag Time
> Tracker, Basin Health KRS, Spatial & Dynamic Threshold Map) yang
> di-deploy online di Streamlit Community Cloud.
>
> • Dataset Bersih Cimanuk (Format CSV): File master data historis ARR
> dan AWLR DAS Cimanuk yang telah dibersihkan dari pencilan (outliers)
> dan di-imputasi nilai kosongnya.
>
> • Repositori Kode GitHub (Private): Berisi seluruh source code
> pemrograman terstruktur, file konfigurasi, and README.md instruksi
> replikasi.
>
> • Laporan Tertulis Bab IV Kerja Praktik: Menyajikan analisis
> karakteristik hidrologi komparatif, visualisasi dashboard, pembuktian
> teori kerusakan hutan, dan panduan mitigasi warga.

**C. JADWAL PENGERJAAN & TIMELINE**

Kegiatan Kerja Praktik ini dipadatkan secara ketat ke dalam \*\*4 minggu
(1 Bulan) efektif\*\* agar hasil pekerjaan tuntas sebelum masa kuliah
Semester 7 dimulai. Alokasi waktu detail per fase disajikan pada tabel
di bawah ini:

| **Minggu**   | **Fase Kegiatan**                     | **Aktivitas Pekerjaan**                                                                                                                                                                                                                                                                                                                              | **Milestone / Deliverable**                                                                                       |
|--------------|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| **Minggu 1** | Akuisisi Data & Setup (Extract)       | Observasi mendalam platform FFEWFMS KemenPU. Memetakan koordinat stasiun ARR, AWLR, dan AWS khusus di sepanjang aliran Sungai Cimanuk (wd.fews-cs07.cloud/stasiun-hidrologi). Mengunduh berkas log historis (format CSV/XLSX) dengan rentang data minimal 5 tahun terakhir (periode 2021-2026/2022-2026) untuk analisis runtun waktu jangka panjang. | M1: Berkas raw dataset historis khusus stasiun DAS Cimanuk berhasil terkumpul di lingkungan lokal.                |
| **Minggu 2** | Data Wrangling & Analisis (Transform) | Pembersihan data kosong (missing values) menggunakan teknik interpolasi linear di Pandas. Menyaring data pencilan (outliers) akibat galat transmisi telemeteri. Menghitung selisih waktu puncak hujan hulu dan puncak air hilir (lag time) serta merumuskan basis logika perhitungan KRS.                                                            | M2: Dataset bersih (master.csv) siap digunakan dan pohon keputusan berbasis aturan (rule-based) telah dirumuskan. |
| **Minggu 3** | Dashboard Development (Load)          | Membangun visualisasi interaktif (grafik garis Plotly hulu-hilir, grafik bar KRS, dan peta sebaran stasiun berbasis Folium). Merakit seluruh komponen visualisasi ke dalam dashboard multi-halaman web berbasis Streamlit.                                                                                                                           | M3: Aplikasi dashboard Cimanuk-HEAD selesai dibangun secara lokal dan seluruh tombol filter berfungsi.            |
| **Minggu 4** | Rilis Aplikasi & Dokumentasi          | Melakukan deployment aplikasi dasbor Cimanuk-HEAD secara gratis ke server Streamlit Community Cloud. Melakukan pengujian antarmuka bersama dosen pembimbing, perbaikan galat (bug fixing), serta merampungkan dokumen Bab 4 Laporan KP SI-ITG.                                                                                                       | M4: Aplikasi live terpublikasi gratis dan draf Laporan Kerja Praktik Bab 1-5 selesai disusun.                     |

**D. URAIAN RENCANA PENUGASAN (JOB DESK)**

Sesuai dengan ketentuan okupasi Buku Kendali KP Sistem Informasi ITG,
meskipun proyek ini dikerjakan secara mandiri oleh satu mahasiswa
(Single Fighter), peran pekerjaan dibagi secara profesional berdasarkan
klaster keahlian teknis berikut:

**1. Peran Arsitek Data (Data Architect)**

> • Merancang struktur penyimpanan pangkalan data lokal berbasis
> flat-file (.csv) hasil unduhan platform FFEWFMS KemenPU.  
> • Memetakan skema integrasi data spasial (koordinat latitude/longitude
> pos sensor) dengan data atribut runtun waktu (ARR & AWLR).  
> • Menetapkan standar normalisasi timestamp dan satuan unit sensor (mm
> untuk curah hujan, meter untuk tinggi air).

**2. Peran Data Analyst (Fokus Utama)**

> • Melakukan Exploratory Data Analysis (EDA) untuk mengidentifikasi
> korelasi curah hujan hulu terhadap luapan sungai hilir.  
> • Melakukan proses Data Cleaning untuk mendeteksi data pencilan
> (outliers) dan melakukan imputasi data kosong.  
> • Menghitung parameter hidro-ekologis hulu-hilir (perhitungan KRS
> Cimanuk dan pergeseran waktu lag-time).  
> • Menyusun narasi interpretasi hasil data hidrologi menjadi
> rekomendasi mitigasi bencana bencana.

**3. Peran Analis Program (Program Analyst)**

> • Membangun antarmuka dashboard multi-halaman yang interaktif
> menggunakan kerangka kerja Streamlit.  
> • Melakukan integrasi komponen visualisasi grafik Plotly dan peta
> spasial Folium agar terpasang secara dinamis.  
> • Melakukan unit testing terhadap responsivitas fungsionalitas tombol
> filter stasiun, filter bulan, dan slider sensitivitas.  
> • Melakukan deployment aplikasi web ke Streamlit Community Cloud serta
> menjamin kesiapan aksesibilitas publik.

**E. SUMBER DAYA PROYEK (PROJECT RESOURCES)**

Kebutuhan perangkat keras, perangkat lunak, dan pustaka kode pemrograman
yang akan digunakan untuk mendukung kelancaran eksekusi proyek
Cimanuk-HEAD selama 4 minggu ini dirinci sebagai berikut:

**1. Bahasa Pemrograman & Framework**

> • Python 3.9+: Bahasa pemrograman utama untuk seluruh alur ETL
> (Extract, Transform, Load) dan kalkulasi statistik.  
> • Streamlit Framework: Alat pembangun aplikasi web interaktif yang
> efisien tanpa memerlukan keahlian HTML/CSS lanjutan.

**2. Pustaka Manipulasi & Visualisasi Data**

> • Pandas & NumPy: Digunakan untuk wrangling data, manipulasi tabel,
> parsing timestamp, dan perhitungan agregat harian/bulanan.  
> • Plotly Express: Digunakan untuk membuat grafik garis (line chart)
> tren hidrologi hulu-hilir dan grafik batang KRS yang interaktif.  
> • Folium & Branca: Digunakan untuk membangun visualisasi peta spasial
> interaktif aliran Sungai Cimanuk dan sebaran pos sensor.  
> • missingno: Digunakan untuk mengaudit sebaran data bolong (missing
> value profiling) secara visual pada tahap transformasi.

**3. Environment & Tools Pengembangan**

> • Visual Studio Code (VS Code): Editor kode lokal utama untuk merakit
> file skrip python dashboard.  
> • Google Colaboratory: Platform cloud berbasis Jupyter Notebook untuk
> mempercepat analisis eksplorasi data awal.  
> • Git & GitHub: Sistem version control terpusat untuk menyimpan kode
> sumber secara aman dan teratur.  
> • Figma: Alat desain UI/UX untuk merancang wireframe visual halaman
> dasbor sebelum masuk ke tahap pengodean.

**4. Dataset Studi Kasus (DAS Cimanuk)**

> • Data ARR (Pos Curah Hujan): Data intensitas hujan harian historis
> dari stasiun hulu Cimanuk (Jatigede, Cipasang, Cikajang, Bayongbong,
> Pajajar).  
> • Data AWLR (Pos Tinggi Muka Air): Data elevasi air sungai harian
> historis dari stasiun duga air (Cimanuk-Rentang, Cimanuk-Leuwidaun,
> Cimanuk-Bayongbong, Cilutung-Kamun, Cilutung-Kadumalik).  
> • Metadata Stasiun: Titik koordinat geografis stasiun, wilayah
> administrasi BWS, Daerah Aliran Sungai (DAS), dan batas threshold
> bahaya.

**F. RENCANA MANAJEMEN RISIKO DAN ISU**

Untuk meminimalkan potensi kegagalan proyek Kerja Praktik mandiri ini,
dilakukan analisis SWOT serta penyusunan skenario mitigasi risiko teknis
sebagai berikut:

**1. Analisis SWOT Proyek**

> • KEKUATAN (STRENGTHS):  
> - Fokus area sangat spesifik (DAS Cimanuk) sehingga pengolahan data
> lebih padat dan mendalam.  
> - Orisinalitas tinggi karena mensimulasikan fitur Bidang 8 FFEWES
> nasional yang belum dikembangkan oleh kementerian.  
> • KELEMAHAN (WEAKNESSES):  
> - Ketergantungan penuh pada data historis telemeteri yang sering
> mengalami data kosong (not update/offline).  
> - Pengerjaan mandiri (single fighter) menuntut manajemen waktu yang
> sangat disiplin selama 4 minggu.  
> • PELUANG (OPPORTUNITIES):  
> - Hasil prototipe dasbor Streamlit dapat ditawarkan langsung sebagai
> alat bantu audit keandalan sensor bagi teknisi BWS.  
> - Skalabilitas sistem sangat terbuka untuk diaplikasikan pada wilayah
> sungai lain seperti BBWS Pemali Juana.  
> • ANCAMAN (THREATS):  
> - Risiko anomali data (noise/outlier) akibat gangguan alat fisik di
> lapangan yang dapat merusak akurasi perhitungan lag time.  
> - Limitasi RAM atau waktu muat (loading time) pada server gratis
> Streamlit Cloud saat memproses dataset spasial besar.

**2. Skenario Mitigasi Risiko Teknis**

> **• Isu Data Kosong (Missing Values) pada Sensor:  
> ** - Mitigasi: Karena kita mengolah data temporal jangka panjang
> (minimal 5 tahun terakhir), penanganan data kosong (missing values)
> harus dilakukan secara defensif. Untuk missing values berdurasi
> singkat (\< 3 jam), Pandas akan mengisinya secara otomatis menggunakan
> teknik interpolasi linear. Jika terjadi sensor offline dalam skala
> panjang (\> 3 jam), data tidak akan langsung dihapus melainkan
> ditandai (flagged) secara khusus. Penghitungan statistik bulanan atau
> perhitungan KRS harian hanya akan melibatkan baris data yang valid
> agar tidak mendistorsi pola musiman (seasonal patterns) historis
> selama 5 tahun tersebut.  
> **• Isu Kelangkaan Data Historis Jangka Panjang (Minimal 5 Tahun):  
> ** - Mitigasi: Guna memitigasi risiko kelangkaan data pada stasiun
> tertentu (misal stasiun hidrologi baru yang belum genap beroperasi
> selama 5 tahun), pengembang akan melakukan validasi keandalan data
> (data completeness checks) sejak awal. Jika terdapat stasiun yang data
> historisnya tidak mencapai 5 tahun, statusnya akan dicatat sebagai
> keterbatasan proyek (project limitation). Analisis korelasi dan
> visualisasi lag time serta indeks KRS akan diarahkan pada
> stasiun-stasiun utama DAS Cimanuk yang memiliki rekam data hidrologis
> matang dan kontinu selama periode 5 tahun tersebut (misalnya stasiun
> AWLR Cimanuk-Rentang dan stasiun ARR Jatigede).  
> **• Isu Keterbatasan Server Hosting Streamlit Cloud (dengan Dataset
> Big Data 5 Tahun):  
> ** - Mitigasi: Memuat data mentah (raw data) per jam dari puluhan pos
> sensor selama 5 tahun penuh (jutaan baris) ke dalam visualisasi
> dinamis di Streamlit Cloud dapat menyebabkan server kelebihan beban
> RAM (RAM overflow) dan memicu crash. Sebagai mitigasi teknis,
> pengembang akan melakukan agregasi di awal (pre-aggregation) di sisi
> lokal terlebih dahulu sebelum data diunggah. Data mentah harian
> didegradasi menjadi resolusi harian (daily averages) atau bulanan
> (monthly index). Selain itu, dataset hasil transformasi akan disimpan
> dalam format Parquet yang dikompresi (bukan format CSV biasa), serta
> membagi muatan visualisasi per halaman menggunakan dekorator cache
> Streamlit (@st.cache_data dan @st.cache_resource) secara ketat demi
> menjamin kecepatan rendering peta Folium dan grafik Plotly dalam
> hitungan milidetik.

Garut, 8 Agustus 2026  
  
Menyetujui,

| **( Dr. Dede Kurniadi, S.Kom., M.Kom. )** <br> Dosen Pembimbing Akademik <br> NIDN. 0402059202 | **( [Isi Nama Anda] )** <br> Mahasiswa Praktikan <br> NIM. [Isi NIM Anda] |
| :--- | :--- |
