from flask_login import UserMixin
from db_model.sqlite import conn_sqlitedb


class User(UserMixin):
    
    def __init__(self, user_id, user_email):
        self.id = user_id
        self.user_email = user_email
        
    def get_id(self):
        return str(self.id)
    
    
    # 작성 필요
    @staticmethod
    def get(user_id):
        sqlite_db = conn_sqlitedb()
        db_cursor = sqlite_db.cursor()
        sql = 'sql문 작성'
        db_cursor.execute(sql)
        user = db_cursor.fetchone()
        if not user:
            return None
        
        user = User(user_id=user[0], user_email=user[1])
        return user
    
    @staticmethod
    def find(user_email):
        sqlite_db = conn_sqlitedb()
        db_cursor = sqlite_db.cursor()
        sql = 'sql문 작성'
        db_cursor.execute(sql)
        user = db_cursor.fetchone()
        if not user:
            return None
        
        user = User(user_id=user[0], user_email=user[1])
        return user
    
    @staticmethod
    def create(user_email, user_id):
        user = User.find(user_email)
        if user == None:
            sqlite_db = conn_sqlitedb()
            db_cursor = sqlite_db.cursor()
            sql = 'sql문 작성'
            db_cursor.execute(sql)
            sqlite_db.commit()
            return User.find(user_email)
        else:
            return user
        
    @staticmethod
    def delete(user_id):
        sqlite_db = conn_sqlitedb()
        db_cursor = sqlite_db.cursor()
        sql = 'sql문 작성'
        deleted = db_cursor.execute(sql)
        sqlite_db.commit()
        return deleted