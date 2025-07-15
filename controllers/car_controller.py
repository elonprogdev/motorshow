import os
from werkzeug.utils import secure_filename
from flask import request, session, flash, redirect, url_for, render_template
from models.car import Car # Импорт модели объявлений


UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/advert_create', methods=['GET', 'POST'])
def car_advert_create():
    if not session.get('logged_in'):
        flash("Пожалуйста, войдите в систему для создания объявления.")
        return redirect(url_for('login'))

    if request.method == 'POST':
        # Обработка изображения
        photo = request.files.get('photo')
        photo_filename = None
        if photo and allowed_file(photo.filename):
            photo_filename = secure_filename(photo.filename)
            save_path = os.path.join(UPLOAD_FOLDER, photo_filename)
            os.makedirs(UPLOAD_FOLDER, exist_ok=True)
            photo.save(save_path)

        # Сбор данных
        data = {
            'brand': request.form['brand'],
            'model': request.form['model'],
            'year': int(request.form['year']),
            'mileage': int(request.form['mileage']),
            'engine_fuel': request.form['engine_fuel'],
            'engine_volume': float(request.form['engine_volume']),
            'transmission': request.form['transmission'],
            'color': request.form['color'],
            'price': int(request.form['price']),
            'description': request.form.get('description', ''),
            'photo': photo_filename
        }

        client_id = session.get('user_id')
        Car.create(data, client_id)

        flash("Объявление успешно создано!")
        return redirect(url_for('home'))

    return render_template('advert.html', css_path=url_for('static', filename='css/home.css'))
