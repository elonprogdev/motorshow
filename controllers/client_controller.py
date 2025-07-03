from flask import render_template, request, redirect, url_for, flash, session, make_response
from models.client import Client
# from models.order import Order
import config





# @app.route("/profile")
def profile():
    logged_in = session.get('logged_in', False) 
    client_id = request.cookies.get('client_id')
    # Чтение данных из cookie
    e_mail = request.cookies.get('e_mail') # e-mail для кнопки "Profile"
    print(session["viewed_lamps"][client_id])
  
    return render_template("client/profile.html", Profile = e_mail, logged_in=logged_in,
                            client_data = Client.get_client_by_id(client_id),
                            order_data = Order.get_all_orders_data_by_client_id(client_id),
                            view=session["viewed_lamps"][client_id], css_path = url_for('static', filename='css/catalog.css') )



# @app.route('/register', methods=['GET'])
def register():
    # Получаем данные из формы
    e_mail = request.args['e_mail']
    phone_number = request.args['number']
        
    mark, message =  Client.client_registration(e_mail,phone_number)
    flash (message)
    if mark:
        return render_template('/client/login.html', style= "confirm-message")
    else:         
        return redirect(url_for('registration'))



# @app.route('/log_in', methods=['GET'])
def log_in():

    e_mail = request.args['e_mail']
    phone_number = request.args['number']

    print(e_mail, config.admin_mail, " ", phone_number, config.admin_phone)
    if e_mail == config.admin_mail and phone_number == config.admin_phone:
            session['admin_logged_in'] = True
            # session['user_id'] = client_id
            return redirect(url_for('admin/home'))
    
    else:
        id_client, message = Client.login_client(e_mail, phone_number)        
        flash(message)
        
        if id_client is not None:
            # Сохранение данных в cookie
            response = make_response(redirect(url_for('home')))
            response.set_cookie('client_id', str(id_client), httponly=True, secure=True)  # Преобразуем id_client в строку
            response.set_cookie('e_mail', e_mail)
            response.set_cookie('phone_number', phone_number)
            return response
        else:
            # Если id_client None, вернем пользователя на страницу входа
            return render_template('/client/login.html', style= "alert-message")



# @app.route('/logout')
def logout():
# Удаление данных из сессии
    session.pop('logged_in', None)
    session.pop('user_id', None)
 

    # # Удаляем существующее содержимое в users.json
    # with open(file_path, 'w') as file:
    #     json.dump({}, file)

    # Удаляем cookie
    response = make_response(redirect('/'))
    response.set_cookie('client_id', '', expires=0)
    response.set_cookie('e_mail', '', expires=0)
    response.set_cookie('phone_number', '', expires=0)

    return response
  




