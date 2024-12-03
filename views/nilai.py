import os
from core.controllers.nilai import NilaiController

class NilaiView:
    @staticmethod
    def menu():
        while True:
            os.system("cls")
            print("\n=== Manage Grades ===")
            print("1. Add Grade")
            print("2. Update Grade")
            print("3. Delete Grade")
            print("4. View All Grades")
            print("5. View Student Grades")
            print("0. Back")

            choice = input("Select menu: ")
            if choice == "1":
                NilaiView.tambah_nilai()
            elif choice == "2":
                NilaiView.perbarui_nilai()
            elif choice == "3":
                NilaiView.hapus_nilai()
            elif choice == "4":
                NilaiView.lihat_semua_nilai()
            elif choice == "5":
                NilaiView.lihat_nilai_mahasiswa()
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
            input("Press Enter to continue...")

    @staticmethod
    def tambah_nilai():
        try:
            ID_MAHASISWA = input("Enter Student ID: ").strip()
            ID_MATKUL = input("Enter Course ID: ").strip()
            GRADE = input("Enter Grade (A, B+, etc.): ").strip().upper()
            INDEKS = input("Enter Index (4.0, 3.5, etc.): ").strip()
            
            NilaiController.insert_nilai(ID_MAHASISWA, ID_MATKUL, GRADE, INDEKS)
        except Exception as e:
            print(f"An error occurred: {e}")

    @staticmethod
    def perbarui_nilai():
        try:
            ID_NILAI = input("Enter Grade ID: ").strip()
            if not ID_NILAI:
                print("Grade ID cannot be empty.")
                return

            GRADE = input("Enter new Grade (leave blank if no change): ").strip().upper() or None
            INDEKS = input("Enter new Index (leave blank if no change): ").strip()

            if GRADE and GRADE not in ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D', 'E']:
                print("Invalid grade.")
                return

            INDEKS = float(INDEKS) if INDEKS else None
            if INDEKS is not None and (INDEKS < 0 or INDEKS > 4.0):
                print("Index must be between 0 and 4.0")
                return

            NilaiController.update_nilai(ID_NILAI, GRADE, INDEKS)
        except ValueError:
            print("Index must be a number.")
        except Exception as e:
            print(f"An error occurred: {e}")

    @staticmethod
    def hapus_nilai():
        ID_NILAI = input("Enter Grade ID: ")
        NilaiController.delete_nilai(ID_NILAI)

    @staticmethod
    def lihat_semua_nilai():
        nilai = NilaiController.list_all_nilai()
        if not nilai:
            print("No grade data.")
        else:
            for n in nilai:
                print(f"Student ID: {n['ID_MAHASISWA']}")
                for nilai_item in n.get('NILAI', []):
                    print(f"  Grade ID: {nilai_item['ID_NILAI']}, "
                          f"Course ID: {nilai_item['ID_MATA_KULIAH']}, "
                          f"Grade: {nilai_item['GRADE']}, "
                          f"Index: {nilai_item['INDEKS']}")

    @staticmethod
    def lihat_nilai_mahasiswa():
        ID_MAHASISWA = input("Enter Student ID: ")
        data_nilai = NilaiController.get_nilai_by_mahasiswa(ID_MAHASISWA)
        if not data_nilai:
            print(f"No grades found for student with ID {ID_MAHASISWA}.")
        else:
            print(f"Grades for Student with ID {ID_MAHASISWA}:")
            for nilai in data_nilai:
                print(f"Course: {nilai['NAMA_MATA_KULIAH']}, "
                      f"Credits: {nilai['SKS']}, Grade: {nilai['GRADE']}, "
                      f"Index: {nilai['INDEKS']}, Credit*Index: {nilai['KN']}")
            summary = NilaiController.get_summary_nilai(ID_MAHASISWA)
            if summary:
                print(f"\nTotal Credits: {summary['TOTAL_SKS']}, "
                      f"Total Credit*Index: {summary['TOTAL_KN']}, "
                      f"GPA: {summary['IPK']}")