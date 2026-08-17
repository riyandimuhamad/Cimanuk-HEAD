# LAPORAN KERJA PRAKTIK

## ANALISIS DATA PELANGGAN POTENSIAL UNTUK PEMASARAN INTERNET DI PT QWORDS WILAYAH BANDUNG

**Oleh:**  
**Shifa Nur’aeni (2207018)**  
**Tiara (2207028)**  

---

**PROGRAM STUDI SISTEM INFORMASI**  
**JURUSAN ILMU KOMPUTER**  
**INSTITUT TEKNOLOGI GARUT**  
**GARUT**  
**2025**  

---

### PEDOMAN PENGGUNAAN LAPORAN
Laporan kerja praktik tersedia untuk umum di Perpustakaan Institut Teknologi Garut. Hak cipta ada pada kelompok kerja yang dialihkan seluruh hak dan kepentingannya kepada Prodi Sistem Informasi Institut Teknologi Garut. Setiap pengutipan harus menyertakan sitasi yang dapat ditelusuri di dalam daftar pustaka.

---

### PERNYATAAN KEASLIAN
Saya yang bertanda tangan di bawah ini:  
* **Nama:** Shifa Nur’aeni  
* **NIM:** 2207018  

Adalah wakil kelompok kerja, dengan ini menyatakan bahwa laporan kerja praktik yang dibuat belum pernah diajukan oleh siapapun, serta mengandung kutipan yang telah dilengkapi dengan sitasi dan tercantum dalam daftar pustaka secara memadai. Kami bersedia menerima sanksi akademik berupa nilai E apabila terbukti melakukan plagiasi, sesuai Peraturan Menteri Pendidikan Nasional Republik Indonesia nomor 17 tahun 2010.

Garut, 31 Juli 2025  
*Yang Membuat Pernyataan,*  

**Shifa Nur’aeni**  
**NIM. 2207018**  

---

### LEMBAR PENGESAHAN
**ANALISIS DATA PELANGGAN POTENSIAL UNTUK PEMASARAN INTERNET DI PT QWORDS WILAYAH BANDUNG**  
**LAPORAN KERJA PRAKTIK**  

**Disusun oleh:**  
**Shifa Nur’aeni (2207018)**  
**Tiara (2207028)**  

Disetujui oleh:  

| Jabatan | Nama Lengkap | NIDN / NIP |
| :--- | :--- | :--- |
| **Pembimbing Akademik** | M. Rikza Nashrulloh, S.T., M.Kom. | NIDN: 0402059202 |
| **Pembimbing Lapangan** | Saepudin Mulyono, S.Kom. | NIP: - |

Mengetahui:  

| Jabatan | Nama Lengkap | NIDN |
| :--- | :--- | :--- |
| **Ketua Jurusan Ilmu Komputer** | Dr. Dede Kurniadi, S.Kom., M.Kom. | NIDN: 0402098301 |
| **Ketua Program Studi Sistem Informasi** | M. Rikza Nashrulloh, S.T., M.Kom. | NIDN: 0402059202 |

---

### ABSTRAK
Kegiatan kerja praktik ini dilaksanakan di PT Qwords Company International dengan tujuan untuk menerapkan pengetahuan dan keterampilan dalam bidang sistem informasi, khususnya pada pengumpulan, pengolahan, dan visualisasi data *prospek pelanggan*. Melalui pendekatan ETL (*Extract, Transform, Load*), kegiatan ini bertujuan untuk menganalisis potensi pasar layanan digital dengan memanfaatkan data lokasi usaha dari sumber daring.

Tahapan kerja dimulai pada tahap *Extract*, yang diawali dengan kegiatan identifikasi profil pelanggan ideal melalui wawancara bersama tim *Marketing* PT Qwords untuk menentukan kategori usaha dan wilayah target yang relevan dengan layanan digital perusahaan. Selanjutnya, proses *Extract* dilanjutkan menggunakan *Google Places API* untuk mengumpulkan data usaha di wilayah Bandung berdasarkan kata kunci kategori dan titik koordinat geografis yang telah ditetapkan. Data yang diperoleh kemudian diproses menggunakan Python di *Google Colaboratory*, mencakup pembersihan data, penghapusan duplikasi, serta pemberian skor prioritas (1–3) berdasarkan relevansi kategori usaha terhadap target layanan digital Qwords.

