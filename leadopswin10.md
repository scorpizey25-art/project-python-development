scorpizey25-art

Kasus :
saya punya sekenario,
ketika laptop A sudah melakukan perubahan file app.py,
dan laptop B ingin melakukan push model.py,
jadi laptop B harus melakukan pull dulu untuk menyeragamkan 
struktur git, baru bisa melakukan push ?

Solusi :
1. laptop B 
	terminal : git pull origin main
	terminal : git pull --rebase origin main ( rekomendasi : untuk menjaga commit tetap bersih)

Kasus :
git commit --amend --no-edit	: melakukan commit file terakhir tanpa pesan
git push --force-with-lease origin main

git commit biasa		: melakukan commit perubahan baru     