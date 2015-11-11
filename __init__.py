from flask import Flask
import os

# create application
ASSETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), './static/app')
app = Flask(__name__, static_folder=ASSETS_DIR)
from app import views