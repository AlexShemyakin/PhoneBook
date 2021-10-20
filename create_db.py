import mariadb
import os
import sys
import PyInstaller

class create_db():
    conn = mariadb.connect(
        user = "root",
        host = "127.0.0.1",
        port = 3306
    )
    cur = conn.cursor()

    cur.execute("CREATE DATABASE book;")
    conn.commit()

    conn = mariadb.connect(
        user="root",
        host="127.0.0.1",
        port=3306,
        database='book'
    )
    cur = conn.cursor()
    cur.execute("CREATE TABLE users ("
                "id INT AUTO_INCREMENT, "
                "name VARCHAR (100), "
                "password VARCHAR (100), "
                "date DATE, "
                "remember_me INT, "
                "PRIMARY KEY (id))")
    conn.commit()
    cur.execute("CREATE TABLE contacts ("
                "id INT AUTO_INCREMENT, "
                "name VARCHAR (100), "
                "phone VARCHAR (100), "
                "date DATE, "
                "PRIMARY KEY (id))")
    conn.commit()
    print('Database is created')
    input()

if __name__ == '__main__':
    create_db()


