from views.base import show_header, show_menu
from views.mahasiswa import MahasiswaView

class DashboardView:
    """Class untuk menampilkan dan mengelola menu dashboard."""

    @staticmethod
    def show_menu(role):
        """Menampilkan menu dashboard berdasarkan peran."""
        if role == "mahasiswa":
            print("\n=== Dashboard Mahasiswa ===")
            print("1. Lihat Jadwal Kuliah")
            print("2. Lihat Nilai")
            print("0. Logout")
        elif role == "dosen":
            print("\n=== Dashboard Dosen ===")
            print("1. Lihat Jadwal Mengajar")
            print("2. Input Nilai")
            print("3. Input Absensi")
            print("0. Logout")
        elif role == "admin":
            print("\n=== Dashboard Admin ===")
            print("1. Kelola Data Mahasiswa")
            print("2. Kelola Data Dosen")
            print("3. Kelola Data Mata Kuliah")
            print("4. Kelola Data Fakultas")
            print("5. Kelola Data Jurusan")
            print("6. Kelola Data ")
            print("7. ")
            print("8. ")
            print("9. ")
            print("10. ")
            print("11. ")
            print("12. ")
            print("0. Logout")
        else:
            print("Role tidak dikenali.")
            return "0"

        # Input pilihan pengguna
        pilihan = input("Pilih menu: ")
        return pilihan

    @staticmethod
    def show_logout_message():
        """Menampilkan pesan logout."""
        print("Logout berhasil.")
