import sqlite3
from flask import session


class Client:
    def __init__(self, client_id, e_mail, phone):
        self.id = client_id
        self.e_mail = e_mail
        self.phone = phone
     
        
    def __repr__(self):
        return f"id:{self.id}, e_mail: {self.e_mail}, phone: {self.phone}"
    
    
    def add_self_to_clients(self, db_name="lamps.db"):
        with sqlite3.connect(db_name) as connect:
            cursor = connect.cursor()
            cursor.execute("""INSERT INTO Clients
                                (e_mail, phone) VALUES(?, ?)""", (self.e_mail, self.phone_number))


    def get_client_by_email(self, db_name="lamps.db"):
        with sqlite3.connect(db_name) as connect:
            data = connect.cursor().execute(f"""SELECT id FROM Clients
                                WHERE e_mail = ?""", (self.e_mail,))
            return Client (*data)
        
        
    @staticmethod
    def delete_client_by_id(id_client, tab_name="Clients", col_name= "id", db_name="lamps.db"):
        with sqlite3.connect(db_name) as connect:
            cursor = connect.cursor()
            cursor.execute(f"""DELETE FROM {tab_name}
                                    WHERE {col_name} = (?)""", (id_client,)) 


    @staticmethod
    def get_all_clients_data(tab_name="Clients", db_name="lamps.db"):
        with sqlite3.connect(db_name) as connect:
            return Client.convert_data_to_profile_list (
                connect.cursor().execute(f"SELECT * FROM {tab_name}").fetchall()) 
        
    
    @staticmethod 
    def get_client_by_id(id_client, db_name="lamps.db"):
        with sqlite3.connect(db_name) as connect:
            return Client.convert_data_for_selected_client(
                connect.cursor().execute(f"SELECT * FROM Clients WHERE id = (?)", (id_client,)).fetchall()
                )
            # Explanation
            # cursor = connect.cursor()
            # data = cursor.execute(f"SELECT * FROM Clients WHERE id = (?)", (id_client,)).fetchall()
            # return data

                  
    @staticmethod     
    def convert_data_to_profile_list(data):
        return [Client(*i) for i in data] # Client(i[0],i[1],i[2])
    
    
    
    @staticmethod                
    def convert_data_for_selected_client(data):
        return Client(*data[0]) if data else None
    
       
    @staticmethod
    def  client_registration (e_mail, phone_number, db_name="cars.db"): #add_client 
        with sqlite3.connect(db_name) as connect:
            cursor = connect.cursor()
            
            if  Client.check_for_register_availability (e_mail, phone_number):
                cursor.execute(f"""INSERT INTO Clients
                                (e_mail, phone) VALUES(?, ?)""", (e_mail, phone_number,))
                return True, "Registered successfully - try login"
            else:
                return False, "Such parameters already exists - try again"     
    
    
    
    @staticmethod 
    def login_client(e_mail, phone_number,db_name="cars.db"):
        with sqlite3.connect(db_name) as connect:
            cursor = connect.cursor()
                      
            if Client.check_for_login_availability (e_mail, phone_number):
                return None, "Invalid data - try again"
            
            else:
                cursor.execute(f"""SELECT id FROM Clients
                                WHERE e_mail = ?""", (e_mail,))
                user_row = cursor.fetchone()
                
                client_id = user_row[0]
                session['logged_in'] = True
                session['user_id'] = client_id
                # add_to_json(id, e_mail, phone_number)
                 # Проверяем, существует ли 'viewed_lamps' в сессии
                if "viewed_lamps" not in session or not isinstance(session["viewed_lamps"], dict):
                    session["viewed_lamps"] = {}  # Инициализируем как словарь, если он не существует

                # Преобразуем client_id в строку для использования в сессии
                client_id_str = str(client_id)

                # Если список для этого client_id не существует, инициализируем его
                if client_id_str not in session["viewed_lamps"]:
                    session["viewed_lamps"][client_id_str] = []  # Инициализируем как список
                return client_id, ""
      
    
    @staticmethod
    def check_for_login_availability (e_mail, phone_number, db_name="cars.db"):
        with sqlite3.connect(db_name) as connect:
            cursor = connect.cursor()
            cursor_data = cursor.execute(f"""
                SELECT id FROM Clients 
                WHERE e_mail = ? AND phone = ? """, (e_mail, phone_number)).fetchall()
            
            print(cursor_data)
            print(len(cursor_data) < 1)
            return len(cursor_data) < 1
        
    
    @staticmethod
    def check_for_register_availability (e_mail, phone_number, db_name="cars.db"):
        with sqlite3.connect(db_name) as connect:
            cursor = connect.cursor()
            cursor_data = cursor.execute(f"""
                SELECT id FROM Clients 
                WHERE e_mail = ? OR phone = ? """, (e_mail, phone_number)).fetchall()
            
            print(cursor_data)
            print(len(cursor_data) < 1)
            return len(cursor_data) < 1    


# Client.check_for_register_availability('qqq',111)

# Client.get_client_by_id(2)
# Client.get_all_clients_data()
           
 
        

    
