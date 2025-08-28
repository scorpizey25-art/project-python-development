print("Pembelajaran Basic Array...")

angka = [1, 2, 4, 5]

print(angka[3])

# jika langsung didefinisikan langsung
angka.sort()
print("urutkan tanpa variabel : ", angka)

# jika ingin menyalin kedalam variabel pakai sorted
sort_angka = sorted(angka)
print("urutkan dengan salinan variabel : ", sort_angka)

insert_angka = inse
angka.insert(len(angka), angka[len(angka)-1]+1)
print(f"insert tanpa variabel : {angka}")
