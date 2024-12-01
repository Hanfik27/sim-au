import os
from core.controllers.mahasiswa import MahasiswaController

class MahasiswaView:
    @staticmethod
    def menu():
        while True:
            os.system('cls')
            print("\n=== Menu Mahasiswa ===")
            print("1. Lihat Mahasiswa")
            print("2. Cari Mahasiswa")
            print("3. Tambah Mahasiswa")
            print("4. Perbarui Mahasiswa")
            print("5. Hapus Mahasiswa")
            print("0. Back to Admin Menu")

            pilihan = input("Pilih menu: ")
            if pilihan == "1":
                mahasiswa = MahasiswaController.list_mahasiswa()
                for m in mahasiswa:
                    print(m)
            elif pilihan == "2":
                ID_MAHASISWA = input("Masukkan ID MAHASISWA: ")
                mahasiswa = MahasiswaController.find_mahasiswa(ID_MAHASISWA)
                print(mahasiswa)
            elif pilihan == "3":
                ID_MAHASISWA = input("Masukkan ID MAHASISWA: ")
                NIM = input("Masukkan NIM: ")
                NAMA = input("Masukkan Nama: ")
                EMAIL = input("Masukkan Email: ")
                NAMA_JURUSAN = input("Masukkan Jurusan: ")
                NAMA_FAKULTAS = input("Masukkan Fakultas: ")
                MahasiswaController.add_mahasiswa(ID_MAHASISWA, NIM, NAMA, EMAIL, NAMA_JURUSAN, NAMA_FAKULTAS)
            elif pilihan == "4":
                ID_MAHASISWA = input("Masukkan ID: ")
                NIM = input("NIM: ")
                NAMA = input("Masukkan Nama baru: ")
                EMAIL = input("Masukkan EMAIL baru: ")
                NAMA_JURUSAN = input("Masukkan Jurusan baru: ")
                NAMA_FAKULTAS = input("Masukkan Fakultas baru: ")
                MahasiswaController.update_mahasiswa(ID_MAHASISWA, NIM, NAMA, EMAIL, NAMA_JURUSAN, NAMA_FAKULTAS)
            elif pilihan == "5":
                ID_MAHASISWA = input("Masukkan NIM: ")
                MahasiswaController.delete_mahasiswa(ID_MAHASISWA)
            elif pilihan == "0":
                break
            else:
                print("Pilihan tidak valid.")
