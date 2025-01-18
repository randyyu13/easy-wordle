from api.db.base_dao import BaseDAO
from api.models import User

class UserDAO(BaseDAO):
    def insert_user(self, user: User):
        """
        Inserts a new user into the users table. 
        Assumes the `guest_id`, `username`, or `email` are unique (depending on your database schema).
        """
        query = """
        INSERT INTO usersTbl (isGuest, guestId, username, email)
        VALUES (%s, %s, %s, %s)
        """
        self.execute(query, (user.is_guest, user.guest_id, user.username, user.email))

    def upsert_user(self, user: User):
        """
        Inserts or updates a user. If a conflict occurs (e.g., on `guestId`, `username`, or `email`), it updates the existing record.
        """
        query = """
        INSERT INTO usersTbl (isGuest, guestId, username, email)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (guestId)  -- Assuming guestId is the unique constraint
        DO UPDATE SET
            isGuest = EXCLUDED.isGuest,
            username = EXCLUDED.username,
            email = EXCLUDED.email;
        """
        self.execute(query, (user.is_guest, user.guest_id, user.username, user.email))

    def delete_user_by_guest_id(self, guest_id: str):
        """
        Deletes a user by their guest ID.
        """
        query = "DELETE FROM usersTbl WHERE guestId = %s;"
        self.execute(query, (guest_id,))