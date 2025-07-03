from flask import request, session, flash, redirect, url_for, render_template
from models.advert import CarAdvert # Импорт модели объявлений

# @app.route('/advert_create', methods=['GET', 'POST'])
def advert_create():
    if not session.get('logged_in'):
        flash("Пожалуйста, войдите в систему для создания объявления.")
        return redirect(url_for('login'))

    if request.method == 'POST':
        data = {
            'brand': request.form['brand'],
            'model': request.form['model'],
            'year': int(request.form['year']),
            'mileage': int(request.form['mileage']),
            'fuel_type': request.form['fuel_type'],
            'transmission': request.form['transmission'],
            'price': int(request.form['price']),
            'description': request.form.get('description', ''),
            'photo': None  # Здесь можно добавить логику сохранения файла и путь
        }

        client_id = session.get('user_id')
        CarAdvert.create(data, client_id)

        flash("Объявление успешно создано!")
        return redirect(url_for('home'))

    return render_template('create_ad.html', css_path=url_for('static', filename='css/home.css'))