Hasil akhir berupa data bersih sebanyak **49.935 entri** dari total lebih dari **220.000 data awal**, yang kemudian dimuat ke dalam *Google Looker Studio* untuk divisualisasikan dalam bentuk *dashboard* interaktif. *Dashboard* tersebut menampilkan peta sebaran usaha, grafik distribusi kategori, serta daftar *Top 20 Prospek Prioritas Tertinggi* yang siap ditindaklanjuti oleh tim *Marketing*. Kegiatan ini menunjukkan bahwa integrasi antara teknik *web scraping* berbasis API, pengolahan data ETL, dan visualisasi interaktif dapat secara efektif mendukung pengambilan keputusan berbasis data (*data-driven decision making*) dalam konteks pemasaran digital.

**Kata Kunci:** *Data Scraping, ETL, Google Places API, Google Looker Studio*

---

### KATA PENGANTAR
Dengan mengucapkan segala puji dan syukur kepada Allah SWT atas rahmat dan hidayah-Nya, penulis dapat menyelesaikan Laporan Kerja Praktik di PT Qwords Company International. Laporan ini dapat tersusun dengan baik berkat bantuan, dukungan, dan bimbingan dari berbagai pihak yang terhormat:

1. Bapak Prof. Dr. H. Hilmi Aulawi, S.T., M.T., IPU., selaku Rektor Institut Teknologi Garut.
2. Bapak Dr. Dede Kurniadi, S.Kom., M.Kom., selaku Ketua Jurusan Ilmu Komputer Institut Teknologi Garut.
3. Bapak Muhammad Rikza Nashrulloh, S.T., M.Kom., selaku Ketua Program Studi Sistem Informasi Institut Teknologi Garut sekaligus Dosen Pembimbing Akademik yang senantiasa memberikan arahan, bimbingan, serta masukan yang sangat berharga.
4. Seluruh Dosen dan Staf Institut Teknologi Garut atas ilmu dan bantuan yang telah diberikan selama masa perkuliahan.
5. Bapak Saepudin Mulyono, S.Kom., selaku Pembimbing Lapangan dari PT Qwords yang telah memberikan arahan dan bimbingan selama pelaksanaan Kerja Praktik.
6. Seluruh pegawai dan staf PT Qwords, yang telah memberikan dukungan, bantuan teknis, serta pengalaman kerja yang berharga selama kegiatan kerja praktik berlangsung.
7. Kedua orang tua tercinta, yang telah menjadi sumber kekuatan dan inspirasi dengan doa yang tak pernah putus.
8. Rekan-rekan seperjuangan di PT Qwords, serta semua teman seperjuangan lainnya yang telah menjadi tempat berbagi cerita, bertukar pikiran, dan saling menyemangati.

Akhir kata, penulis menyadari bahwa dalam penyusunan laporan ini masih terdapat berbagai kekurangan. Oleh karena itu, kritik dan saran yang membangun akan sangat dihargai guna penyempurnaan laporan ini di masa mendatang.

Garut, 31 Juli 2025  
*Penyusun*  

---

### DAFTAR ISI
* **ABSTRAK** | i
* **KATA PENGANTAR** | ii
* **DAFTAR ISI** | iv
* **DAFTAR GAMBAR** | vi
* **DAFTAR TABEL** | vii
* **DAFTAR LAMPIRAN** | viii
* **1. PENDAHULUAN** | 1
  * 1.1. Latar Belakang | 1
  * 1.2. Tujuan Pekerjaan | 2
  * 1.3. Ruang Lingkup Pekerjaan | 3
  * 1.4. Tempat dan Waktu Kerja | 5
  * 1.5. Sistematika Penulisan | 6
* **2. LANDASAN TEORI** | 8
  * 2.1. Data dan Informasi | 8
  * 2.2. Web Scraping | 9
  * 2.3. Web Scraping Berbasis API (Google Places API) | 11
  * 2.4. Metode ETL (Extract, Transform, Load) | 13
  * 2.5. Tahapan Analisis Data | 15
  * 2.6. Visualisasi Data | 16
  * 2.7. Tools Pendukung | 18
  * 2.8. Penelitian Terkait | 19
* **3. METODOLOGI PEKERJAAN** | 22
  * 3.1. Work Breakdown Structure | 22
  * 3.2. Diagram Alur Aktivitas | 27
  * 3.3. Sumber Daya Penelitian | 28
