import psycopg2

from support.config import bd_user, bd_password, bd_database



PASS=bd_password
USER=bd_user
DBNAME=bd_database
HOST='127.0.0.1'


def connect():
    conn = psycopg2.connect(host = HOST,
                            dbname = DBNAME,
                            user = USER,
                            password = PASS,
                            port = 5432)
    cursor = conn.cursor()
    return conn, cursor




def close(conn, cursor):
    conn.commit()
    cursor.close()
    conn.close()
