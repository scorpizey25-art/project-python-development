# function dengan inisialisasi nilai parameter
def beginner_function(username, gender="women"):
    print(f"username : {username}\ngender : {gender}")


# parameter kedua jika kosong, maka otomatis
# akan mengisi women
# beginner_function("Ratih")


# function args(*) dan kwargs(*)
#   - dapat digunakan untuk mengisi parameter tak terbatas
#   - menggunakan list / dictionary ( array )
# args(*) penggunaan func(*args)
#   - tupple/list : sama penggunaan pada array tunggal
# kwargs(**) penggunaan func(**kwargs)
#   - dictionary : sama penggunaan pada array assosoatif
#     key dan value (pair)

# menggunakan list/tuple
def beginner_function_A(*pesanan):
    print(f"Pesanan anda adalah : {pesanan}")


param_single = 'sate', 'bakso', 'nasi lemak'
beginner_function_A(*param_single)


# menggunakan dictionary
def beginner_function_B(**pesanan):
    print(f"Pesanan detail anda {pesanan}")


param_pair = {
    'name': 'Novan',
    'ages': 38,
    'email': 'scorpizey25@gmail.com'
}
beginner_function_B(**param_pair)
