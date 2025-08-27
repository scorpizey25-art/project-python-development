Langkah dasar GIT
A. Jika baru membuat repository di GITHUB :
	- baru memulai project dari 0, gunakan 
		terminal : "git init"
	- buat file baru, misalkan main.py
    - tambahkan ke repository lokal, 
		* gunakan .(menambahkan all file)
			terminal : git add .		
		* mendefinisikan nama file		
			terminal : git add main.py		
	- commit perubahan ke repository lokal
		* terminal : git commit -m "tulis pesan anda"
	- Hubungkan repositori lokal Anda ke remote (GitHub)
		* terminal : git remote add origin https://github.com/scorpizey25-art/project-python-development
	- Jika pertama kali push gunakan ini	
		* terminal : git push -u origin master	

B. Jika repository di GITHUB sudah ada dan project sudah ada :
    - Hubungkan repositori lokal Anda ke remote (GitHub)
		* terminal : git clone https://github.com/scorpizey25-art/project-python-development
	- Git add
	- Git commit -M "pesan"
	- Git push   
   
C. Konfigurasi
	- cek status branch (default master, maka ganti ke main)
		terminal : git status / git branch (lokal) / git branch -a (lokal+github)
	- ubah pada repo lokal menjadi main 
		terminal : git branch -m main
	- jangan lupa push perubahannya ke github
		terminal : git push -u origin main

Pemahaman Penting => git commit VS git commit --amend --no-edit
1.git commit
2.git commit --amend --no-edit