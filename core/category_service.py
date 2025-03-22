class CategoryService:
    def __init__(self, db):
        self.db = db


    def get_category(self, username, category):
        user_exists = self.db.fetchone("SELECT username FROM users WHERE username = ?", (username,))
        if not user_exists:
            return "Error - unknown user"
        
        category_exists = self.db.fetchone("SELECT count FROM categories WHERE category = ?", (category,))
        if not category_exists:
            return "Error - category not found"
        
        listings = self.db.fetchall(
            """
            SELECT title, description, price, created_at FROM listings
            WHERE category = ? ORDER BY created_at DESC
            """,
            (category,)
        )

        return "\n".join("|".join(map(str, listing)) for listing in listings)
    

    def get_top_category(self, username):

        user_exists = self.db.fetchone("SELECT username FROM users WHERE username = ?", (username,))
        if not user_exists:
            return "Error - unknown user"

        self.db.execute(

            """
            SELECT category
            FROM listings
            GROUP BY category
            HAVING COUNT(*) = (
                SELECT MAX(category_count)
                FROM (
                    SELECT COUNT(*) AS category_count
                    FROM listings
                    GROUP BY category
                )
            )
            ORDER BY category ASC
            """

        )

        categories = self.db.fetchall()
        if not categories:
            return "Error - no listings found"
        
        # 返回所有最多 listing 的分類，按字母排序
        return " ".join(category[0] for category in categories)