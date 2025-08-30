# function lambda untuk tugas kecil dan anonim
# tanpa mendefinisikan nama fungsi
# dan function disimpan pada variabel

# secara aturan flake8
# operasi ini sangat tidak direkomendasikan
# karena mengurangi keterbacaan kode
# lebih baik menggunakan def function
# namun untuk tugas-tugas kecil
# penggunaan lambda function masih diperbolehkan
#   => tambah = lambda a, b: a+b
#   => print(tambah(10, 10))


# function decorator
def decorator_wrapper(fcontaint):    # membuat fungsi decorator
    print("Membuat Pembungkus")

    def create_wrapper():   # membuat fungsi pembungkus
        print("Menambahkan Pita Kuning")
        fcontaint()
        print("Menambahkan Pita Pink")
    return create_wrapper    # mengembalikan fungsi pembungkus

@decorator_wrapper    # menambahkan decorator pada fungsi
def IsiKado():   # fungsi yang akan dibungkus
    print("Ini adalah kado spesial untukmu")


# memanggil fungsi yang sudah dibungkus
IsiKado()   # fungsi yang akan dibungkus
