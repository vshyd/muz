from ..extensions import db
from sqlalchemy import text

class DBService:

    def __init__(self) -> None:
        self.db = db
        self.artist_table = 'Artysta'

    
    def get_all_artists(self) -> dict:
        SQL = text(f"select * from {self.artist_table}")
        res = self.db.session.execute(SQL)
        artists = [row._mapping for row in res]
        return {"artists":artists}
    