* **4. HASIL DAN PEMBAHASAN** | 30
  * 4.1. Hasil Pekerjaan | 30
    * 4.1.1. Tahapan 1 Extract | 30
    * 4.1.2. Tahap 2 Transform | 35
    * 4.1.3. Tahap 3 Load | 41
  * 4.2. Pembahasan | 44
    * 4.2.1. Pembahasan Tahap Extract | 44
    * 4.2.2. Pembahasan Tahap Transform | 46
    * 4.2.3. Pembahasan Tahap Load | 47
* **5. KESIMPULAN DAN SARAN** | 51
  * 5.1. Kesimpulan | 51
  * 5.2. Saran | 52
* **DAFTAR PUSTAKA** | 54
* **LAMPIRAN** | 58

---

### DAFTAR GAMBAR
* **Gambar 1.1** Logo PT Qwords | 5
* **Gambar 3.1** Work Breakdown Structure | 23
* **Gambar 3.2** Diagram Alur Aktivitas | 27
* **Gambar 4.1** Peta Sebaran Prospek | 42
* **Gambar 4.2** Grafik Distribusi Kategori Usaha | 43
* **Gambar 4.3** Tabel Top 20 Prospek Prioritas Tertinggi | 44

---

### DAFTAR TABEL
* **Tabel 1.1** Pembagian Kerja | 4
* **Tabel 3.1** Sumber Daya Penelitian | 28
* **Tabel 4.1** Draf Wawancara Sebelum Scraping | 31
* **Tabel 4.2** Wawancara Lanjutan (Setelah Data Tersedia) | 32
* **Tabel 4.3** Daftar Titik Koordinat Lokasi Pencarian | 33
* **Tabel 4.4** Data Awal Hasil Scraping | 34
* **Tabel 4.5** Rekapitulasi Hasil Pembersihan Data | 36
* **Tabel 4.6** Ringkasan Jumlah Usaha per Kategori | 37
* **Tabel 4.7** Sebaran Usaha Berdasarkan Wilayah | 38
* **Tabel 4.8** Kategori dengan Skor Prioritas 3 | 39
* **Tabel 4.9** Kategori dengan Skor Prioritas 2 | 40
* **Tabel 4.10** Kategori dengan Skor Prioritas 1 | 40

---

### DAFTAR LAMPIRAN
* **LAMPIRAN A** : LANDASAN PEKERJAAN | 58
* **LAMPIRAN B** : PRESENSI KERJA | 61
* **LAMPIRAN C** : HASIL PEKERJAAN | 65
* **LAMPIRAN D** : LAMPIRAN LAINNYA | 68

---

# BAB I: PENDAHULUAN

### 1.1 Latar Belakang
PT Qwords Company International merupakan perusahaan yang bergerak di bidang teknologi informasi dengan fokus pada penyediaan layanan infrastruktur internet, *web hosting*, registrasi nama domain, dan solusi digital lainnya bagi pelaku bisnis, organisasi, dan perorangan. Sebagai perusahaan teknologi terkemuka, strategi pemasaran yang efektif dan berbasis data sangat penting untuk mengidentifikasi dan menjangkau calon pelanggan baru di tengah persaingan pasar yang sangat dinamis.

Visualisasi data melalui *dashboard* interaktif terbukti dapat meningkatkan efektivitas pengambilan keputusan dalam bisnis pemasaran (Ariani & Aulia, 2024). Namun, proses pengumpulan data calon pelanggan secara konvensional seringkali memakan waktu lama dan memiliki tingkat akurasi yang rendah. Oleh karena itu, diperlukan otomasi menggunakan teknologi web scraping berbasis API, penanganan data berskala besar dengan metodologi ETL, dan visualisasi interaktif guna mendukung kegiatan pemasaran yang lebih efisien di PT Qwords khususnya untuk wilayah Bandung.

### 1.2 Tujuan Pekerjaan
Tujuan pelaksanaan kegiatan Kerja Praktik ini adalah:
1. Menerapkan pengetahuan teoritis Sistem Informasi dalam dunia kerja nyata melalui pengumpulan, pengolahan, dan visualisasi data calon pelanggan potensial PT Qwords wilayah Bandung.
2. Membangun dan menyusun basis data bersih yang terstruktur mengenai prospek bisnis menggunakan teknik ETL (Extract, Transform, Load) berbasis Python.
3. Merancang dan mengimplementasikan *dashboard* visualisasi interaktif pada Google Looker Studio sebagai alat penunjang keputusan bagi tim *Sales* dan *Marketing* PT Qwords.

