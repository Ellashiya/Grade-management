import sqlite3

SQLITE_HOST = 'localhost'
SQLITE_CONN = sqlite3.connect('database.db')

def conn_sqlite3db():
    return SQLITE_CONN