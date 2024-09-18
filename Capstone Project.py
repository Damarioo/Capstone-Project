from datetime import datetime

# Data Collection: List of Dictionaries
data_pasien = []
data_dokter = [
    {'id': 1, 'nama': 'Dr. Alfyy'},
    {'id': 2, 'nama': 'Dr. Gibranz'},
    {'id': 3, 'nama': 'Dr. Maxwell'}
]

# Fitur Create: Menambahkan data pasien
def create_pasien(nama, umur, penyakit, id_dokter, tanggal_masuk):
    dokter = next((dokter for dokter in data_dokter if dokter['id'] == id_dokter), None)
    if dokter is None:
        print("Dokter dengan ID tersebut tidak ditemukan.")
        return
    
    pasien = {
        'id': len(data_pasien) + 1,  # Assign Unique ID
        'nama': nama,
        'umur': umur,
        'penyakit': penyakit,
        'dokter': dokter,
        'tanggal_masuk': tanggal_masuk
    }
    data_pasien.append(pasien)
    print(f"Data pasien {nama} telah ditambahkan dengan ID {pasien['id']}.")

# Fitur Read: Menampilkan Seluruh Data atau Data Tertentu
def read_pasien(id=None):
    if id is None:
        for pasien in data_pasien:
            print(pasien)
    else:
        for pasien in data_pasien:
            if pasien['id'] == id:
                print(pasien)
                return
        print("Pasien dengan ID tersebut tidak ditemukan.")

# Fitur Update: Memperbarui Data Pasien berdasarkan ID
def update_pasien(id, nama=None, umur=None, penyakit=None, id_dokter=None):
    for pasien in data_pasien:
        if pasien['id'] == id:
            if nama is not None:
                pasien['nama'] = nama
            if umur is not None:
                pasien['umur'] = umur
            if penyakit is not None:
                pasien['penyakit'] = penyakit
            if id_dokter is not None:
                dokter = next((dokter for dokter in data_dokter if dokter['id'] == id_dokter), None)
                if dokter is not None:
                    pasien['dokter'] = dokter
                else:
                    print("Dokter dengan ID tersebut tidak ditemukan.")
                    return
            print(f"Data pasien dengan ID {id} telah diperbarui.")
            return
    print("Pasien dengan ID tersebut tidak ditemukan.")

# Fitur Delete: Menghapus Data Pasien berdasarkan ID dan Menghitung Durasi Rawat
def delete_pasien(id, tanggal_keluar):
    global data_pasien
    pasien = next((pasien for pasien in data_pasien if pasien['id'] == id), None)
    
    if pasien is not None:
        tanggal_masuk = datetime.strptime(pasien['tanggal_masuk'], '%Y-%m-%d')
        tanggal_keluar = datetime.strptime(tanggal_keluar, '%Y-%m-%d')
        durasi_rawat = (tanggal_keluar - tanggal_masuk).days
        
        data_pasien = [pasien for pasien in data_pasien if pasien['id'] != id]
        print(f"Data pasien dengan ID {id} telah dihapus.")
        print(f"Durasi rawat pasien: {durasi_rawat} hari.")
    else:
        print("Pasien dengan ID tersebut tidak ditemukan.")

# Fitur Lainnya: Menampilkan Jumlah Pasien
def jumlah_pasien():
    print(f"Jumlah pasien saat ini: {len(data_pasien)}")

# Menampilkan Daftar Dokter
def tampilkan_dokter():
    print("Daftar Dokter:")
    for dokter in data_dokter:
        print(f"ID: {dokter['id']}, Nama: {dokter['nama']}")

# Menu Utama untuk Interaksi dengan Pengguna
def menu():
    while True:
        print("\nMenu:")
        print("1. Tambah Pasien")
        print("2. Lihat Pasien")
        print("3. Perbarui Pasien")
        print("4. Hapus Pasien")
        print("5. Jumlah Pasien")
        print("6. Keluar")
        
        pilihan = input("Pilih opsi (1-6): ")
        
        if pilihan == '1':
            nama = input("Masukkan nama pasien: ")
            umur = int(input("Masukkan umur pasien: "))
            penyakit = input("Masukkan penyakit pasien: ")
            tampilkan_dokter()
            id_dokter = int(input("Masukkan ID dokter yang menangani pasien: "))
            tanggal_masuk = input("Masukkan tanggal masuk (YYYY-MM-DD): ")
            create_pasien(nama, umur, penyakit, id_dokter, tanggal_masuk)
        
        elif pilihan == '2':
            id_input = input("Masukkan ID pasien untuk melihat (atau tekan Enter untuk semua): ")
            if id_input:
                read_pasien(int(id_input))
            else:
                read_pasien()
        
        elif pilihan == '3':
            id_input = int(input("Masukkan ID pasien yang ingin diperbarui: "))
            nama = input("Masukkan nama baru (tekan Enter jika tidak diubah): ")
            umur = input("Masukkan umur baru (tekan Enter jika tidak diubah): ")
            penyakit = input("Masukkan penyakit baru (tekan Enter jika tidak diubah): ")
            tampilkan_dokter()
            id_dokter = input("Masukkan ID dokter baru (tekan Enter jika tidak diubah): ")
            update_pasien(id_input, nama if nama else None, int(umur) if umur else None, penyakit if penyakit else None, int(id_dokter) if id_dokter else None)
        
        elif pilihan == '4':
            id_input = int(input("Masukkan ID pasien yang ingin dihapus: "))
            tanggal_keluar = input("Masukkan tanggal keluar (YYYY-MM-DD): ")
            delete_pasien(id_input, tanggal_keluar)
        
        elif pilihan == '5':
            jumlah_pasien()
        
        elif pilihan == '6':
            print("Keluar dari program.")
            break
        
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1 hingga 6.")

# Menjalankan Menu Utama
if __name__ == "__main__":
    menu()
