from crypt import methods
from flask import jsonify, request, url_for, render_template, Blueprint

from .service import AdminService
from ...extensions import db
from sqlalchemy import text


admin_bp = Blueprint('admin', url_prefix='/admin', import_name=__name__, template_folder='./templates', static_folder='./static')
admin_service = AdminService()

@admin_bp.route('/')
def index():
    artists = admin_service.get_artists()
    exponats = admin_service.get_exponats()
    exhibition_rooms = admin_service.get_exbition_rooms()
    institutions = admin_service.get_instutions()
    return render_template('index.html',
                            artists=artists,
                            exponats=exponats,
                            exhibition_rooms=exhibition_rooms,
                            institutions=institutions)


@admin_bp.route('/get_exponats')
def get_exponats():
    return jsonify([dict(exponat) for exponat in admin_service.get_exponats()])


@admin_bp.route('/assign_exponat', methods=['POST'])
def assign_exponats():
    data = request.json
    response = admin_service.assign_exponat_to_gallery(data)
    return response


@admin_bp.route('/save_new_artist', methods=['POST'])
def save_new_artist():
    data = request.json
    response = admin_service.save_new_artist(data)
    return response


@admin_bp.route('/save_new_institution', methods=['POST'])
def save_new_institution():
    data = request.json
    response = admin_service.save_new_institution(data)
    return response