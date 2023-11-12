from flask_login import UserMixin
from db_model.sqlite import conn_sqlite3db


class User(UserMixin):
    
    def __init__(self, user_id) -> None:
        self.id = user_id
        
    def get_id(self):
        return str(self.id)
    
    
    # 작성 필요
    @staticmethod
    def get(user_id):
        sqlite3_db = conn_sqlite3db()
        sql = 'sql문 작성'
        pass