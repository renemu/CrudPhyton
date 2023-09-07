import sqlite3

# Membuat koneksi ke database (atau membuatnya jika belum ada)
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# Membuat tabel jika belum ada
cursor.execute('''CREATE TABLE IF NOT EXISTS mahasiswa
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nama TEXT,
                   jurusan TEXT)''')
conn.commit()

def tambah_data(nama, jurusan):
    cursor.execute("INSERT INTO mahasiswa (nama, jurusan) VALUES (?, ?)", (nama, jurusan))
    conn.commit()
    print("Data berhasil ditambahkan.")

def tampilkan_data():
    cursor.execute("SELECT * FROM mahasiswa")
    data = cursor.fetchall()
    if len(data) > 0:
        for row in data:
            print(f"ID: {row[0]}, Nama: {row[1]}, Jurusan: {row[2]}")
    else:
        print("Tidak ada data.")

def update_data(id, nama, jurusan):
    cursor.execute("UPDATE mahasiswa SET nama=?, jurusan=? WHERE id=?", (nama, jurusan, id))
    conn.commit()
    print("Data berhasil diupdate.")

def hapus_data(id):
    cursor.execute("DELETE FROM mahasiswa WHERE id=?", (id,))
    conn.commit()
    print("Data berhasil dihapus.")

while True:
    print("\nMenu:")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print("5. Keluar")
    
    pilihan = input("Pilih menu (1/2/3/4/5): ")
    
    if pilihan == '1':
        nama = input("Masukkan nama: ")
        jurusan = input("Masukkan jurusan: ")
        tambah_data(nama, jurusan)
    elif pilihan == '2':
        tampilkan_data()
    elif pilihan == '3':
        id = input("Masukkan ID data yang akan diupdate: ")
        nama = input("Masukkan nama baru: ")
        jurusan = input("Masukkan jurusan baru: ")
        update_data(id, nama, jurusan)
    elif pilihan == '4':
        id = input("Masukkan ID data yang akan dihapus: ")
        hapus_data(id)
    elif pilihan == '5':
        break
    else:
        print("Pilihan tidak valid. Silakan pilih lagi.")
