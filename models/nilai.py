import uuid
from core.lib.db import nilai_col

class NilaiModel:
    @staticmethod
    def generate_id_nilai():
        """Generate unique ID_NILAI."""
        return str(uuid.uuid4())

    @staticmethod
    def get_nilai_by_mahasiswa(ID_MAHASISWA):
        """Retrieve grade data for a specific student."""
        print(f"Searching for student ID: {ID_MAHASISWA}")  # Debug print
        
        pipeline = [
            {"$match": {"ID_MAHASISWA": ID_MAHASISWA}},  # Verify this matches exactly
            {"$unwind": "$NILAI"},
            {
                "$lookup": {
                    "from": "mata_kuliah",
                    "localField": "NILAI.ID_MATA_KULIAH",
                    "foreignField": "_id",
                    "as": "MATA_KULIAH_DETAIL"
                }
            },
            {"$unwind": "$MATA_KULIAH_DETAIL"},
            {
                "$project": {
                    "_id": 0,
                    "ID_NILAI": "$NILAI.ID_NILAI",
                    "NAMA_MATA_KULIAH": "$MATA_KULIAH_DETAIL.NAMA",
                    "SKS": "$MATA_KULIAH_DETAIL.SKS",
                    "GRADE": "$NILAI.GRADE",
                    "INDEKS": "$NILAI.INDEKS",
                    "KN": {"$multiply": ["$MATA_KULIAH_DETAIL.SKS", "$NILAI.INDEKS"]}
                }
            }
        ]
        
        # Print all documents to understand the data structure
        all_docs = list(nilai_col.find({"ID_MAHASISWA": ID_MAHASISWA}))
        print("All matching documents:", all_docs)
        
        result = list(nilai_col.aggregate(pipeline))
        print("Pipeline result:", result)
        
        return result

    @staticmethod
    def get_summary_nilai(ID_MAHASISWA):
        """Get summary of student grades."""
        pipeline = [
            {"$match": {"ID_MAHASISWA": ID_MAHASISWA}},
            {"$unwind": "$NILAI"},
            {
                "$lookup": {
                    "from": "mata_kuliah",
                    "localField": "NILAI.ID_MATA_KULIAH",
                    "foreignField": "_id",
                    "as": "MATA_KULIAH_DETAIL"
                }
            },
            {"$unwind": "$MATA_KULIAH_DETAIL"},
            {
                "$group": {
                    "_id": "$ID_MAHASISWA",
                    "TOTAL_SKS": {"$sum": "$MATA_KULIAH_DETAIL.SKS"},
                    "TOTAL_KN": {"$sum": {"$multiply": ["$MATA_KULIAH_DETAIL.SKS", "$NILAI.INDEKS"]}},
                    "IPK": {"$avg": "$NILAI.INDEKS"}
                }
            }
        ]
        result = list(nilai_col.aggregate(pipeline))
        if result:
            summary = result[0]
            summary['IPK'] = round(summary.get('IPK', 0), 2)
            return summary
        return None

    @staticmethod
    def insert(ID_MAHASISWA, ID_MATA_KULIAH, GRADE, INDEKS):
        """Insert new grade for a student."""
        ID_NILAI = NilaiModel.generate_id_nilai()
        nilai_data = {
            "ID_NILAI": ID_NILAI,
            "ID_MATA_KULIAH": ID_MATA_KULIAH,
            "GRADE": GRADE,
            "INDEKS": INDEKS
        }
        nilai_col.update_one(
            {"ID_MAHASISWA": ID_MAHASISWA},
            {"$push": {"NILAI": nilai_data}},
            upsert=True
        )
        return ID_NILAI

    @staticmethod
    def update(ID_NILAI, GRADE=None, INDEKS=None):
        """Update grade by ID_NILAI."""
        update_fields = {}
        if GRADE:
            update_fields["NILAI.$.GRADE"] = GRADE
        if INDEKS is not None:
            update_fields["NILAI.$.INDEKS"] = INDEKS

        nilai_col.update_one(
            {"NILAI.ID_NILAI": ID_NILAI},
            {"$set": update_fields}
        )

    @staticmethod
    def delete(ID_NILAI):
        """Delete grade by ID_NILAI."""
        nilai_col.update_one(
            {"NILAI.ID_NILAI": ID_NILAI},
            {"$pull": {"NILAI": {"ID_NILAI": ID_NILAI}}}
        )

    @staticmethod
    def get_all_nilai():
        """Retrieve all grade data."""
        return list(nilai_col.find())