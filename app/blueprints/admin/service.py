import psycopg2
from ...services.db_service import DBService
import random
import datetime
class AdminService:

    def __init__(self) -> None:
        self.db_service = DBService()

    
    def get_artists(self) -> list:
        raw_artists = self.db_service.get_all_artists()
        return [self.serialize_artist(artist) for artist in raw_artists]
    

    def serialize_artist(self, artist:dict):
        return {
            "id": artist["id"],
            "imie_nazwisko": artist["imie_nazwisko"],
            "data_urodzenia": artist["data_urodzenia"].isoformat() if artist["data_urodzenia"] else None,
            "data_smierci": artist["data_smierci"].isoformat() if artist["data_smierci"] else None
        }
    

    def serialize_exponat(self, exponat:dict):
        return {
            'expid':exponat['expid'],
            'tytul':exponat['tytul'],
            'artysta_id':int(exponat['artysta_id']),
            'status_wyp':str(exponat['status_wyp']),
            'wysokosc':float(exponat['wysokosc']),
            'szerokosc':float(exponat['szerokosc']),
            'waga':float(exponat['waga'])
        }
    
    def serialize_history(self, record:dict):
        return {
            'record_id': record['id'],
            'exhibit':record["exhibit"],
            'gallery':record["gallery"],
            'institution':record["institution"],
            'date_start':self._to_isoformat(record["date_start"]),
            'date_end':self._to_isoformat(record["date_end"]),
            'date_at':self._to_isoformat(record['date_at'])
        }
    
    def _create_history_record(self, record:dict) -> dict:
        res = {'record_id':record['record_id']}
        if record['institution']:
            res['action'] = f"{record['exhibit']} rented to {record['institution']} from {record['date_start']} to {record['date_end']} on {record['date_at']}"
        elif record['gallery']:
            res['action'] = f"{record['exhibit']} moved to {record['gallery']} on {record['date_at']}"
        return res
                

    def get_exponats(self) -> list:
        return [self.serialize_exponat(exponat) for exponat in self.db_service.get_all_exponats()]
    

    def get_exbition_rooms(self) -> list:
        return self.db_service.get_all_exhibition_rooms()
    

    def get_instutions(self) -> list:
        return self.db_service.get_all_institutions()
    

    def get_history(self) -> list:
        data = [self.serialize_history(record) for record in self.db_service.get_history()]
        return [self._create_history_record(record) for record in data]

    def assign_exponat_to_gallery(self, data:dict) -> dict:
        gallery_id = data['gallery_id']
        exponat_id = data['exponat_id']
        
        params = {
            "eksponat_id":exponat_id,
            "sala_id":gallery_id,
            "instytucja_id":None,
            "data_pocz": datetime.datetime.today().strftime('%Y-%m-%d'),
            "data_kon":None
        }

        try:
            self.db_service.add_record_to_history(params)
            message = "Exponat was assigned successfuly"
        except Exception as e:
            message = str(e)
        
        return {'message':message}
    

    def save_new_artist(self, data:dict) -> dict:
        params = {"imie_nazwisko":data['imie_nazwisko'],
                  "data_urodzenia":self._replace_empty_string_with_none(data['data_urodzenia']),
                  "data_smierci":self._replace_empty_string_with_none(data['data_smierci'])
                 }
        
        try:
            self.db_service.save_new_artist(params)
            message = "Artist was added successfuly"
        except Exception as e:
            message = str(e)

        return {'message':message}
    

    def update_artist(self, data:dict) -> dict:
        params = {"id":data["id"],
                  "imie_nazwisko":data['imie_nazwisko'],
                  "data_urodzenia":self._replace_empty_string_with_none(data['data_urodzenia']),
                  "data_smierci":self._replace_empty_string_with_none(data['data_smierci'])
                 }
        
        try:
            self.db_service.update_artist(params)
            message = "Artist was updated successfuly"
        except Exception as e:
            message = str(e)

        return {'message':message}
    

    def save_new_institution(self, data:dict) -> dict:
        params = {"nazwa": data['nazwa'],
                  "miasto": data['miasto']
                 }
        
        try:
            self.db_service.save_new_institution(params)
            message = "Institution was added successfuly"
        except Exception as e:
            message = str(e)

        return {'message':message}
    
    def update_institution(self, data:dict) -> dict:
        params = {"id": data['instid'],
                  "nazwa": data['nazwa'],
                  "miasto": data['miasto']
                 }
        
        try:
            self.db_service.update_institution(params)
            message = "Institution was updated successfuly"
        except Exception as e:
            message = str(e)
            print(message)
        return {'message':message}
    

    def save_new_exponat(self, data:dict) -> dict:
        params = {
            'tytul':data['tytul'],
            'artysta_id':int(data['artysta_id']),
            'status_wyp':False,
            'wysokosc':float(data['wysokosc']),
            'szerokosc':float(data['szerokosc']),
            'waga':float(data['waga'])
        }

        try:
            self.db_service.save_new_exponat(params)
            message = "Exponat was added successfuly"
        except Exception as e:
            message = str(e)

        return {'message':message}
    

    def update_exponat(self, data:dict) -> dict:
        params = {
            'id': data['expid'],
            'tytul':data['tytul'],
            'artysta_id':int(data['artysta_id']),
            'wysokosc':float(data['wysokosc']),
            'szerokosc':float(data['szerokosc']),
            'waga':float(data['waga'])
        }

        try:
            self.db_service.update_exponat(params)
            message = "Exponat was updated successfuly"
        except Exception as e:
            message = str(e)
            print(message)
        return {'message':message}
    

    def save_new_gallery(self, data:dict) -> dict:
        params = {
            'nazwa_galerii':data['nazwa_galerii']
        }

        try:
            self.db_service.save_new_gallery(params)
            message = "Gallery was added successfuly"
        except Exception as e:
            message = str(e)
        return {'message':message}


    def update_gallery(self, data:dict) -> dict:
        params = {
            'id': data['roomid'],
            'nazwa_galerii':data['nazwa_galerii']
        }

        try:
            self.db_service.update_gallery(params)
            message = "Gallery was updated successfuly"
        except Exception as e:
            message = str(e)
        return {'message':message}
    

    def rent_exponat(self, data:dict) -> dict:
        institution_id = data['institution_id']
        exponat_id = data['exponat_id']
        
        params = {
            "eksponat_id":exponat_id,
            "sala_id": None,
            "instytucja_id":institution_id,
            "data_pocz": data['date_start'],
            "data_kon": data['date_end']
        }

        try:
            self.db_service.add_record_to_history(params)
            self.db_service.set_to_non_avaiable_exponat(exponat_id)
            message = "Exhibit was rented successfuly"
        except Exception as e:
            message = "Exhibit cannot be outside of museum for more than 30 days in a year."
        
        return {'message':message}
    

    def get_all_exponats_for_users(self) -> dict:
        return self.db_service.get_all_exponats_for_users()


    def get_assign_exponats(self):
        return self.db_service.get_assign_exponats()
            

    def get_rent_exponats(self) -> dict:
        return self.db_service.get_rent_exponats()

    def _replace_empty_string_with_none(self, value:str):
        return value if value else None
    

    def _to_isoformat(self, value):
        return value.isoformat() if value else ''
        



        

    
