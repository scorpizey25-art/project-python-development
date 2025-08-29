# bagian pertama => buat function
def basic_function():
    print("Dasar function bagian Pertama")


# bagian pertama => panggil function
basic_function()


# bagian kedua => buat function dengan parameter
def basic_function(username):
    print(f"Cetak username anda menjadi : {username}")


# bagian kedua => panggil function
basic_function("Scorpizey25")


# bagian ketiga => buat function dengan pengembalian nilai
def basic_function_ret():
    price = 20000
    return price


# bagian ketiga => panggil function
print(basic_function_ret())
