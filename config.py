import os
import binascii

""" database_filename = "database"
project_dir = os.path.dirname(os.path.abspath(__file__)) """
database_path = "sqlite:///my_port.db"

class Config:
    SECRET_KEY = binascii.b2a_hex(os.urandom(15))
    SQLALCHEMY_DATABASE_URI = database_path
    CKEDITOR_ENABLE_CODESNIPPET = True
    CKEDITOR_CODE_THEME = "default"
    
