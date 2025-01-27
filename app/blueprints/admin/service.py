from ...services.db_service import DBService

class AdminService:

    def __init__(self) -> None:
        self.db_service = DBService()

    
    def get_artists(self) -> list:
        return [str(row) for row in self.db_service.get_all_artists()['artists']]


    def get_exponats(self) -> list:
        return [str(row) for row in self.db_service.get_all_exponats()['exponats']]
    

    def get_exbition_rooms(self) -> list:
        return [str(row) for row in self.db_service.get_all_exhibition_rooms()['exhibition_rooms']]
    

    def get_instutions(self) -> list:
        return [str(row) for row in self.db_service.get_all_institutions()['institutions']]
    
