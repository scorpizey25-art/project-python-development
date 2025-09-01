import configparser
import os
import shutil
import zipfile
import subprocess
import datetime
import glob

def process_automation():
    """
    Mengotomatisasi proses berdasarkan konfigurasi dari config.ini.
    """
    config = configparser.ConfigParser()
    
    # Jalur absolut ke file konfigurasi
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(current_dir, 'config.ini')

    # Membaca konfigurasi
    try:
        # Menambahkan raw=True untuk menghindari kesalahan format
        config.read(config_path, encoding='utf-8')
        
        # Mengambil jalur dari [settings_paths]
        paths = config['settings_paths']
        path_winrar = paths['path_winrar']
        pathsource_network = paths['pathsource_network']
        pathsource_device = paths['pathsource_device']
        pathsource_extract = paths['pathsource_extract']
        pathsource_archived = paths['pathsource_archived']

        # Mengambil format dari [settings_format]
        formats = config['settings_format']
        date_format = formats['date_format']
        time_format = formats['time_format']
        
        # Mengambil tanggal dari [settings_dates]
        dates = config['settings_dates']
        date_source_str = dates['date_source']
        date_target_str = dates['date_target']

    except Exception as e:
        print(f"ERROR: Tidak dapat membaca file konfigurasi atau ada bagian yang hilang: {e}")
        return

    print("--- Memulai Proses Otomasi Berkas ---")
    print(f"Jalur Jaringan: {pathsource_network}")
    print(f"Jalur Perangkat: {pathsource_device}")
    print(f"Tanggal Sumber: {date_source_str}")
    print(f"Tanggal Target: {date_target_str}")
    print("-------------------------------------")

    # Langkah 1: Salin file dari jaringan ke folder perangkat lokal
    print("Langkah 1: Menyalin file dari jaringan...")
    try:
        # Mengatur format tanggal untuk pencarian file
        date_source_formatted = datetime.datetime.strptime(date_source_str, date_format).strftime('%Y_%m_%d')
        search_pattern = os.path.join(pathsource_network, '**', f"*{date_source_formatted}.zip")
        
        # Mencari semua file yang cocok dengan pola
        files_to_copy = glob.glob(search_pattern, recursive=True)
        
        if not files_to_copy:
            print("Peringatan: Tidak ada file yang ditemukan di jaringan untuk tanggal tersebut.")
            return

        # Pastikan folder tujuan ada
        os.makedirs(pathsource_device, exist_ok=True)
        
        print(f"Ditemukan {len(files_to_copy)} file untuk disalin:")
        for source_path in files_to_copy:
            file_name = os.path.basename(source_path)
            destination_path = os.path.join(pathsource_device, file_name)
            
            print(f"  - Menyalin '{file_name}'...")
            shutil.copyfile(source_path, destination_path)
        
        print("Semua file berhasil disalin.")

    except Exception as e:
        print(f"ERROR: Gagal menyalin file. Pesan kesalahan: {e}")
        return

    # Langkah 2: Ekstrak file yang disalin menggunakan WinRAR
    print("Langkah 2: Mengekstrak file...")
    try:
        os.makedirs(pathsource_extract, exist_ok=True)
        
        files_to_extract = glob.glob(os.path.join(pathsource_device, '*.zip'))
        
        if not files_to_extract:
            print("Tidak ada file ZIP untuk diekstrak.")
            return
            
        for file_path in files_to_extract:
            print(f"  - Mengekstrak '{os.path.basename(file_path)}'...")
            winrar_cmd = [path_winrar, 'x', '-o+', file_path, pathsource_extract]
            subprocess.run(winrar_cmd, check=True, creationflags=subprocess.CREATE_NO_WINDOW)
            
        print("Semua file berhasil diekstrak.")

    except Exception as e:
        print(f"ERROR: Gagal mengekstrak file dengan WinRAR. Pastikan WinRAR.exe ada di jalur yang benar. Pesan kesalahan: {e}")
        return

    # Langkah 3: Kompres kembali file yang diekstrak
    print("Langkah 3: Mengompres ulang file...")
    try:
        # Contoh: Kompres folder yang diekstrak menjadi file zip baru
        new_zip_name = f"arsip_{datetime.date.today().strftime(date_format)}.zip"
        archived_zip_path = os.path.join(pathsource_archived, new_zip_name)
        
        os.makedirs(pathsource_archived, exist_ok=True)
        
        with zipfile.ZipFile(archived_zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(pathsource_extract):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, pathsource_extract))

        print(f"Berhasil mengompres ke {new_zip_name}")
    except Exception as e:
        print(f"ERROR: Gagal mengompres file. Pesan kesalahan: {e}")
        return
        
    print("--- Proses Otomasi Selesai ---")

if __name__ == "__main__":
    process_automation()
