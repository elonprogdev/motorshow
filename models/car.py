import sqlite3


class Car:
    def __init__(self, car_id, brand, model, year, mileage, engine_fuel, engine_volume, transmission, color,
                  price, description, photo, client_id):
        self.id = car_id
        self.brand = brand
        self.model = model        
        self.year = year
        self.mileage = mileage
        self.engine_fuel = engine_fuel
        self.engine_volume = engine_volume
        self.transmission = transmission
        self.color = color
        self.price = price        
        self.description = description
        self.photo = photo # путь к файлу или имя файла
        self.client_id = client_id

     

    def __repr__(self):
        return (f"id: {self.id}, model: {self.model}, volume: {self.volume}, price: {self.price}, "
                f"year: {self.year}, mileage: {self.mileage}, brand: {self.brand}, fuel_type: {self.fuel_type}, "
                f"transmission: {self.transmission}, description: {self.description}, photo: {self.photo}, "
                f"client_id: {self.client_id}")

    # @staticmethod
    # def get_all_cars(db_name="cars.db"):
    #     with sqlite3.connect(db_name) as conn:
    #         cursor = conn.cursor()
    #         rows = cursor.execute("SELECT * FROM Cars").fetchall()
    #         return [Car(*row) for row in rows]
    
    @staticmethod
    def get_all_cars_data(tab_name="Cars", db_name="cars.db"):
        with sqlite3.connect(db_name) as connect:
            return Car.convert_data_to_car_list(
                connect.cursor().execute(f"SELECT * FROM {tab_name}").fetchall())
        
    
    @staticmethod                
    def convert_data_to_car_list(data):
        return [Car(*i) for i in data]
    # Explanation:
#     return [Car(i[0],i[1],i[2],i[3],i[4]) for i in data]     


    @staticmethod
    def create(data: dict, client_id, db_name="cars.db"):
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Cars (
                    brand, model, year, mileage,
                    engine_fuel, engine_volume,
                    transmission, color,
                    price, description, photo, client_id
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                data['brand'],
                data['model'],
                data['year'],
                data['mileage'],
                data['engine_fuel'],
                data['engine_volume'],
                data['transmission'],
                data['color'],
                data['price'],
                data.get('description', ''),
                data.get('photo'),
                client_id
            ))
            conn.commit()


 
    @staticmethod
    def get_car_by_client(client_id, db_name="cars.db"):
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            rows = cursor.execute("SELECT * FROM Cars WHERE client_id = ?", (client_id,)).fetchall()
            return [Car(*row) for row in rows]
        

    @staticmethod
    def get_сar_by_id(ad_id, db_name="cars.db"):
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            row = cursor.execute("SELECT * FROM Cars WHERE id = ?", (ad_id,)).fetchone()
            return Car(*row) if row else None
        

    @staticmethod
    def update_car(ad_id, data: dict, client_id, db_name="cars.db"):
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT client_id FROM Cars WHERE id = ?", (ad_id,))
            row = cursor.fetchone()
            if not row or row[0] != client_id:
                return False

            cursor.execute("""
                UPDATE Cars SET brand=?, model=?, year=?, mileage=?, fuel_type=?, transmission=?, price=?, description=?, photo=?
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
    def delete_car(ad_id, client_id, db_name="cars.db"):
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT client_id FROM Cars WHERE id = ?", (ad_id,))
            row = cursor.fetchone()
            if not row or row[0] != client_id:
                return False

            cursor.execute("DELETE FROM Cars WHERE id = ?", (ad_id,))
            conn.commit()
            return True
