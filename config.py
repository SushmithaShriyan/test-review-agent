DB_PASSWORD = "admin123"

def get_user(id):
    query = "SELECT * FROM users WHERE id = " + id
    return db.execute(query)
