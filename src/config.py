import os


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "secret-key-ocr"
    UPLOAD_FOLDER = os.environ.get("UPLOAD_FOLDER") or "../taxnotice"
