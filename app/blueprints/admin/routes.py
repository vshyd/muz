from crypt import methods
from flask import jsonify, request, request_started, url_for, render_template, Blueprint

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
    history = admin_service.get_history()
    return render_template('index.html',
                            artists=artists,
                            exponats=exponats,
                            exhibition_rooms=exhibition_rooms,
                            institutions=institutions,
                            history=history)


@admin_bp.route('/get_exponats')
def get_exponats():
    return jsonify([dict(exponat) for exponat in admin_service.get_assign_exponats()])

@admin_bp.route('/get_rent_exponats')
def get_exponats_rent():
    return jsonify([dict(exp) for exp in admin_service.get_rent_exponats()])


@admin_bp.route('/rent_exponat', methods=['POST'])
def rent_exponat():
    data = request.json
    response = admin_service.rent_exponat(data)
    return response


@admin_bp.route('/assign_exponat', methods=['POST'])
def assign_exponats():
    data = request.json
    response = admin_service.assign_exponat_to_gallery(data)
    return response


@admin_bp.route('/save_new_artist', methods=['POST', 'PUT'])
def save_new_artist():
    if request.method == 'POST':
        data = request.json
        response = admin_service.save_new_artist(data)
    else:
        data = request.json
        print(data)
        response = admin_service.update_artist(data)
    return response


@admin_bp.route('/save_new_institution', methods=['POST', 'PUT'])
def save_new_institution():
    if request.method == 'POST':
        data = request.json
        response = admin_service.save_new_institution(data)
    else:
        data = request.json
        response = admin_service.update_institution(data)
    return response


@admin_bp.route('/save_new_exponat', methods=['POST', 'PUT'])
def save_new_exponat():
    if request.method == 'POST':
        data = request.json
        response = admin_service.save_new_exponat(data)
    else:
        data = request.json
        response = admin_service.update_exponat(data)
    return response


@admin_bp.route('/save_new_gallery', methods=['POST', 'PUT'])
def save_new_gallery():
    if request.method == 'POST':
        data = request.json
        response = admin_service.save_new_gallery(data)
    else:
        data = request.json
        response = admin_service.update_gallery(data)
    return response
