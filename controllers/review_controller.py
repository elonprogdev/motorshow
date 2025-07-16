from flask import render_template, session, request, redirect, url_for, send_file, flash
from models.review import Review 




# @app.route('/review/<int:reviewed_id>', methods=['POST'])
def leave_review(reviewed_id):
    if not session.get('logged_in'):
        flash('Авторизуйтесь, чтобы оставить отзыв.')
        return redirect(url_for('login'))

    author_id = session.get('user_id')
    text = request.form['text']
    Review.add_review(author_id, reviewed_id, text)
    flash('Отзыв успешно добавлен!')
    return redirect(url_for('profile', client_id=reviewed_id))
