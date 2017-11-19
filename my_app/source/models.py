import sqlite3
import os.path
sqlite_file = 'BookCatalog.db.sqbpro'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, sqlite_file)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()
