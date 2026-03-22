import sqlite3
from datetime import datetime

class DBManager:
    def __init__(self, database_name: str = 'database.db'):
        self.con = sqlite3.connect('database/' + database_name)
        self.con.execute("PRAGMA foreign_keys = ON;")
        self.cur = self.con.cursor()
        
        self._create_tables()


    def _create_tables(self):
        """creates all tables if they do not exist"""
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS LOGS (
                id_scan INTEGER PRIMARY KEY AUTOINCREMENT,
                start_time TEXT NOT NULL,
                end_time TEXT,
                offers_found INTEGER DEFAULT 0,
                new_offers INTEGER DEFAULT 0,
                price_changes INTEGER DEFAULT 0,
                errors_count INTEGER DEFAULT 0
            )
        """)
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS PROPERTY (
                id_property TEXT PRIMARY KEY,
                name TEXT,
                url TEXT,
                city TEXT,
                district TEXT,
                street TEXT,
                rooms INTEGER,
                size REAL,
                floor INTEGER,
                market TEXT,
                is_active BOOLEAN DEFAULT 1,
                first_scan_id INTEGER,
                last_scan_id INTEGER,
                FOREIGN KEY (first_scan_id) REFERENCES LOGS(id_scan),
                FOREIGN KEY (last_scan_id) REFERENCES LOGS(id_scan)
            )
        """)
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS PRICE_HISTORY (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_property TEXT NOT NULL,
                id_scan INTEGER NOT NULL,
                timestamp TEXT NOT NULL,
                price INTEGER,
                FOREIGN KEY (id_property) REFERENCES PROPERTY(id_property),
                FOREIGN KEY (id_scan) REFERENCES LOGS(id_scan)
            )
        """)
        
        self.con.commit()

    def __del__(self):
        self.con.close()

    def setup_scan(self):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cur.execute("INSERT INTO LOGS (start_time) VALUES (?)", (timestamp,))
        self.current_scan_id = self.cur.lastrowid
        self.con.comit()
        return self.current_scan_id

if __name__ == '__main__':
    db = DBManager()