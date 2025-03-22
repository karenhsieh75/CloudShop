from datetime import datetime

class ListingService:
    def __init__(self, db):
        self.db = db


    def create_listing(self, username, title, description, price, category):
        user_exists = self.db.fetchone("SELECT username FROM users WHERE username = ?", (username,))
        if not user_exists:
            return "Error - unknown user"
        
        category_exists = self.db.fetchone("SELECT category FROM categories WHERE category = ?", (category,))
        if not category_exists:
            self.db.execute("INSERT INTO categories (category) VALUES (?)", (category,))
        
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.db.execute(
            """
            INSERT INTO listings (title, description, price, category, username, created_at)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (title, description, price, category, username, created_at)
        )

        listing_id = self.db.fetchone("SELECT last_insert_rowid()")
        return str(listing_id[0])
    

    def delete_listing(self, username, listing_id):
        listing = self.db.fetchone("SELECT username, category FROM listings WHERE listing_id = ?", (listing_id,))
        if not listing:
            return "Error - listing does not exist"
        if listing[0] != username:
            return "Error - listing owner mismatch"
        
        self.db.execute("DELETE FROM listings WHERE listing_id = ?", (listing_id,))
        return "Success"
    
    
    def get_listing(self, username, listing_id):
        user_exists = self.db.fetchone("SELECT username FROM users WHERE username = ?", (username,))
        if not user_exists:
            return "Error - unknown user"
        
        listing = self.db.fetchone(
            """
            SELECT title, description, price, created_at, category, username
            FROM listings WHERE listing_id = ?
            """, (listing_id,)
        )

        if not listing:
            return "Error - not found"
        return "|".join(map(str, listing))