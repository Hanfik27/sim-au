from views.dashboard import DashboardView
from views.mahasiswa import MahasiswaView

class DashboardController:
    """Class untuk mengontrol navigasi di dashboard berdasarkan role."""

    @staticmethod
    def show_dashboard(role):
        while True:
            # Tampilkan menu dashboard dan dapatkan pilihan
            choice = DashboardView.show_menu(role)

            # Jika pengguna memilih logout
            if choice == "0":
                DashboardView.show_logout_message()
                break

            # Tindakan berdasarkan peran dan pilihan
            if role == "admin":
                if choice == "1":
                    MahasiswaView.menu()
                elif choice == "2":
                    print("Kelola Data Dosen (belum diimplementasi).")
                elif choice == "3":
                    print("Kelola Data Mata Kuliah (belum diimplementasi).")
                else:
                    print("Pilihan tidak valid.")
            elif role == "mahasiswa":
                if choice == "1":
                    print("Lihat Jadwal Kuliah (belum diimplementasi).")
                elif choice == "2":
                    print("Lihat Nilai (belum diimplementasi).")
                else:
                    print("Pilihan tidak valid.")
            elif role == "dosen":
                if choice == "1":
                    print("Lihat Jadwal Mengajar (belum diimplementasi).")
                elif choice == "2":
                    print("Input Nilai (belum diimplementasi).")
                else:
                    print("Pilihan tidak valid.")
            else:
                print("Role tidak dikenali.")
                break
