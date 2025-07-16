import sqlite3


class Review:
    @staticmethod
    def get_reviews_about(client_id, db_name="cars.db"):
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT r.text, c.e_mail
                FROM Reviews r
                JOIN Clients c ON r.author_id = c.id
                WHERE r.reviewed_id = ?
            """, (client_id,))
            return [{'text': row[0], 'author_email': row[1]} for row in cursor.fetchall()]

    @staticmethod
    def add_review(author_id, reviewed_id, text, db_name="cars.db"):
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Reviews (author_id, reviewed_id, text)
                VALUES (?, ?, ?)
            """, (author_id, reviewed_id, text))
            conn.commit()
