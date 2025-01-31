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
            'id':exponat['id'],
            'tytul':exponat['tytul'],
            'artysta_id':int(exponat['artysta_id']),
            'status_wyp':str(exponat['status_wyp']),
            'wysokosc':float(exponat['wysokosc']),
            'szerokosc':float(exponat['szerokosc']),
            'waga':float(exponat['waga'])
        }
    

    def get_exponats(self) -> list:
        return [self.serialize_exponat(exponat) for exponat in self.db_service.get_all_exponats()]
    

    def get_exbition_rooms(self) -> list:
        return self.db_service.get_all_exhibition_rooms()
    

    def get_instutions(self) -> list:
        return self.db_service.get_all_institutions()
    

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
            self.db_service.assign_exponat_to_gallery(params)
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
            'id': data['id'],
            'tytul':data['tytul'],
            'artysta_id':int(data['artysta_id']),
            'status_wyp':False,
            'wysokosc':float(data['wysokosc']),
            'szerokosc':float(data['szerokosc']),
            'waga':float(data['waga'])
        }

        try:
            self.db_service.update_exponat(params)
            message = "Exponat was updated successfuly"
        except Exception as e:
            message = str(e)
        return {'message':message}


    
    def _replace_empty_string_with_none(self, value:str):
        return value if value else None
        



        

    
