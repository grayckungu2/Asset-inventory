from flask import Flask, request, jsonify, render_template, g
from flask_cors import CORS
import os
from models.dbconfig import db
from config import SQLAlchemyConfig
from datetime import datetime, timedelta
from models.assetallocation import AssetAllocation
from models.assetrequest import AssetRequest
from models.PasswordResetToken import PasswordResetToken
from models.User import User
from models.dbconfig import db
from config import SQLAlchemyConfig



# create_app function
def create_app():
    app = Flask(__name__)
    app.secret_key = 'your_secret_key'  # Replace with a secure secret key
    CORS(app)

    # Initialize database
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLAlchemyConfig.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLAlchemyConfig.SQLALCHEMY_TRACK_MODIFICATIONS
    db.init_app(app)
    
    return app