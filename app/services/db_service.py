from ..extensions import db
from sqlalchemy import text

class DBService:

    def __init__(self) -> None:
        self.db = db
        self.artist_table = 'Artysta'
        self.exponat_table = 'Eksponat'
        self.exhibition_room_table = 'Sala'
        self.institution_table = 'Instytucja'
        self.history_table = 'Historia'

    
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
                    id as expid, 
                    tytul, 
                    artysta_id,
                    status_wyp,
                    wysokosc, 
                    szerokosc,
                    waga
                FROM {self.exponat_table}
                ORDER BY id
                """)
        res = self.db.session.execute(SQL)
        exponats = [row._mapping for row in res]
        return exponats
    

    def get_all_exhibition_rooms(self) -> list:
        SQL = text(f"""
                SELECT
                    id as roomid, 
                    nazwa_galerii
                FROM {self.exhibition_room_table}
                """)
        res = self.db.session.execute(SQL)
        exhibition_rooms = [row._mapping for row in res]
        return exhibition_rooms
    

    def get_all_institutions(self) -> list:
        SQL = text(f"""
                SELECT
                    id as instid,
                    nazwa,
                    miasto
                FROM {self.institution_table}
                """)
        res = self.db.session.execute(SQL)
        institutions = [row._mapping for row in res]
        return institutions
    

    def get_history(self) -> list:
        SQL = text(f"""
                SELECT
                    h.id,
                    e.tytul as exhibit,
                    s.nazwa_galerii as gallery,
                    i.nazwa as institution,
                    h.data_pocz as date_start,
                    h.data_kon as date_end,
                    h.data_wpisu as date_at
                FROM {self.history_table} h
                left join {self.exponat_table} e on e.id = h.eksponat_id
                left join {self.exhibition_room_table} s on s.id = h.sala_id
                left join {self.institution_table} i on i.id = h.instytucja_id
                """)
        res = self.db.session.execute(SQL)
        history = [row._mapping for row in res]
        return history
    

    def add_record_to_history(self, query_params:dict):
        SQL = text(f"""
                INSERT INTO Historia (eksponat_id, sala_id, instytucja_id, data_pocz, data_kon)
                VALUES (:eksponat_id, :sala_id, :instytucja_id, :data_pocz, :data_kon)
                """)
        self.db.session.execute(SQL, query_params)
        self.db.session.commit()

    def set_to_non_avaiable_exponat(self, exp_id):
        SQL = text(f"""
            UPDATE Eksponat
            SET status_wyp = True
            WHERE id = {exp_id}
            """)
        self.db.session.execute(SQL)
        self.db.session.commit()


    def save_new_artist(self, query_params:dict):
        SQL = text(f"""
                INSERT INTO Artysta (imie_nazwisko, data_urodzenia, data_smierci)
                VALUES (:imie_nazwisko, :data_urodzenia, :data_smierci)
                """)
        self.db.session.execute(SQL, query_params)
        self.db.session.commit()


    def update_artist(self, query_params:dict):
        SQL = text("""
            UPDATE Artysta
            SET imie_nazwisko = :imie_nazwisko,
                data_urodzenia = :data_urodzenia,
                data_smierci = :data_smierci
            WHERE id = :id
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

    
    def update_institution(self, query_params:dict):
        SQL = text("""
            UPDATE Instytucja
            SET nazwa = :nazwa,
                miasto = :miasto
            WHERE id = :id
            """)
        self.db.session.execute(SQL, query_params)
        self.db.session.commit()


    def save_new_exponat(self, query_params:dict):
        SQL = text(f"""
                INSERT INTO Eksponat (tytul, artysta_id, status_wyp, wysokosc, szerokosc, waga)
                VALUES (:tytul, :artysta_id, :status_wyp, :wysokosc, :szerokosc, :waga)
                """)
        self.db.session.execute(SQL, query_params)
        self.db.session.commit()

    
    def update_exponat(self, query_params:dict):
        SQL = text("""
            UPDATE Eksponat
            SET tytul = :tytul,
                artysta_id = :artysta_id,
                wysokosc = :wysokosc,
                szerokosc = :szerokosc,
                waga = :waga
            WHERE id = :id
            """)
        self.db.session.execute(SQL, query_params)
        self.db.session.commit()
    

    def save_new_gallery(self, query_params:dict):
        SQL = text(f"""
                INSERT INTO Sala (nazwa_galerii)
                VALUES (:nazwa_galerii)
                """)
        self.db.session.execute(SQL, query_params)
        self.db.session.commit()
    

    def update_gallery(self, query_params:dict):
        SQL = text("""
            UPDATE Sala
            SET nazwa_galerii = :nazwa_galerii
            WHERE id = :id
            """)
        self.db.session.execute(SQL, query_params)
        self.db.session.commit()


    def get_rent_exponats(self):
        SQL = text(f"""
            with artists_exponats as (
                   select a.id, count(e.id) as num from {self.artist_table} a
                   join {self.exponat_table} e on e.artysta_id = a.id
                   where e.status_wyp = False
                   group by a.id
                   having count(e.id) > 1
            )
            select e.id, e.tytul 
            from {self.exponat_table} e
            join artists_exponats a on e.artysta_id = a.id
            """)

        res = self.db.session.execute(SQL)
        exps = [row._mapping for row in res]
        return exps


    
