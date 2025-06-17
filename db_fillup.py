import sqlite3 
from cars_data import data
# from clients_data import data



if __name__ == "__main__":
    with sqlite3.connect("cars.db") as connect:
        cursor = connect.cursor()

        for i in data:
            cursor.execute(f"""INSERT INTO Cars
                            (model,volume,price,year,mileage) VALUES (?, ?, ?, ?, ?)""", (i[0], i[1],i[2],i[3],i[4])) 