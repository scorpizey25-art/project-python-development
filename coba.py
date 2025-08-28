try:
    # Membuka file dalam mode 'r' (read)
    with open('examp/data_user.txt', 'r') as file:
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
