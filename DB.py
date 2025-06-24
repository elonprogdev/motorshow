import sqlite3 



with sqlite3.connect("cars.db") as connect:
    cursor = connect.cursor()

    # cursor.execute("DROP TABLE IF EXISTS Lamps")
    # cursor.execute("DROP TABLE IF EXISTS Basket")
    # cursor.execute("DROP TABLE IF EXISTS Clients")
    # cursor.execute("DROP TABLE IF EXISTS Orders")
    # cursor.execute("DROP TABLE IF EXISTS SubOrders")

    cursor.execute("PRAGMA foreign_keys = ON")

    # cursor.execute("""CREATE TABLE IF NOT EXISTS
    #                Cars(
    #                id INTEGER PRIMARY KEY AUTOINCREMENT,
    #                model TEXT NOT NULL,
    #                volume INTEGER NOT NULL,
    #                price INTEGER NOT NULL, 
    #                year INTEGER NOT NULL,
    #                mileage INTEGER NOT NULL
    #                )""")
    

    cursor.execute("""CREATE TABLE IF NOT EXISTS
                   Clients(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   e_mail TEXT NOT NULL,
                   phone TEXT NOT NULL
                   )""")


    # cursor.execute("""CREATE TABLE IF NOT EXISTS
    #            Basket(
    #            id INTEGER PRIMARY KEY,
    #            client_id INTEGER NOT NULL,
    #            lamp_id INTEGER NOT NULL,
    #            quantity INTEGER NOT NULL,
    #            FOREIGN KEY(client_id) REFERENCES Clients(id) ON DELETE CASCADE,
    #            FOREIGN KEY(lamp_id) REFERENCES Lamps(id) ON DELETE CASCADE
    #            )""")

    # cursor.execute("""CREATE TABLE IF NOT EXISTS
    #             Orders(
    #             id INTEGER PRIMARY KEY,
    #             client_id INTEGER NOT NULL,
    #             status TEXT NOT NULL,
    #             FOREIGN KEY(client_id) REFERENCES Clients(id) ON DELETE CASCADE
    #             )""")
    
    
    # cursor.execute("""CREATE TABLE IF NOT EXISTS
    #             SubOrders(
    #             order_id INTEGER NOT NULL,
    #             lamp_id INTEGER NOT NULL,
    #             quantity INTEGER NOT NULL,
    #             FOREIGN KEY(lamp_id) REFERENCES Lamps(id) ON DELETE CASCADE,
    #             FOREIGN KEY(order_id) REFERENCES Orders(id) ON DELETE CASCADE
    #                )""")