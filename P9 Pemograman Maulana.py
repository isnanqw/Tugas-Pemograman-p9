# Program Input Data Mahasiswa dengan Perhitungan Nilai Akhir

# List untuk menyimpan data mahasiswa
data_mahasiswa = []

print("=" * 60)
print("PROGRAM INPUT DATA MAHASISWA")
print("=" * 60)
print()

# Perulangan untuk input data
while True:
    print("-" * 60)
    # Input data mahasiswa
    nama = input("Nama Mahasiswa: ")
    nim = input("NIM: ")

    # Input nilai dengan validasi
    try:
        tugas = float(input("Nilai Tugas (0-100): "))
        uts = float(input("Nilai UTS (0-100): "))
        uas = float(input("Nilai UAS (0-100): "))

        # Hitung nilai akhir
        # Tugas: 30%, UTS: 35%, UAS: 35%
        nilai_akhir = (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

        # Simpan data ke dalam list sebagai dictionary
        mahasiswa = {
            'nama': nama,
            'nim': nim,
            'tugas': tugas,
            'uts': uts,
            'uas': uas,
            'nilai_akhir': nilai_akhir
        }

        data_mahasiswa.append(mahasiswa)
        print(f"\nData berhasil ditambahkan! Nilai Akhir: {nilai_akhir:.2f}")

    except ValueError:
        print("\nError: Masukkan nilai dalam bentuk angka!")
        continue

    # Tanya apakah ingin menambah data lagi
    print()
    tambah = input("Tambah data lagi? (y/t): ").lower()

    if tambah == 't':
        break
    print()

# Tampilkan semua data mahasiswa
print("\n" + "=" * 60)
print("DAFTAR DATA MAHASISWA")
print("=" * 60)

if len(data_mahasiswa) == 0:
    print("Tidak ada data mahasiswa.")
else:
    for i, mhs in enumerate(data_mahasiswa, 1):
        print(f"\nData Mahasiswa ke-{i}:")
        print(f"Nama         : {mhs['nama']}")
        print(f"NIM          : {mhs['nim']}")
        print(f"Nilai Tugas  : {mhs['tugas']:.2f}")
        print(f"Nilai UTS    : {mhs['uts']:.2f}")
        print(f"Nilai UAS    : {mhs['uas']:.2f}")
        print(f"Nilai Akhir  : {mhs['nilai_akhir']:.2f}")
        print("-" * 60)

print("\nProgram selesai. Terima kasih!")