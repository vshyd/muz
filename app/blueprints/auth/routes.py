from flask import render_template, Blueprint, session, redirect, request, url_for
from ...extensions import db
from sqlalchemy import text


auth_bp = Blueprint('auth', import_name=__name__, template_folder='./templates', static_folder='./static')

users = {
    'admin': {'id': 1, 'username': 'admin', 'password': 'admin'}
}

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)
        if user and user['password'] == password:
            session['user_id'] = user['id']
            session['username'] = user['username']
            return redirect(url_for('main.index'))
        return 'Invalid credentials', 401
    return render_template('login.html')


@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.index'))

