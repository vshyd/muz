from flask import render_template, Blueprint
from ...extensions import db
from sqlalchemy import text
from ..admin.service import AdminService


main_bp = Blueprint('main', import_name=__name__, template_folder='./templates', static_folder='./static')

admin_service = AdminService()

@main_bp.route('/')
def index():
    return render_template('home.html', year=2025)

@main_bp.route('/artists')
def artists():
    return render_template('artists.html', artists=admin_service.get_artists())

@main_bp.route('/exhibits')
def exhibits():
    return render_template('exhibits.html', exponats=admin_service.get_exponats())

@main_bp.route('/exhibition_rooms')
def exhibition_rooms():
    return render_template('exhibition_rooms.html', exhibition_rooms=admin_service.get_exbition_rooms())

@main_bp.route('/partners')
def partners():
    return render_template('partners.html', institutions=admin_service.get_instutions())
