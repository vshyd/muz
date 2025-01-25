from flask import render_template, Blueprint
from ..extensions import db
from sqlalchemy import text


main_bp = Blueprint('main', import_name=__name__, template_folder='./templates', static_folder='./static')


@main_bp.route('/')
def index():
    print('hello')
    return render_template('home.html', year=2025)

@main_bp.route('/about')
def about():
    return render_template('home.html', year=2025)

@main_bp.route('/exhibits')
def exhibits():
    return render_template('home.html', year=2025)

@main_bp.route('/contact')
def contact():
    return render_template('home.html', year=2025)

@main_bp.route('/artists')
def artists():
    return render_template('artists.html', artists=['Gavno', 'zalupa'])

@main_bp.route('/test_db')
def test_db():
    db.session.execute(text('select 1'))
    return 'success'
