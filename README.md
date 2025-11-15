# Tugas-Pemograman-p9
Program Input Data Mahasiswa
Deskripsi
Program sederhana untuk menginput data mahasiswa beserta nilai-nilainya dan menghitung nilai akhir berdasarkan komponen:

Tugas: 30%
UTS: 35%
UAS: 35%

Flowchart Program
mermaidflowchart TD

    A([START]) --> B[Inisialisasi list data_mahasiswa]
    
    B --> C[Tampilkan header program]
    
    C --> D[Input Nama Mahasiswa]
    
    D --> E[Input NIM]
    
    E --> F[Input Nilai Tugas]
    
    F --> G[Input Nilai UTS]
    
    G --> H[Input Nilai UAS]
    
    H --> I{Validasi Input Nilai}
    
    I -->|Error| J[Tampilkan pesan error]
    
    J --> F
    
    I -->|Valid| K[Hitung Nilai Akhir<br/>NA = Tugas*0.3 + UTS*0.35 + UAS*0.35]
    
    K --> L[Simpan data ke list]
    
    L --> M[Tampilkan konfirmasi]
    
    M --> N{Tambah data lagi?<br/>y/t?}
    
    N -->|y - Ya| D
    
    N -->|t - Tidak| O[Tampilkan header daftar]
    
    O --> P{Apakah list kosong?}
    
    P -->|Ya| Q[Tampilkan: Tidak ada data]
    
    P -->|Tidak| R[Loop untuk setiap mahasiswa]
    
    R --> S[Tampilkan data mahasiswa]
    
    S --> T{Masih ada data?}
    
    T -->|Ya| R
    
    T -->|Tidak| U[Tampilkan pesan selesai]
    
    Q --> U
    
    U --> V([END])
    
Penjelasan Program
1. Struktur Data
Program menggunakan list sebagai wadah utama untuk menyimpan data mahasiswa. Setiap mahasiswa disimpan dalam bentuk dictionary dengan key:

nama: Nama mahasiswa
nim: Nomor Induk Mahasiswa
tugas: Nilai tugas
uts: Nilai UTS
uas: Nilai UAS
nilai_akhir: Hasil perhitungan nilai akhir

2. Alur Program
A. Inisialisasi
pythondata_mahasiswa = []
Membuat list kosong untuk menampung data mahasiswa.
B. Input Data (Perulangan)
Program menggunakan while True untuk perulangan tanpa batas hingga user memilih untuk berhenti.
Proses input:

Input nama dan NIM mahasiswa
Input nilai tugas, UTS, dan UAS (dengan validasi)
Jika input tidak valid (bukan angka), program menampilkan error dan meminta input ulang
Jika valid, hitung nilai akhir

C. Perhitungan Nilai Akhir
pythonnilai_akhir = (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)
Formula perhitungan:

Tugas berkontribusi 30%
UTS berkontribusi 35%
UAS berkontribusi 35%

D. Penyimpanan Data
Data mahasiswa disimpan dalam bentuk dictionary kemudian ditambahkan ke list menggunakan append().
E. Konfirmasi Penambahan Data
pythontambah = input("Tambah data lagi? (y/t): ").lower()
if tambah == 't':
    break
Program menanyakan apakah user ingin menambah data lagi:

y (Ya): Kembali ke input data
t (Tidak): Keluar dari perulangan dan menampilkan data

F. Menampilkan Data
Program melakukan pengecekan:

Jika list kosong: tampilkan "Tidak ada data mahasiswa"
Jika ada data: tampilkan semua data menggunakan perulangan for dengan enumerate() untuk penomoran otomatis

3. Fitur Program
✅ Input data unlimited - User dapat menambahkan data sebanyak-banyaknya
✅ Validasi input - Program memeriksa apakah nilai yang diinput adalah angka
✅ Perhitungan otomatis - Nilai akhir dihitung secara otomatis
✅ Tampilan terstruktur - Data ditampilkan dengan format yang rapi dan mudah dibaca
✅ Error handling - Program tidak crash saat input salah
4. Contoh Output
============================================================
PROGRAM INPUT DATA MAHASISWA
============================================================

------------------------------------------------------------
Nama Mahasiswa: Budi Santoso
NIM: 2024001
Nilai Tugas (0-100): 85
Nilai UTS (0-100): 90
Nilai UAS (0-100): 88

Data berhasil ditambahkan! Nilai Akhir: 87.75

Tambah data lagi? (y/t): t

============================================================
DAFTAR DATA MAHASISWA
============================================================

Data Mahasiswa ke-1:
Nama         : Budi Santoso
NIM          : 2024001
Nilai Tugas  : 85.00
Nilai UTS    : 90.00
Nilai UAS    : 88.00
Nilai Akhir  : 87.75
------------------------------------------------------------

Program selesai. Terima kasih!
Cara Menjalankan Program

Pastikan Python sudah terinstall (Python 3.x)
Clone repository ini
Jalankan program:

bash   python program_mahasiswa.py

Ikuti instruksi yang muncul di layar

Teknologi yang Digunakan

Python 3.x
Built-in functions: input(), print(), append(), enumerate()
Data structures: List dan Dictionary
Exception handling: try-except

Pengembangan Lebih Lanjut
Beberapa fitur yang bisa ditambahkan:

 Menyimpan data ke file (CSV/JSON)
 Fitur edit dan hapus data
 Fitur pencarian data
 Konversi nilai akhir ke huruf mutu (A, B, C, D, E)
 Statistik nilai (rata-rata, tertinggi, terendah)
 Export data ke Excel
