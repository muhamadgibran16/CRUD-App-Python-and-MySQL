"""
fetchall()   => untuk mengambil semua data.
fetachmany() => untuk mengambil data dalam jumlah tertentu yang ditentukan.
fetchone()   => untuk mengambil satu data pertama saja.
cursor()     => metode cursor untuk mengeksekusi hasil query
execute()    => perintah untuk mengeksekusi
commit()     => untuk perubahan dalam database
"""

import mysql.connector
import os

# Create connection to database 
db = mysql.connector.connect(
    host     = "localhost",
    user     = "root",
    passwd   = "",
    database = "mahasiswa"
)


# Clear Screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Insert Data into database
def insert_data(db) :
    nama   = input("Masukan nama    : ")
    nim    = input("Masukan NIM     : ")
    kelas  = input("Masukan Kelas   : ")
    jurusan= input("Masukan Jurusan : ")
    values = (nama, nim, kelas, jurusan)
    cursor = db.cursor()
    query  = "INSERT INTO mahasiswa (nama, nim, kelas, jurusan) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, values)
    db.commit()
    print("{} Data Saved Successfully!!!".format(cursor.rowcount))

# show data on database
def show_data(db) :
    cursor  = db.cursor()
    query   = "SELECT * FROM mahasiswa"
    cursor.execute(query)
    record  = cursor.fetchall()
    
    if cursor.rowcount < 1 :
        print("---------------------------------")
        print("Data not found")
        print("---------------------------------")
    else:
        for data in record :
            print("---------------------------------")
            print("Id_mhs  : ", data[0])
            print("Nama    : ", data[1])
            print("NIM     : ", data[2])
            print("Kelas   : ", data[3])
            print("Jurusan : ", data[4])
            print("---------------------------------")


# change or edit data in database
def update_data(db) :
    cursor       = db.cursor()
    show_data(db)
    id_mhs       = input("Pilih id mahasiswa >> ")
    nama         = input("Nama baru    : ")
    nim          = input("NIM baru     : ")
    kelas        = input("Kelas Baru   : ")
    jurusan      = input("Jurusan Baru : ")
    query        = "UPDATE mahasiswa SET nama=%s, nim=%s, kelas=%s, jurusan=%s WHERE id_mhs=%s"
    values       = (nama, nim, kelas, jurusan, id_mhs)
    cursor.execute(query, values)
    db.commit()
    print("{} Data Changed Successfully!!!".format(cursor.rowcount))

# delete data in database
def delete_data(db):
    cursor       = db.cursor()
    show_data(db)
    id_mhs       = input("Pilih id mahasiswa >> ")
    query        = "DELETE FROM mahasiswa WHERE id_mhs=%s"
    values       = (id_mhs,)
    cursor.execute(query, values)
    db.commit()
    print("{} Data Deleted Successfully!!!".format(cursor.rowcount))


def main_menu(db):
    print("\n=================================")
    print("       PROGRAM CRUD PYTHON")
    print("---------------------------------")
    print("1. Tambahkan Data")
    print("2. Tampilkan Data Mahasiswa")
    print("3. Edit Data")
    print("4. Hapus Data")
    print("5. Keluar")
    print("---------------------------------")

    menu = input("Pilih menu >> ")

    clear_screen()

    if menu == "1" :
        insert_data(db)
    elif menu == "2" :
        show_data(db)
    elif menu == "3" :
        update_data(db)
    elif menu == "4" :
        delete_data(db)
    elif menu == "5" :
        exit()
    else:
        print("Please Input Correctly!!!")

# Main Program 
if __name__ == "__main__" :
    while True :
        main_menu(db)

