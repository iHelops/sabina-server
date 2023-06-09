from flask import Blueprint
from werkzeug.datastructures import FileStorage
from decorators import login_required, file_required
from service import file_service

upload_image_router = Blueprint('upload_image', __name__)
IMAGE_EXT = ['jpeg', 'jpg', 'png', 'gif', 'webp']


@upload_image_router.route('/file/upload-image', methods=['POST'])
@login_required
@file_required(extensions=IMAGE_EXT, max_size=10)
def upload_image(file: FileStorage, user):
    answer = file_service.upload(str(user.id), file, file_type='image')
    return answer
