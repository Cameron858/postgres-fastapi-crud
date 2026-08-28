import psycopg2


def creat_connection():
    """"""
    try:
        conn = psycopg2.connect(
            user="postgres", host="localhost", port="5432", password="mysecretpassword"
        )

        return conn
    except Exception as e:
        print(f"Cannot connect: {e}")


def get_conn():
    """"""
    try:
        conn = creat_connection()
        yield conn
    finally:
        conn.close()
