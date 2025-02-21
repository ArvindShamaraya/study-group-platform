from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
#from flask_migrate import Migrate
from config import config
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://username:password@localhost/dbname"
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

from app import routes #Avoiding circular imports
