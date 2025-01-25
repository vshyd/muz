from flask import jsonify, url_for, render_template, Blueprint

from .service import AdminService
from ...extensions import db
from sqlalchemy import text


admin_bp = Blueprint('admin', url_prefix='/admin', import_name=__name__, template_folder='./templates')
admin_service = AdminService()

@admin_bp.route('/')
def index():
    artists = admin_service.get_artists()
    return render_template('index.html', artists=artists)