from flask import Blueprint, send_file
from service import file_service

file_router = Blueprint('file', __name__)


@file_router.route('/file/<file_id>', methods=['GET'])
def file(file_id):
    url, ext = file_service.get_file(file_id)
    return send_file(url, download_name=f'{file_id}.{ext}')
