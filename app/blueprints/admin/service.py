from ...services.db_service import DBService

class AdminService:

    def __init__(self) -> None:
        self.db_service = DBService()

    
    def get_artists(self):
        return [str(row) for row in self.db_service.get_all_artists()['artists']]

