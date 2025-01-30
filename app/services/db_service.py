from ..extensions import db
from sqlalchemy import text

class DBService:

    def __init__(self) -> None:
        self.db = db
        self.artist_table = 'Artysta'
        self.exponat_table = 'Eksponat'
        self.exhibition_room_table = 'Sala'
        self.institution_table = 'Instytucja'

    
    def get_all_artists(self) -> list:
        SQL = text(f"""
                SELECT
                    id,
                    imie_nazwisko,
                    data_urodzenia, 
                    data_smierci 
                FROM {self.artist_table}
                """)
        res = self.db.session.execute(SQL)
        artists = [row._mapping for row in res]
        return artists
    

    def get_all_exponats(self) -> list:
        SQL = text(f"""
                SELECT
                    id, 
                    tytul, 
                    artysta_id,
                    status_wyp,
                    wysokosc, 
                    szerokosc,
                    waga
                FROM {self.exponat_table}
                """)
        res = self.db.session.execute(SQL)
        exponats = [row._mapping for row in res]
        return exponats
    

    def get_all_exhibition_rooms(self) -> list:
        SQL = text(f"""
                SELECT
                    id, 
                    nazwa_galerii
                FROM {self.exhibition_room_table}
                """)
        res = self.db.session.execute(SQL)
        exhibition_rooms = [row._mapping for row in res]
        return exhibition_rooms
    

    def get_all_institutions(self) -> list:
        SQL = text(f"""
                SELECT
                    id,
                    nazwa,
                    miasto
                FROM {self.institution_table}
                """)
        res = self.db.session.execute(SQL)
        institutions = [row._mapping for row in res]
        return institutions
    

    def assign_exponat_to_gallery(self, query_params:dict):
        SQL = text(f"""
                INSERT INTO Historia (eksponat_id, sala_id, instytucja_id, data_pocz, data_kon)
                VALUES (:eksponat_id, :sala_id, :instytucja_id, :data_pocz, :data_kon)
                """)
        self.db.session.execute(SQL, query_params)
        self.db.session.commit()


    def save_new_artist(self, query_params:dict):
        SQL = text(f"""
                INSERT INTO Artysta (imie_nazwisko, data_urodzenia, data_smierci)
                VALUES (:imie_nazwisko, :data_urodzenia, :data_smierci)
                """)
        self.db.session.execute(SQL, query_params)
        self.db.session.commit()


    def save_new_institution(self, query_params:dict):
        SQL = text(f"""
                INSERT INTO Instytucja (nazwa, miasto)
                VALUES (:nazwa, :miasto)
                """)
        self.db.session.execute(SQL, query_params)
        self.db.session.commit()