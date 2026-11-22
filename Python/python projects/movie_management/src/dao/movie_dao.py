from mysql.connector import Error
from config.db_config import pool
from models.movie import Movie

class MovieDAO:

    @staticmethod
    def save(movie: Movie):
        conn = None
        try:
            with pool.get_connection() as conn:
                with conn.cursor() as cursor:
                    sql = "INSERT INTO movies(title, genre, year) VALUES(%s, %s, %s)"
                    cursor.execute(sql, (movie.title, movie.genre, movie.year))
                    conn.commit()
                    return True
        except Error as e:
            print(e)
            if conn and conn.is_connected():
                conn.rollback()
            return False

    @staticmethod
    def fetch_all():
        try:
            with pool.get_connection() as conn:
                with conn.cursor() as cursor:
                    sql = "SELECT * FROM movies"
                    cursor.execute(sql)
                    rows = cursor.fetchall()
                    for row in rows:
                        id, title, genre, year, *_ = row
                        print(f"{id}: {title} | {genre} | {year}")
                    return rows
        except Error as e:
            print(e)
            return []

    @staticmethod
    def find_by_id(movie_id):
        try:
            with pool.get_connection() as conn:
                with conn.cursor() as cursor:
                    sql = "SELECT * FROM movies WHERE id=%s"
                    cursor.execute(sql, (movie_id,))
                    return cursor.fetchone()
        except Error as e:
            print(e)
            return None

    @staticmethod
    def update(movie: Movie):
        conn = None
        try:
            with pool.get_connection() as conn:
                with conn.cursor() as cursor:
                    sql = "UPDATE movies SET title=%s, genre=%s, year=%s WHERE id=%s"
                    cursor.execute(sql, (movie.title, movie.genre, movie.year, movie.id))
                    conn.commit()
                    return True
        except Error as e:
            print(e)
            if conn and conn.is_connected():
                conn.rollback()
            return False

    @staticmethod
    def delete(movie_id):
        conn = None
        try:
            with pool.get_connection() as conn:
                with conn.cursor() as cursor:
                    sql = "DELETE FROM movies WHERE id=%s"
                    cursor.execute(sql, (movie_id,))
                    conn.commit()
                    return cursor.rowcount > 0
        except Error as e:
            print(e)
            if conn and conn.is_connected():
                conn.rollback()
            return False
