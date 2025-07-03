import sqlite3 
from cars_data import data



if __name__ == "__main__":
    with sqlite3.connect("cars.db") as connect:
        cursor = connect.cursor()

        for i in data:
            cursor.execute("""INSERT INTO Cars
                              (model, volume, price, year, mileage, brand, fuel_type, transmission, description, photo, client_id)
                              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                           (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]))

