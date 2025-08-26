fullname = "Novan Surya Ardani"
username = "scorpizey"
password = "pwd_scorpizey"
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