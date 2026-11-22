from mysql.connector import Error
from config.db_config import pool
from models.user import User

class UserDAO:

    @staticmethod
    def save(user: User):
        conn = None
        try:
            with pool.get_connection() as conn:
                with conn.cursor() as cursor:
                    sql = "INSERT INTO users(username, password, email, full_name) VALUES(%s, %s, %s, %s)"
                    cursor.execute(sql, (user.username, user.password, user.email, user.full_name))
                    conn.commit()
                    return True
        except Error as e:
            print(e)
            if conn and conn.is_connected():
                conn.rollback()
            return False

    @staticmethod
    def login(username, password):
        try:
            with pool.get_connection() as conn:
                with conn.cursor(dictionary=True) as cursor:
                    sql = "SELECT * FROM users WHERE username=%s AND password=%s"
                    cursor.execute(sql, (username, password))
                    row = cursor.fetchone()
                    return row
        except Error as e:
            print(e)
            return None