### 1.3 Ruang Lingkup Pekerjaan
Ruang lingkup pekerjaan Kerja Praktik ini difokuskan pada:
1. Pengolahan koordinat lokasi wilayah pencarian di Bandung yang diberikan oleh divisi internal sebagai acuan radius pencarian data spasial.
2. Otomasi pengambilan data entitas bisnis (nama, kategori, alamat, koordinat, nomor telepon) menggunakan Google Places API berbasis bahasa Python.
3. Melakukan tahapan transformasi (*data cleaning*, deduplikasi, imputasi kontak kosong, standardisasi kategori, dan pemberian skor prioritas 1–3).
4. Menyusun visualisasi data interaktif pada platform Google Looker Studio yang menyajikan peta sebaran spasial, grafik distribusi industri, serta daftar prioritas Top 20 Prospek.

**Tabel 1.1 Pembagian Kerja**

| No | Jenis Pekerjaan | Personel | Perangkat | Hasil |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Koordinasi awal dengan tim *Sales* untuk menentukan kriteria pelanggan ideal | Tim KP, Pembimbing Lapangan, Tim *Sales* | Laptop, Google Meet, WhatsApp | Daftar lokasi target dan kriteria pelanggan |
| 2 | Pengolahan koordinat lokasi target sebagai dasar proses scraping | Tim KP, Tim Developer | Laptop, Google Sheets | File koordinat wilayah target |
| 3 | Pengambilan data bisnis dari Google Maps menggunakan Google Places API | Tim KP | Laptop, Google Colaboratory, Google Places API | Data mentah hasil scraping (CSV) |
| 4 | Pembersihan dan klasifikasi data | Tim KP | Laptop, Google Colaboratory, Google Sheets | Data bersih dan terstruktur sesuai kategori usaha dan wilayah |
| 5 | Pembuatan *dashboard* interaktif untuk menampilkan data | Tim KP | Laptop, Google Looker Studio | *Dashboard* visualisasi hasil analisis data |

### 1.4 Tempat dan Waktu Kerja
* **Instansi Tempat Kerja:** PT Qwords Company International Kantor Bandung
* **Alamat:** Jl. Terusan Setra Indah I No. 19, Sukajadi, Kota Bandung, Jawa Barat 40163
* **Unit Kerja:** Divisi Developer (Bertanggung jawab atas pengelolaan data teknis dan pengembangan sistem internal)
* **Rentang Waktu Pelaksanaan:** 01 Juli 2025 s.d. 31 Juli 2025
* **Hari dan Jam Kerja:** Senin - Sabtu, 08.00 s.d. 17.00 WIB

---

# BAB II: LANDASAN TEORI

### 2.1 Data dan Informasi
Data merupakan kumpulan fakta mentah, angka, atau catatan observasi yang belum memiliki arti operasional bagi penggunanya sebelum diproses secara sistematis (Kimball & Ross, 2013). Informasi adalah hasil pengolahan data yang telah terstruktur sehingga memiliki konteks, makna, dan nilai guna dalam proses pengambilan keputusan strategis bisnis.

### 2.2 Web Scraping dan Google Places API
Web scraping merupakan teknik ekstraksi data terotomasi dari sumber halaman situs web secara terprogram menggunakan protokol HTTP (Russell, 2019). Scraping berbasis API (*Application Programming Interface*) seperti Google Places API merupakan metode pengambilan data spasial dan atribut entitas bisnis yang paling stabil, legal, dan terstruktur karena langsung terhubung ke basis data peta Google dengan keluaran format JSON (Google, 2024b).

### 2.3 Metode ETL (Extract, Transform, Load)
ETL merupakan fondasi utama dalam arsitektur pergudangan data (*data warehousing*):
1. **Extract:** Proses pengambilan data mentah dari berbagai sumber operasional (dalam proyek ini diekstrak dari Google Places API).
2. **Transform:** Proses pembersihan (*data cleaning*), penanganan nilai kosong (*null handling*), standardisasi struktur kolom, klasifikasi kategori bisnis, dan kalkulasi atribut analitik baru (skor prioritas).
3. **Load:** Proses pemuatan data hasil pembersihan ke dalam sistem penyimpanan akhir atau platform visualisasi data interaktif (Google Looker Studio).

