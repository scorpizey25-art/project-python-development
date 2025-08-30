# KERANGKA BERPIKIR GIT TINGKAT MENENGAH

## 1. Git Restore

### `git restore <file>`

Perintah ini membatalkan perubahan yang belum di-`add` pada **working directory**.

- **working directory**: Menjadi bersih/dipulihkan. Perubahan yang belum di-`add` akan hilang.
- **staging**: Tidak berubah. Status file di staging area tetap sama.
- **commit**: Tidak berubah. Tidak ada commit baru yang dibuat.
  - **create id hash**: Tidak.
- **push**: Tidak. Perintah ini hanya bekerja secara lokal.

---

### `git restore --staged <file>`

Perintah ini memindahkan file dari **staging area** kembali ke **working directory** sebagai "unstaged".

- **working directory**: Kembali ke status "modified". Perubahan yang tadinya di staging area sekarang berada di sini.
- **staging**: Dikosongkan. File di-`unstage`.
- **commit**: Tidak berubah. Tidak ada commit baru yang dibuat.
  - **create id hash**: Tidak.
- **push**: Tidak. Perintah ini hanya bekerja secara lokal.

---

### `git restore --source=<commit_hash> <nama_file>`

Perintah ini menimpa file di **working directory** dengan versi dari commit tertentu.

- **working directory**: Ditimpakan. File akan diganti dengan versi dari hash commit yang ditentukan.
- **staging**: Tidak berubah. Status file di staging area tetap sama.
- **commit**: Tidak berubah. Tidak ada commit baru yang dibuat, hanya mengambil data dari commit lama.
  - **create id hash**: Tidak.
- **push**: Tidak. Perintah ini hanya bekerja secara lokal.