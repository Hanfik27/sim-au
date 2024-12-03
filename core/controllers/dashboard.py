# from views.absensi import AbsensiView
from views.dashboard import DashboardView
from views.dosen import DosenView
# from views.fakultas import FakultasView
# from views.gedung import GedungView
# from views.jadwal import JadwalView
# from views.jurusan import JurusanView
# from views.kelas import KelasView
# from views.lab import LabView
from views.mahasiswa import MahasiswaView
from views.matkul import MatkulView
from views.nilai import NilaiView
from views.user import UserView

class DashboardController:

    @staticmethod
    def show_dashboard(role):
        while True:
            choice = DashboardView.show_menu(role)

            if choice == "0":
                DashboardView.show_logout_message()
                break

            if role == "admin":
                if choice == "1":
                    print("Kelola Data Mata Kuliah (belum diimplementasi).")
                elif choice == "2":
                    DosenView.menu()
                elif choice == "3":
                    print("Kelola Data Mata Kuliah (belum diimplementasi).")
                elif choice == "4":
                    print("Kelola Data Mata Kuliah (belum diimplementasi).")
                elif choice == "5":
                    print("Kelola Data Mata Kuliah (belum diimplementasi).")
                elif choice == "6":
                    print("Kelola Data Mata Kuliah (belum diimplementasi).")
                elif choice == "7":
                    print("Kelola Data Mata Kuliah (belum diimplementasi).")
                elif choice == "8":
                    print("Kelola Data Mata Kuliah (belum diimplementasi).")
                elif choice == "9":
                    MahasiswaView.menu()
                elif choice == "10":
                    MatkulView.menu()
                elif choice == "11":
                    NilaiView.menu()
                elif choice == "12":
                    UserView.menu()
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
