import os
from core.controllers.dosen import DosenController

class DosenView:
    @staticmethod
    def menu():
        while True:
            print("\n=== Menu Dosen ===")
            print("1. Lihat Dosen")
            print("2. Cari Dosen")
            print("3. Tambah Dosen")
            print("4. Perbarui Dosen")
            print("5. Hapus Dosen")
            print("0. Back to Admin Menu")

            pilihan = input("Pilih menu: ")
            if pilihan == "1":
                Dosen = DosenController.list_dosen()
                for m in Dosen:
                    print(m)
            elif pilihan == "2":
                ID_DOSEN = input("Masukkan ID Dosen: ")
                Dosen = DosenController.find_dosen(ID_DOSEN)
                print(Dosen)
            elif pilihan == "3":
                NAMA = input("Masukkan Nama: ")
                NIP = input("Masukkan NIP: ")
                EMAIL = input("Masukkan Email: ")
                DEPARTEMEN = input("Masukkan Departemen: ")
                DosenController.add_dosen(NIP, NAMA, EMAIL, DEPARTEMEN)
            elif pilihan == "4":
                ID_DOSEN = input("Masukkan ID: ")
                NIP = input("NIP: ")
                NAMA = input("Masukkan Nama baru: ")
                EMAIL = input("Masukkan EMAIL baru: ")
                DEPARTEMEN = input("Masukkan Departemen baru: ")
                DosenController.update_dosen(ID_DOSEN, NIP, NAMA, EMAIL, DEPARTEMEN)
            elif pilihan == "5":
                ID_DOSEN = input("Masukkan NIP: ")
                DosenController.delete_dosen(ID_DOSEN)
            elif pilihan == "0":
                break
            else:
                print("Pilihan tidak valid.")
