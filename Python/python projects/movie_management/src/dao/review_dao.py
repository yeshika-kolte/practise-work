from mysql.connector import Error
from config.db_config import pool
from models.review import Review

class ReviewDAO:

    @staticmethod
    def save(review: Review):
        conn = None
        try:
            with pool.get_connection() as conn:
                with conn.cursor() as cursor:
                    sql = "INSERT INTO reviews(user_id, movie_id, rating, comment) VALUES(%s, %s, %s, %s)"
                    cursor.execute(sql, (review.user_id, review.movie_id, review.rating, review.comment))
                    conn.commit()
                    return True
        except Error as e:
            print(e)
            if conn and conn.is_connected():
                conn.rollback()
            return False

    @staticmethod
    def fetch_all_with_join():
        try:
            with pool.get_connection() as conn:
                with conn.cursor(dictionary=True) as cursor:
                    sql = """
                        SELECT r.id, u.username, m.title, r.rating, r.comment
                        FROM reviews r
                        JOIN users u ON r.user_id = u.id
                        JOIN movies m ON r.movie_id = m.id
                    """
                    cursor.execute(sql)
                    rows = cursor.fetchall()
                    for row in rows:
                        print(f"ReviewID: {row['id']} | User: {row['username']} | Movie: {row['title']} | Rating: {row['rating']} | Comment: {row['comment']}")
                    return rows
        except Error as e:
            print(e)
            return []
