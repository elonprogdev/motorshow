import sqlite3


class Car:
    def __init__(self, car_id, model, volume, price, year, mileage):
        self.id = car_id
        self.model = model
        self.volume = volume
        self.price = price
        self.year = year
        self.mileage = mileage

    
    def __repr__(self):
        return f"id: {self.id}, model: {self.model}, voltage: {self.volume}, price: {self.price}, year: {self.picture}, mileage: {self.mileage}"
    

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