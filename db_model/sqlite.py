import sqlite3

SQLITE_HOST = 'localhost'
SQLITE_CONN = sqlite3.connect('instance/database.db')

def conn_sqlitedb():
    return SQLITE_CONN