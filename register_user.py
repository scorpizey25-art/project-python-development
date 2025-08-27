import array;
import sys;

fullname = input("Masukkan Nama kamu :")
username = input("Masukkan Username kamu :")
password = input("Masukkan Password kamu :")
tanggal = "01-11-1987"

arr_panjang_password = array.array('i',[1,2,3,4,5]);

#print(fullname)
#print(username)
#print(password)
#print(tanggal)

if fullname is None or fullname == '':
    print("fullname tidak boleh kosong !!!")
    sys.exit()
else:
    username = input("Masukkan Username kamu :")
    password = input("Masukkan Password kamu :")
    tanggal  = "01-11-1987"

if password == "12":
    if len(password) >= arr_panjang_password[4]:
        print("password match")
    else:
        #jika numeric dialam {} pakai => 
        # simbol f"isi string {}", atau 
        # gunakan format({}), atau 
        # gunakan % {}
        print(f"password must containt more {arr_panjang_password[4]} length")
else:
    print("password incorrect")
