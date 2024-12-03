from core.middleware.auth import AuthController
from core.controllers.dashboard import DashboardController
from models.auth import AuthModel
from views.base import BaseView

def main():
    AuthModel.create_default_admin()

    while True:
        BaseView.clear_screen()
        print("=== Sistem Informasi Akademik ===")
        print("1. Login")
        print("2. Register")
        print("0. Keluar")
        choice = input("Pilih menu: ")

        if choice == "1":
            BaseView.clear_screen()
            role = AuthController.login()
            if role:
                DashboardController.show_dashboard(role)
            BaseView.pause()
        elif choice == "2":
            BaseView.clear_screen()
            AuthController.register()
            BaseView.pause()

        elif choice == "0":
            print("Terima kasih telah menggunakan sistem ini.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
