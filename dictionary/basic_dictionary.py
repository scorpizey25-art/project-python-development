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

print(f"Infomasi Data Awal kendaraan :\n {kendaraan}")

# Menampilkan informasi kendaraan
kendaraan["bahan_bakar"] = "Bensin"  # menambah bahan bakar
kendaraan["harga"] = "350000000"  # memperbarui harga
kendaraan["stok"] -= 1  # mengurangi stok karena ada yang terjual
del kendaraan["isHapus"]  # menghapus isHapus

info_key = kendaraan.keys()
info_value = kendaraan.values()
get_info = kendaraan.get("merk")

print(f"Info Key kendaraan :\n {info_key}")
print(f"Info Value kendaraan :\n {info_value}")
print(f"Info Merk kendaraan : {get_info}")

print(f"Infomasi Data Akhir kendaraan :\n {kendaraan}")
