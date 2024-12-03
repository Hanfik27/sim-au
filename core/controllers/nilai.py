from models.nilai import NilaiModel

class NilaiController:
    @staticmethod
    def list_all_nilai():
        """Get all grade data."""
        return NilaiModel.get_all_nilai()

    @staticmethod
    def insert_nilai(ID_MAHASISWA, ID_MATKUL, GRADE, INDEKS):
        """Add new grade with validation."""
        if not ID_MAHASISWA or not ID_MATKUL:
            print("Student ID and Course ID must be filled.")
            return False
        
        valid_grades = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D', 'E']
        if GRADE not in valid_grades:
            print("Invalid grade.")
            return False
        
        try:
            INDEKS = float(INDEKS)
            if INDEKS < 0 or INDEKS > 4.0:
                print("Index must be between 0 and 4.0")
                return False
        except ValueError:
            print("Index must be a number.")
            return False
        
        ID_NILAI = NilaiModel.insert(ID_MAHASISWA, ID_MATKUL, GRADE, INDEKS)
        print(f"Grade for Course {ID_MATKUL} added with ID_NILAI {ID_NILAI}.")
        return True

    @staticmethod
    def update_nilai(ID_NILAI, GRADE=None, INDEKS=None):
        """Update grade by ID_NILAI."""
        NilaiModel.update(ID_NILAI, GRADE, INDEKS)
        print(f"Grade with ID_NILAI {ID_NILAI} updated successfully.")

    @staticmethod
    def delete_nilai(ID_NILAI):
        """Delete grade by ID_NILAI."""
        NilaiModel.delete(ID_NILAI)
        print(f"Grade with ID_NILAI {ID_NILAI} deleted successfully.")

    @staticmethod
    def get_nilai_by_mahasiswa(ID_MAHASISWA):
        """Get grade data for a specific student."""
        return NilaiModel.get_nilai_by_mahasiswa(ID_MAHASISWA)

    @staticmethod
    def get_summary_nilai(ID_MAHASISWA):
        """Get summary of student grades."""
        return NilaiModel.get_summary_nilai(ID_MAHASISWA)