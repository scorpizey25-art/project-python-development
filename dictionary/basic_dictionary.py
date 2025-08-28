kendaraan = {
    "tipe": "Mobil",
    "merk": "Toyota",
    "model": "Corolla",
    "tahun": 2020,
    "warna": "Merah",
    "harga": 250000000,
    "stok": 5,
    "isHapus": True
}

#print(f"Infomasi Data Awal kendaraan :\n {kendaraan}")

# Menampilkan informasi kendaraan
kendaraan["bahan_bakar"] = "Bensin"  # menambah bahan bakar
kendaraan["harga"] = "350000000"  # memperbarui harga
kendaraan["stok"] -= 1  # mengurangi stok karena ada yang terjual
del kendaraan["isHapus"]  # menghapus isHapus

info_key = kendaraan.keys()
info_value = kendaraan.values()
get_info = kendaraan.get("merk")

#print(f"Info Key kendaraan :\n {info_key}")
#print(f"Info Value kendaraan :\n {info_value}")
#print(f"Info Merk kendaraan : {get_info}")
#print(f"Infomasi Data Akhir kendaraan :\n {kendaraan}")

# Soal dictionary
data_nilai = {
    "Andi": 85,
    "Budi": 70,
    "Citra": 92,
    "Doni": 68,
    "Eka": 75
}

# Tugas Anda adalah membuat sebuah program Python untuk:
#   1. Menghitung dan mencetak rata-rata nilai dari seluruh siswa.
#   2. Menemukan dan mencetak nama siswa dengan nilai tertinggi beserta nilainya.
#   3. Menampilkan daftar siswa yang lulus, dengan asumsi nilai kelulusan adalah 75 atau lebih.

print(f"Data Nilai Awal :\n {data_nilai}")

# 1. Menghitung dan mencetak rata-rata nilai dari seluruh siswa
nilai_avg = sum(data_nilai.values()) / len(data_nilai)
nilai_high = max(data_nilai.values())

# 2. Menemukan dan mencetak nama siswa dengan nilai tertinggi beserta nilainya.

nama_siswa_high = ""
nilai_siswa_high = 0

for i in data_nilai:
    if data_nilai[i] == nilai_high:
        nama_siswa_high  = i
        nilai_siswa_high = data_nilai[i]
        break
    
print(f"Rata-Rata Nilai : {nilai_avg}")
print(f"Nilai Tertinggi : {nama_siswa_high, nilai_siswa_high}")