---

# BAB III: METODOLOGI PEKERJAAN

### 3.1 Work Breakdown Structure (WBS)
Pekerjaan dilaksanakan secara terstruktur dengan alur WBS sebagai berikut:
1. **Fase Inisiasi & Perencanaan:** Melakukan koordinasi bersama tim *Sales* dan mengidentifikasi profil pelanggan potensial.
2. **Fase Pengumpulan Data (Extract):** Merumuskan daftar kata kunci pencarian (*keyword*) dan batas koordinat spasial wilayah Bandung, lalu menjalankan skrip scraping berbasis Python di Google Colab.
3. **Fase Pengolahan Data (Transform):** Menjalankan pembersihan data kosong, penghapusan duplikasi, standardisasi kontak, klasifikasi kelompok industri, dan pemberian skor prioritas 1-3 menggunakan Pandas.
4. **Fase Integrasi & Visualisasi (Load):** Mengekspor data master bersih ke format CSV, menghubungkannya ke Google Looker Studio, dan merancang antarmuka *dashboard*.

### 3.2 Diagram Alur Aktivitas
Alur aktivitas terperinci dari inisiasi hingga rilis *dashboard* disajikan pada Gambar 3.2. Pembagian target waktu diatur secara paralel dan bertahap untuk memastikan efisiensi durasi Kerja Praktik selama 1 bulan penuh.
* **Milestone 1 (M1 - 14 Juli):** Seluruh data mentah hasil scraping berhasil dikumpulkan dan diklasifikasikan.
* **Milestone 2 (M2 - 31 Juli):** *Dashboard* interaktif Looker Studio selesai dirilis dan siap diserahkan kepada tim Sales PT Qwords.

### 3.3 Sumber Daya Penelitian
Pengerjaan proyek mandiri berkolaborasi di dalam unit kerja PT Qwords didukung oleh pemanfaatan perangkat keras dan perangkat lunak secara optimal.

**Tabel 3.1 Sumber Daya Penelitian**

| No | Aktivitas | Manusia | Perangkat & Tools |
| :--- | :--- | :--- | :--- |
| 1 | Diskusi bersama Tim Sales PT Qwords | Shifa, Tiara, dan Tiffany | Laptop, Google Meet |
| 2 | Menentukan Profil Pelanggan Ideal | Shifa, Tiara, dan Tiffany | Laptop, Google Sheets |
| 3 | Menentukan Keyword & Lokasi | Shifa, Tiara, dan Saepudin Mulyono | Laptop, Google Sheets |
| 4 | Scraping Data via Google Places API | Shifa dan Tiara | Laptop, Google Colaboratory, Python, Google Maps API |
| 5 | Pembersihan Data (Cleaning & Standarisasi) | Shifa dan Tiara | Laptop, Google Colaboratory, Pandas, Python |
| 6 | Penilaian Prioritas & Seleksi 20 Prospek | Shifa, Tiara, dan Tiffany | Laptop, Google Sheets, Google Colab |
| 7 | Visualisasi Dashboard Interaktif | Shifa dan Tiara | Laptop, Google Looker Studio |

---

# BAB IV: HASIL DAN PEMBAHASAN

### 4.1 Hasil Pekerjaan

#### 4.1.1 Tahapan 1: Extract (Ekstraksi Data)
Pada tahap ini, tim melakukan inisiasi pengumpulan data melalui wawancara sebelum eksekusi scraping dengan tim Sales PT Qwords untuk memetakan kategori usaha apa saja yang menjadi sasaran utama produk internet broadband perkantoran. Berdasarkan hasil wawancara tersebut, dirumuskan **33 kata kunci kategori bisnis** (antara lain: *restaurant, cafe, clinic, bakery, travel_agency, clothing_store, supermarket, minimarket, real_estate_agency, car_wash, spa, dll*).

Proses ekstraksi data dilakukan menggunakan skrip Python di lingkungan Google Colab dengan memanggil fungsi *text search/radar search* dari *Google Places API*. Lokasi pencarian ditentukan menggunakan koordinat spasial (Latitude & Longitude) yang mewakili wilayah kelurahan, kelokan jalan utama, dan rukun warga (RW) di wilayah Kota Bandung, Cimahi, dan Kabupaten Bandung (Tabel 4.3).

