from flask import Blueprint
from werkzeug.datastructures import FileStorage
from decorators import login_required, file_required
from service import file_service

upload_icon_router = Blueprint('upload_icon', __name__)
IMAGE_EXT = ['svg']


@upload_icon_router.route('/file/upload-icon', methods=['POST'])
@login_required
@file_required(extensions=IMAGE_EXT, max_size=5)
def upload_icon(file: FileStorage, user):
    answer = file_service.upload(str(user.id), file, file_type='icon')
    return answer
