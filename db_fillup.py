import sqlite3 
from cars_data import data  # data = [Car(...), Car(...), ...]

if __name__ == "__main__":
    with sqlite3.connect("cars.db") as connect:
        cursor = connect.cursor()

        for i in data:
            cursor.execute("""
                INSERT INTO Cars
                (brand, model, year, mileage, engine_fuel, engine_volume, transmission, color, price, description, photo, client_id)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                i.brand,
                i.model,
                i.year,
                i.mileage,
                i.engine_fuel,
                i.engine_volume,
                i.transmission,
                i.color,
                i.price,
                i.description,
                i.photo,
                i.client_id
            ))

        connect.commit()
        print("Таблица Cars пересоздана и успешно заполнена.")

