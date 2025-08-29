# ini adalah kumpulan kode - kode sakti dalam python

# kode sakti 1 => if [target search] in [list]
# contoh penggunaan:
group_buah = ['apel', 'jeruk', 'mangga', 'durian']
cari_buah = 'mangga'

# cari buah mangga dalam (in) group_buah
if cari_buah in group_buah:
    print(f"{cari_buah} ditemukan dalam daftar buah.")
else:
    print(f"{cari_buah} tidak ditemukan dalam daftar buah.")

# kode sakti 2 => split()
# contoh penggunaan:

# memisahkan string berdasarkan spasi ( di php explode())
kalimat = "Saya belajar Python di OpenAI"

# default pemisah adalah spasi, bisa juga diisi karakter lain dalam paramter
kata_kata = kalimat.split()
print(kata_kata)


# list vs tuple
# list adalah kumpulan element yg sifatnya dapat diubah atau dinamis
# tuple adalah kumpulan element yang sifatnya konstant atau tetap
# tuple menggunakan pengurung element ()
# list menggunakan pengurung element []
# tuple agar nilai element bisa dimanipulasi harus dikonversi ke list

# contoh penggunaan
var_tuple = ('apel', 'jeruk', 'mangga')
var_convert_list = list(var_tuple)

# manipulasi setelah dikonversi ke list
# dengan menambahkan pisang
var_convert_list.append('pisang')
print(f"setelah konversi tuple ke list : {var_convert_list}")
