import os
from core.controllers.matkul import MatkulController

class MatkulView:
    @staticmethod
    def menu():
        while True:
            print("\n=== Menu Mata Kuliah ===")
            print("1. Lihat Mata Kuliah")
            print("2. Cari Mata Kuliah")
            print("3. Tambah Mata Kuliah")
            print("4. Perbarui Mata Kuliah")
            print("5. Hapus Mata Kuliah")
            print("0. Back to Admin Menu")

            pilihan = input("Pilih menu: ")
            if pilihan == "1":
                Matkul = MatkulController.list_matkul()
                for m in Matkul:
                    print(m)
            elif pilihan == "2":
                ID_MATKUL = input("Masukkan ID Matkul: ")
                Matkul = MatkulController.find_matkul(ID_MATKUL)
                print(Matkul)
            elif pilihan == "3":
                NAMA_MATKUL = input("Masukkan Mata kuliah: ")
                SKS = input("Masukkan SKS: ")
                SEMESTER = input("Masukkan Semester: ")
                MatkulController.add_matkul(NAMA_MATKUL, SKS, SEMESTER)
            elif pilihan == "4":
                ID_MATKUL = input("Masukkan ID: ")
                NAMA_MATKUL = input("Masukkan NAMA_MATKUL baru: ")
                SKS = input("Masukkan SKS baru: ")
                SEMESTER = input("Masukkan Semester baru: ")
                MatkulController.update_matkul(ID_MATKUL, NAMA_MATKUL, SKS, SEMESTER)
            elif pilihan == "5":
                ID_MATKUL = input("Masukkan ID Matkul: ")
                MatkulController.delete_matkul(ID_MATKUL)
            elif pilihan == "0":
                break
            else:
                print("Pilihan tidak valid.")
