# Keterampilan Git Level Menengah

## Alur Kerja Kolaborasi
* `git clone`: Mengunduh salinan repositori dari server remote untuk memulai pekerjaan di proyek.
* `git pull`: Mengambil semua perubahan terbaru dari repositori remote dan secara otomatis menggabungkannya ke _branch_ lokal Anda.
* `git push`: Mengunggah _commit_ lokal Anda ke repositori remote, membagikan perubahan dengan tim.
* **_Pull Request_ / _Merge Request_**: Konsep fundamental untuk mengusulkan perubahan. Di sini Anda akan belajar cara membuat proposal kode dan berpartisipasi dalam _review_ kode tim.

---

## Manajemen _Branch_ Tingkat Lanjut
* `git branch`: Mengelola _branch_ lokal Anda, termasuk membuat _branch_ baru dan menghapus _branch_ yang sudah selesai.
* `git merge`: Menggabungkan perubahan dari satu _branch_ ke _branch_ lain. Ini adalah inti dari kolaborasi.
* **Penyelesaian Konflik Penggabungan (_Merge Conflicts_)**: Keterampilan wajib di level ini. Anda harus tahu cara mengidentifikasi dan menyelesaikan konflik yang muncul ketika Git tidak dapat menggabungkan perubahan secara otomatis.

---

## Manipulasi Riwayat Lokal
* `git reset`: Mengubah posisi `HEAD` dan membatalkan _commit_ lokal, sering digunakan untuk membersihkan riwayat sebelum _push_. Anda harus menguasai mode `--soft`, `--mixed`, dan `--hard`.
* `git restore`: Mengembalikan _file_ ke kondisi sebelumnya, baik dari _staging area_ atau _commit_ terakhir. Perintah ini lebih aman dari `git reset` untuk membatalkan perubahan pada _file_ spesifik.
* `git stash`: Menyimpan perubahan yang belum di-_commit_ untuk sementara waktu, memungkinkan Anda beralih _branch_ tanpa membuat _commit_ setengah jadi.

---

## Membatalkan Perubahan yang Sudah Dibagikan
* `git revert`: Membatalkan _commit_ yang sudah di-_push_ dengan membuat _commit_ baru yang isinya kebalikan dari _commit_ yang dibatalkan. Ini adalah cara yang aman untuk membatalkan perubahan di repositori tim.

---

## Pengelolaan Konfigurasi Proyek
* `.gitignore`: Memastikan _file_ atau folder tertentu (seperti `node_modules/` atau _file_ _cache_) tidak pernah ditambahkan ke repositori, menjaganya tetap rapi dan ringan.
* `git log` dengan opsi: Menggunakan `git log --oneline --graph` dan opsi lainnya untuk meninjau riwayat _commit_ dengan lebih efisien, yang sangat berguna saat menganalisis alur kerja tim.