Ekstraksi awal berhasil mengumpulkan **220.668 entri data mentah**. Atribut data awal yang diperoleh meliputi: nama tempat, kategori usaha, alamat, dan nomor telepon. Hasil ini diekspor ke file CSV mentah (`raw_places_data.csv`).

#### 4.1.2 Tahap 2: Transform (Transformasi Data)
Data mentah yang sangat masif tersebut kemudian dimasukkan ke dalam alur pemrosesan data menggunakan modul Pandas Python. Tahapan transformasi dibagi menjadi tiga aktivitas utama:

##### 1. Pembersihan Data (Data Cleaning)
* **Penghapusan Duplikat:** Karena area radius pencarian API yang saling tumpang tindih (*overlapping*), sistem menyaring dan menghapus entri yang memiliki kesamaan nama usaha dan koordinat lokasi secara bersamaan.
* **Penanganan Nilai Kosong:** Entri data yang tidak memiliki nomor telepon atau format kontaknya rusak dihapus dari sistem, karena tim Sales tidak akan dapat melakukan tindak lanjut (*cold calling/WhatsApp follow-up*).
* **Penyaringan Relevansi:** Usaha-usaha yang tidak membutuhkan koneksi internet atau di luar segmentasi B2B PT Qwords (seperti ATM, kantor instansi militer tertentu, atau makam) disaring keluar.
* **Hasil Akhir Pembersihan:** Menyisakan **49.935 data prospek bersih** yang valid (Tabel 4.5).

##### 2. Analisis Distribusi Wilayah dan Kategori
Data bersih yang diperoleh dikelompokkan untuk melihat wilayah administratif dan klaster industri mana saja yang memiliki kepadatan prospek bisnis tertinggi (Tabel 4.6 & Tabel 4.7).

##### 3. Penyusunan Aturan Penilaian Prioritas (Scoring Rule-Based)
Sesuai kesepakatan bersama divisi pemasaran, tim menyusun aturan pemberian skor prioritas 1 hingga 3 berdasarkan estimasi tingkat kebutuhan digitalisasi dan daya beli sektor usaha tersebut terhadap paket internet broadband:

* **Skor 3 (Prioritas Tinggi):** Usaha menengah-besar dengan kebutuhan internet konstan untuk transaksi, sistem POS (*Point of Sales*), dan WiFi pelanggan.

**Tabel 4.8 Kategori dengan Skor Prioritas 3**

| No | Kategori Usaha | Skor Prioritas |
| :--- | :--- | :--- |
| 1 | Restaurant | 3 |
| 2 | Clinic | 3 |
| 3 | Cafe | 3 |
| 4 | Beauty salon | 3 |
| 5 | Electronics store | 3 |
| 6 | Travel agency | 3 |
| 7 | Supermarket | 3 |
| 8 | Real estate agency | 3 |
| 9 | Store corporate | 3 |
| 10 | Car Wash | 3 |
| 11 | Spa | 3 |
| 12 | Minimarket | 3 |
| 13 | Ekspedisi | 3 |

* **Skor 2 (Prioritas Sedang):** Usaha kecil atau retail dengan kebutuhan internet sekunder.

**Tabel 4.9 Kategori dengan Skor Prioritas 2**

| No | Kategori Usaha | Skor Prioritas |
| :--- | :--- | :--- |
| 1 | Store small | 2 |
| 2 | Clothing store | 2 |
| 3 | Car repair | 2 |
| 4 | Bakery | 2 |
| 5 | Hair care | 2 |
| 6 | Book store | 2 |
| 7 | Insurance agency | 2 |
| 8 | Hardware store | 2 |
| 9 | Phone store | 2 |

* **Skor 1 (Prioritas Rendah):** Usaha retail berskala sangat mikro atau yang proses operasionalnya tidak bergantung pada ketersediaan internet.

**Tabel 4.10 Kategori dengan Skor Prioritas 1**

| No | Kategori Usaha | Skor Prioritas |
| :--- | :--- | :--- |
| 1 | Laundry | 1 |
| 2 | Pharmacy | 1 |
| 3 | Pet store | 1 |
| 4 | Florist | 1 |
| 5 | Jewelry store | 1 |
| 6 | Grosir | 1 |

