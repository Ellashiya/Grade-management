from flask_login import UserMixin
from db_model.sqlite import conn_sqlitedb


class User(UserMixin):
    
    def __init__(self, user_id):
        self.id = user_id
        
    def get_id(self):
        return str(self.id)
    
    
    # 작성 필요
    @staticmethod
    def get(user_id):
        sqlite3_db = conn_sqlitedb()
        db_cursor = sqlite3_db.cursor()
        sql = 'sql문 작성'
        db_cursor.execute(sql)
        user = db_cursor.fetchone()
        if not user:
            return None
        
        user = User(user_id=user[0])
        return user
    
    @staticmethod
    def find(user_id):
        sqlite3_db = conn_sqlitedb()
        db_cursor = sqlite3_db.cursor()
        sql = 'sql문 작성'
        db_cursor.execute(sql)
        user = db_cursor.fetchone()
        if not user:
            return None
        
        user = User(user_id=user[0])
        return user
    
    @staticmethod
    def create(user_id):
        sqlite3_db = conn_sqlitedb()
        db_cursor = sqlite3_db.cursor()
        sql = 'sql문 작성'
        db_cursor.execute(sql)
        user = db_cursor.fetchone()
        if not user:
            return None
        
        user = User(user_id=user[0])
        return user
    
    @staticmethod
    def delete(user_id):
        sqlite3_db = conn_sqlitedb()
        db_cursor = sqlite3_db.cursor()
        sql = 'sql문 작성'
        db_cursor.execute(sql)
        user = db_cursor.fetchone()
        if not user:
            return None
        
        user = User(user_id=user[0])
        return user