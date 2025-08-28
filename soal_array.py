print(" ================= soal 1 ================= ")
"""
Tugas:
1. Gabungkan kedua list buah di bawah menjadi satu list baru yang bernama
    `buah_gabungan`.
2. Hapus semua duplikat (nama buah yang muncul lebih dari satu kali) dari
    `buah_gabungan`.
3. Urutkan list yang sudah bersih dari duplikat tersebut secara alfabetis.
4. Cetak list yang sudah rapi itu.
"""

buah_a = ['mangga', 'jeruk', 'apel']
buah_b = ['anggur', 'pisang', 'mangga']

# --- RUANG KOSONG UNTUK JAWABAN ANDA ---
buah_gabungan = [*buah_a, *buah_b]
print(f"gabungkan kedua array buah dan buah b {buah_gabungan} ")

# set untuk mengeliminasi nilai list sama
buah_unik_set = set(buah_gabungan)

# kembalikan ke list
buah_unik_list = list(buah_unik_set)

print(f"remove duplicate array {buah_unik_list}")

# urutkan
sort_buah = sorted(buah_unik_list)
print(f"urutkan {sort_buah}")

print(" ================= soal 2 ================= ")

"""
Tugas:
1. Sisipkan angka `4` pada posisi yang benar agar list menjadi terurut.
   Anda harus melakukannya tanpa menggunakan `.sort()` atau `sorted()`.
   Anda harus mencari sendiri di mana posisi yang tepat untuk angka `4`.
2. Cetak list yang sudah terisi angka baru.
"""

angka = [7, 1, 9, 3, 5]

# --- RUANG KOSONG UNTUK JAWABAN ANDA ---
angka_baru = 4
angka_posisi = 0

angka.insert(4, 4)
print(f"masukkan angka 4 diposisi sembarang {angka}")

for i in range(len(angka)-1):
    for j in range(len(angka)-1):
        if angka[j] > angka[j+1]:   # jika angka 7 lebih besar dari 1
            temp_angka = angka[j]   # simpan angka 7 kedalam temp_angka
            angka[j] = angka[j+1]   # ganti angka 7 menjadi 1,
            angka[j+1] = temp_angka  # dan ganti angka 1 menjadi 7

angka_urut = angka
print(f"Hasil Pengurutan Angka {angka_urut}")

print(" ================= soal 3 ================= ")
"""
Tugas:
1. Ganti merek 'Suzuki' dengan 'Wuling'.
2. Ganti merek 'Nissan' dengan 'Mercedes'.
3. Cetak list `mobil` setelah semua perubahan.
"""
# --- RUANG KOSONG UNTUK JAWABAN ANDA ---

mobil = ['Honda', 'Toyota', 'Suzuki', 'Mitsubishi', 'Nissan']

print(f"Isi Array Asli {mobil}")

for i in range(len(mobil)):
    if mobil[i] == 'Suzuki':
        mobil[i] = 'Wuling'
    elif mobil[i] == 'Nissan':
        mobil[i] = 'Mercedes'
print(f"{mobil}")
