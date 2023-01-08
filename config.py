import os
import binascii


class Config:
    SECRET_KEY = binascii.b2a_hex(os.urandom(15))
    SQLALCHEMY_DATABASE_URI = "postgresql+pg8000://atesvfzp_adminn:19kemal91@localhost:5432/atesvfzp_my_portfolio"    
    CKEDITOR_ENABLE_CODESNIPPET = True
    CKEDITOR_CODE_THEME = "default"
    
