import sqlite3


class Car:
    def __init__(self, car_id, model, volume, price, year, mileage, brand, fuel_type, transmission, description, photo, client_id):
        self.id = car_id
        self.model = model
        self.volume = volume
        self.price = price
        self.year = year
        self.mileage = mileage
        self.brand = brand
        self.fuel_type = fuel_type
        self.transmission = transmission
        self.description = description
        self.photo = photo
        self.client_id = client_id

    def __repr__(self):
        return (f"id: {self.id}, model: {self.model}, volume: {self.volume}, price: {self.price}, "
                f"year: {self.year}, mileage: {self.mileage}, brand: {self.brand}, fuel_type: {self.fuel_type}, "
                f"transmission: {self.transmission}, description: {self.description}, photo: {self.photo}, "
                f"client_id: {self.client_id}")


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