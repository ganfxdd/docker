from flask import request, redirect, url_for, render_template, flash, jsonify, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from app.application import app
from app.database import db


@app.route('/')
def index():
    return 'Hello World'
