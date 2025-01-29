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


    def get_exponats(self) -> list:
        return self.db_service.get_all_exponats()
    

    def get_exbition_rooms(self) -> list:
        return self.db_service.get_all_exhibition_rooms()
    

    def get_instutions(self) -> list:
        return self.db_service.get_all_institutions()
    

    def assign_exponat_to_gallery(self, data:dict) -> dict:
        gallery_id = data['gallery_id']
        exponat_id = data['exponat_id']
        
        params = {
            "id": random.randint(0, 100000),
            "eksponat_id":exponat_id,
            "sala_id":gallery_id,
            "instytucja_id":None,
            "data_pocz": datetime.datetime.today().strftime('%Y-%m-%d'),
            "data_kon":None
        }
        message = None
        try:
            self.db_service.assign_exponat_to_gallery(params)
            message = "Exponat was assigned successfuly"
        except Exception as e:
            message = str(e)
            print(message)
        
        return {'message':message}

        

    
