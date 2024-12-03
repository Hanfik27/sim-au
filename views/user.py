import os
from core.controllers.user import UserController

class UserView:
    @staticmethod
    def menu():
        while True:
            print("\n=== Menu User ===")
            print("1. Lihat user")
            print("2. Cari user")
            print("3. Tambah user")
            print("4. Perbarui user")
            print("5. Hapus user")
            print("0. Back to Admin Menu")

            pilihan = input("Pilih menu: ")
            if pilihan == "1":
                user = UserController.list_user()
                for m in user:
                    print(m)
            elif pilihan == "2":
                ID_USERS = input("Masukkan ID user: ")
                user = UserController.find_user(ID_USERS)
                print(user)
            elif pilihan == "3":
                NAMA = input("Masukkan Nama: ")
                EMAIL = input("Masukkan Email: ")
                PASSWORD = input("Masukkan Password: ")
                ROLE = input("Masukkan Role: ")
                UserController.add_user(NAMA, EMAIL, PASSWORD, ROLE)
            elif pilihan == "4":
                ID_USERS = input("Masukkan ID: ")
                NAMA = input("Masukkan Nama baru: ")
                EMAIL = input("Masukkan Email baru: ")
                PASSWORD = input("Masukkan Password baru: ")
                ROLE = input("Masukkan Role baru: ")
                UserController.update_user(ID_USERS, NAMA, EMAIL, PASSWORD, ROLE)
            elif pilihan == "5":
                ID_USERS = input("Masukkan ID user: ")
                UserController.delete_user(ID_USERS)
            elif pilihan == "0":
                break
            else:
                print("Pilihan tidak valid.")
