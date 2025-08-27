# Panduan Dasar Git & GitHub

Panduan ini mencakup langkah-langkah dasar untuk memulai dan berkolaborasi menggunakan Git dan GitHub.

---

## 1. Konfigurasi Awal (Sekali Saja)

Lakukan langkah-langkah ini hanya sekali setelah Anda menginstal Git di komputer Anda.

1.  **Buat direktori proyek lokal:**
    ```bash
    mkdir git-project
    ```
2.  **Masuk ke direktori baru:**
    ```bash
    cd git-project
    ```
3.  **Lakukan konfigurasi nama & email Anda:**
    Informasi ini akan terlampir di setiap `commit` yang Anda buat.
    ```bash
    git config --global user.name "Nama Anda"
    git config --global user.email "emailanda@contoh.com"
    ```
    

---

## 2. Alur Kerja Dasar

### A. Memulai Proyek Baru di Komputer Lokal

Gunakan alur ini jika Anda memulai sebuah proyek dari nol di komputer Anda dan ingin mengunggahnya ke GitHub.

1.  **Inisialisasi repositori:**
    ```bash
    git init
    ```
2.  **Buat file baru, lalu tambahkan dan *commit*:**
    ```bash
    # Buat file, misalnya `main.py`
    # Lalu, tambahkan ke staging area
    git add .

    # Commit perubahan
    git commit -m "Initial commit of the project"
    ```
3.  **Hubungkan ke GitHub dan *push*:**
    -   Buat repositori kosong di GitHub terlebih dahulu.
    -   Hubungkan repositori lokal Anda ke remote:
    ```bash
    git remote add origin [https://github.com/scorpizey25-art/project-python-development](https://github.com/scorpizey25-art/project-python-development)
    ```
    -   *Push* untuk pertama kalinya (gunakan `main` jika itu nama *branch* utama Anda):
    ```bash
    git push -u origin main
    ```

---

### B. Berkontribusi pada Proyek yang Sudah Ada di GitHub

Gunakan alur ini jika Anda ingin bekerja pada proyek yang sudah ada.

1.  **Kloning repositori:**
    Ini akan menyalin seluruh proyek dari GitHub ke komputer Anda.
    ```bash
    git clone [https://github.com/scorpizey25-art/project-python-development](https://github.com/scorpizey25-art/project-python-development)
    ```
    

2.  **Masuk ke direktori proyek dan mulai bekerja:**
    ```bash
    cd project-python-development
    
    # ... Buat perubahan atau tambahkan file baru ...
    ```

3.  **Tambah, *commit*, dan *push* perubahan:**
    ```bash
    git add .
    git commit -m "Deskripsi perubahan Anda"
    git push
    ```

---

## 3. Proses Pull dan Konfigurasi Lanjutan

### A. Proses Pull (Menarik Perubahan)

`git pull` digunakan untuk menyinkronkan repositori lokal Anda dengan versi terbaru di GitHub.

1.  **Tujuan `git pull`:**
    -   Menarik kode dari repositori GitHub ke repositori lokal Anda.
    -   Memastikan semua rekan tim bekerja dari versi kode yang sama dan terbaru.
    -   Memaksa Anda untuk menyelesaikan konflik secara manual jika terjadi perubahan pada baris kode yang sama.

2.  **Waktu Pelaksanaan:**
    -   Selalu lakukan `git pull` **sebelum** Anda melakukan `git push` untuk menghindari konflik.
    ```bash
    git pull
    ```
    

### B. Konfigurasi dan Manajemen Branch

* **Cek status repositori dan branch:**
    -   ```bash
        git status
        git branch
        git branch -a
        ```
* **Mengganti nama branch:**
    -   Ganti nama branch lokal Anda dari `master` ke `main` (jika diperlukan).
    ```bash
    git branch -m main
    ```
* ***Push* perubahan nama branch:**
    ```bash
    git push -u origin main
    ```

---

Jika ada pertanyaan lain, jangan ragu untuk bertanya! Semoga panduan ini bermanfaat.