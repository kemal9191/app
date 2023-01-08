import os
from flask import url_for, current_app
from PIL import Image


def save_picture(picture):
    random_hex = os.urandom(8).hex()
    _, f_ext = os.path.splitext(picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/images', picture_fn)

    i = Image.open(picture)
    i.save(picture_path)

    return picture_fn
