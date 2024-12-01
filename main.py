from core.middleware.auth import AuthController
from core.controllers.dashboard import DashboardController
from models.user import UserModel
from views.base import BaseView

def main():
    UserModel.create_default_admin()

    while True:
        BaseView.clear_screen()
        print("\n=== Sistem Informasi Akademik ===")
        print("1. Login")
        print("2. Register")
        print("0. Keluar")
        choice = input("Pilih menu: ")

        if choice == "1":
            BaseView.clear_screen()
            role = AuthController.login()
            if role:
                DashboardController.show_dashboard(role)
        elif choice == "2":
            AuthController.register()
        elif choice == "0":
            print("Terima kasih telah menggunakan sistem ini.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
