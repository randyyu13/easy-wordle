class User:
    def __init__(self, id, is_guest, guest_id, username, email):
        self.id = id
        self.is_guest = is_guest
        self.guest_id = guest_id
        self.username = username
        self.email = email
