# Import modul os untuk membuat direktori jika belum ada
import os
from datetime import datetime

# Buat record datetime current
# Menggunakan f-string dan strftime untuk format yang lebih baik dan konsisten
waktu_registrasi = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

# Menentukan jalur file untuk portabilitas yang lebih baik
file_path = os.path.join('examp', 'data_user.txt')

# Periksa dan buat direktori jika belum ada
if not os.path.exists('examp'):
    os.makedirs('examp')

pilihan = ''
while pilihan != '3':
    print("\n=== Aplikasi Input Data User ===")
    print("1. Daftar Pengguna")
    print("2. Tampilkan Data Pengguna")
    print("3. Cari Data Pengguna")
    print("4. Keluar Aplikasi")

    pilihan = input("Masukkan Pilihan Anda: ")

    # --- Bagian Daftar Pengguna ---
    if pilihan == '1':
        try:
            # Membuka file dalam mode 'a' (append) untuk menambahkan data
            with open(file_path, 'a') as file:
                username = input("Masukkan Username: ")
                password = input("Masukkan Password: ")

                # Validasi input tidak boleh kosong
                if not username.strip() or not password.strip():
                    # Melempar error untuk ditangkap di blok except
                    raise ValueError("Username dan Password " +
                                     "tidak boleh kosong.")

                # Menulis data ke file dengan format yang benar
                file.write(f"Registrasi: {waktu_registrasi}\n")
                file.write(f"Username: {username}\n")
                file.write(f"Password: {password}\n\n")
                print("Data Berhasil Disimpan")

        except ValueError as e:
            # Tangkap error validasi
            print(f"\nKesalahan: {e}")

        except IOError as e:
            # Tangkap error saat menulis ke file
            print(f"\nKesalahan I/O: {e}")

    # --- Bagian Tampilkan Data Pengguna ---
    elif pilihan == '2':
        try:
            # Membuka file dalam mode 'r' (read)
            with open(file_path, 'r') as file:
                data = file.read()
                print("\n=== Data User ===")
                print(data)

        except FileNotFoundError:
            # Tangkap error jika file tidak ditemukan
            print("\nFile data_user.txt tidak ditemukan. " +
                  "Silakan input data user terlebih dahulu.")

        except IOError as e:
            # Tangkap error saat membaca dari file
            print(f"\nKesalahan I/O: {e}")

    elif pilihan == '3':
        try:
            # Membuka file dalam mode 'r' (read)
            with open(file_path, 'r') as file:
                cari_username = input("Masukkan Username yang dicari: ")
                found = False

                print("\n=== Hasil Pencarian ===")
                for line in file:
                    if f"Username: {cari_username}" in line:
                        print(line.strip())
                        found = True
                        # Membaca baris berikutnya untuk menampilkan password
                        # None jika tidak ada baris berikutnya
                        next_line = next(file, None)
                        if next_line and next_line.startswith("Password:"):
                            print(next_line.strip())
                        break

                if not found:
                    print(f"Username '{cari_username}' tidak ditemukan.")

        except FileNotFoundError:
            # Tangkap error jika file tidak ditemukan
            print("\nFile data_user.txt tidak ditemukan. " +
                  "Silakan input data user terlebih dahulu.")

        except IOError as e:
            # Tangkap error saat membaca dari file
            print(f"\nKesalahan I/O: {e}")
    # --- Bagian Keluar Aplikasi ---
    elif pilihan == '4':
        print("\nTerima kasih, program dihentikan.")
        break

    else:
        print("\nPilihan tidak valid. Silakan coba lagi.")
