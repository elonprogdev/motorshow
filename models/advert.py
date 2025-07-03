import sqlite3

class CarAdvert:
    def __init__(self, ad_id, client_id, brand, model, year, mileage, fuel_type, transmission, price, description, photo):
        self.id = ad_id
        self.client_id = client_id
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.fuel_type = fuel_type
        self.transmission = transmission
        self.price = price
        self.description = description
        self.photo = photo  # путь к файлу или имя файла

    def __repr__(self):
        return (f"CarAdvert(id={self.id}, client_id={self.client_id}, brand={self.brand}, model={self.model}, "
                f"year={self.year}, mileage={self.mileage}, fuel_type={self.fuel_type}, "
                f"transmission={self.transmission}, price={self.price}, description={self.description}, photo={self.photo})")

    # @staticmethod
    # def create_table(db_name="cars.db"):
    #     with sqlite3.connect(db_name) as conn:
    #         cursor = conn.cursor()
    #         cursor.execute("""
    #         CREATE TABLE IF NOT EXISTS CarAdverts (
    #             id INTEGER PRIMARY KEY AUTOINCREMENT,
    #             client_id INTEGER NOT NULL,
    #             brand TEXT NOT NULL,
    #             model TEXT NOT NULL,
    #             year INTEGER NOT NULL,
    #             mileage INTEGER NOT NULL,
    #             fuel_type TEXT NOT NULL,
    #             transmission TEXT NOT NULL,
    #             price INTEGER NOT NULL,
    #             description TEXT,
    #             photo TEXT,
    #             FOREIGN KEY (client_id) REFERENCES Clients(id)
    #         )
    #         """)
    #         conn.commit()

    @staticmethod
    def create(data: dict, client_id, db_name="cars.db"):
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO CarAdverts (client_id, brand, model, year, mileage, fuel_type, transmission, price, description, photo)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                client_id,
                data['brand'],
                data['model'],
                data['year'],
                data['mileage'],
                data['fuel_type'],
                data['transmission'],
                data['price'],
                data.get('description', ''),
                data.get('photo')
            ))
            conn.commit()

    @staticmethod
    def get_all_adverts(db_name="cars.db"):
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            rows = cursor.execute("SELECT * FROM CarAdverts").fetchall()
            return [CarAdvert(*row) for row in rows]

    @staticmethod
    def get_adverts_by_client(client_id, db_name="cars.db"):
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            rows = cursor.execute("SELECT * FROM CarAdverts WHERE client_id = ?", (client_id,)).fetchall()
            return [CarAdvert(*row) for row in rows]

    @staticmethod
    def get_advert_by_id(ad_id, db_name="cars.db"):
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            row = cursor.execute("SELECT * FROM CarAdverts WHERE id = ?", (ad_id,)).fetchone()
            return CarAdvert(*row) if row else None

    @staticmethod
    def update_advert(ad_id, data: dict, client_id, db_name="cars.db"):
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT client_id FROM CarAdverts WHERE id = ?", (ad_id,))
            row = cursor.fetchone()
            if not row or row[0] != client_id:
                return False

            cursor.execute("""
                UPDATE CarAdverts SET brand=?, model=?, year=?, mileage=?, fuel_type=?, transmission=?, price=?, description=?, photo=?
                WHERE id=?
            """, (
                data['brand'],
                data['model'],
                data['year'],
                data['mileage'],
                data['fuel_type'],
                data['transmission'],
                data['price'],
                data.get('description', ''),
                data.get('photo'),
                ad_id
            ))
            conn.commit()
            return True

    @staticmethod
    def delete_advert(ad_id, client_id, db_name="cars.db"):
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT client_id FROM CarAdverts WHERE id = ?", (ad_id,))
            row = cursor.fetchone()
            if not row or row[0] != client_id:
                return False

            cursor.execute("DELETE FROM CarAdverts WHERE id = ?", (ad_id,))
            conn.commit()
            return True
