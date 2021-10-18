import mariadb

conn = mariadb.connect(
        user = "root",
        host = "127.0.0.1",
        port = 3306,
        database = "book"
    )
cur = conn.cursor()

def reg_user(name, password, date):
    cur.execute("INSERT INTO users (name, password, date) VALUES (?, ?, ?)", (name, password, date))
    conn.commit()


def add_data(name, phone, date):
    cur.execute("INSERT INTO contacts (name, phone, date) VALUES (?, ?, ?)", (name, phone, date))
    conn.commit()