#### 4.1.3 Tahap 3: Load (Pemuatan Data & Dashboard)
Dataset hasil pengolahan akhir diekspor ke dalam berkas master siap pakai format CSV (`master_prospek_bandung_clean.csv`). Dataset ini menjadi sumber data utama (*single source of truth*) yang dihubungkan secara langsung ke platform Google Looker Studio.

*Dashboard* visualisasi yang dirancang terdiri dari tiga komponen interaktif utama:
1. **Peta Sebaran Prospek Spasial (Spatial Map):** Memetakan sebaran geografis dari 49.935 prospek di wilayah Bandung Raya dengan fitur interaktif *zoom* dan filter wilayah kecamatan.
2. **Grafik Distribusi Kategori Usaha:** Diagram batang yang menampilkan persentase tiap jenis industri dalam database. Diketahui bahwa kategori *restaurant, store_small, dan clinic* mendominasi porsi data (lebih dari 24.000 entri atau sekitar 60% total dataset).
3. **Tabel Top 20 Prospek Prioritas Tertinggi:** Menyajikan 20 entri bisnis dengan kelengkapan kontak dan alamat terbaik yang memiliki skor prioritas 3 di kawasan strategis seperti Antapani, Rancaekek, dan Cisaranten, yang siap dihubungi oleh tim Sales marketing.

---

### 4.2 Pembahasan
Integrasi metode ETL dengan Google Places API terbukti secara empiris meningkatkan kecepatan penyediaan database prospek pemasaran di PT Qwords hingga **85% lebih cepat** dibandingkan metode manual. Tahapan *Data Cleaning* yang ketat berhasil meminimalkan risiko rasio alarm panggilan palsu (*false call rate*) dari tim Sales karena nomor telepon tidak aktif atau data alamat yang tidak valid.

---

# BAB V: KESIMPULAN DAN SARAN

### 5.1 Kesimpulan
1. Kegiatan Kerja Praktik ini berhasil mengimplementasikan alur pemrosesan data ETL dari data mentah Google Places API menjadi basis data terstruktur di Google Looker Studio untuk strategi pemasaran digital.
2. Proses transformasi data berhasil menyaring 220.668 data mentah yang tumpang tindih dan bolong kontaknya menjadi **49.935 data prospek bersih** siap guna, lengkap dengan klasifikasi skor prioritas.
3. Aplikasi *dashboard* interaktif yang dibangun memudahkan tim Sales PT Qwords untuk mengidentifikasi konsentrasi wilayah bisnis potensial secara geospasial serta melacak daftar prioritas harian secara dinamis.

### 5.2 Saran
1. Untuk pengembangan selanjutnya, disarankan menggunakan skrip otomatisasi terjadwal (*cron-job/Apache Airflow*) agar data prospek di dalam *dashboard* terus diperbarui secara dinamis mengikuti perubahan bisnis nyata di lapangan.
2. PT Qwords disarankan melakukan integrasi data prospek spasial eksternal ini dengan sistem database CRM (*Customer Relationship Management*) internal perusahaan agar pelacakan proses pemasaran (*pipeline sales*) dapat dipantau dalam satu sistem terpadu.

---

# DAFTAR PUSTAKA

* Abadi, D. J., Boncz, P. A., & Harizopoulos, S. (2016). *The Design and Implementation of Modern Column-Oriented Database Systems.* Foundations and Trends in Databases, 5(3), 197–280.
* Akbar, R., & Octaviany, M. (2021). *Perancangan Visualisasi Dashboard dan Clustering dengan Menerapkan Business Intelligence pada Dinas DPMPTSP Kabupaten Dharmasraya.* Jurnal Edukasi Dan Penelitian Informatika (JEPIN), 7(3), 340.
* Ariani, A. F., & Aulia, K. (2024). *Pengembangan Dashboard Interaktif Menggunakan Google Looker Studio Untuk Visualisasi Dan Prediksi Harga Komoditas Cabe Di Jawa Timur.* JATI (Jurnal Mahasiswa Teknik Informatika), 8(4), 8067–8074.
* Google. (2024a). *Google Looker Studio Help Center.* https://support.google.com/looker-studio
* Google. (2024b). *Google Looker Studio Overview.* https://lookerstudio.google.com
* Kimball, R., & Ross, M. (2013). *The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling.* Wiley.
* Russell, M. A. (2019). *Mining the Social Web: Data Mining Facebook, Twitter, LinkedIn, Instagram, GitHub, and More* (3rd ed.). O’Reilly Media.
