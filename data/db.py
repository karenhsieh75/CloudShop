import sqlite3

class Database:
    def __init__(self, db_name="cloudshop.db"):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self._init_db()

    def _init_db(self):
        self.cur.executescript(

            """
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY COLLATE NOCASE
            );

            CREATE TABLE IF NOT EXISTS listings (
                listing_id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                price INTEGER NOT NULL,
                category TEXT NOT NULL,
                username TEXT NOT NULL,
                created_at TEXT NOT NULL,
                FOREIGN KEY(username) REFERENCES users(username),
                FOREIGN KEY(category) REFERENCES categories(category)
            );

            CREATE TABLE IF NOT EXISTS categories (
                category TEXT PRIMARY KEY
            );

            -- Create index
            CREATE INDEX IF NOT EXISTS idx_category ON listings(category);

            -- Insert and delete a dummy record to set the sequence
            INSERT INTO listings (listing_id, title, description, price, category, username, created_at) 
            VALUES (100000, 'dummy', 'dummy', 100, 'dummy', 'dummy', 'dummy');

            DELETE FROM listings WHERE listing_id = 100000;
            """

        )
        self.conn.commit()

    def execute(self, query, params=()):
        self.cur.execute(query, params)
        self.conn.commit()
        return self.cur

    def fetchone(self, query, params=()):
        self.cur.execute(query, params)
        return self.cur.fetchone()

    def fetchall(self, query, params=()):
        self.cur.execute(query, params)
        return self.cur.fetchall()
    
    def close(self):
        self.conn.close()