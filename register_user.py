fullname = input("Masukkan Nama kamu :")
username = input("Masukkan Username kamu :")
password = input("Masukkan Password kamu :")
tanggal  = "01-11-1987"

print(fullname)
print(username)
print(password)
print(tanggal)

if password == "pwd_scorpizey":
    if len(password) >= 5:
        print("password match")
    else:
        print("password must containt more 2 length")
else:
    print("password incorrect")