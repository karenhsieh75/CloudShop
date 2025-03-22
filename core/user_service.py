class UserService:
    def __init__(self, db):
        self.db = db


    def register_user(self, username):
        try:
            self.db.execute("INSERT INTO users (username) VALUES (?)", (username,))
            return "Success"
        except Exception:
            return "Error - user already existing"
