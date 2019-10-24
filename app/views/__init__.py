from flask import request, redirect, url_for, render_template, flash, jsonify, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from app.application import app
from app.database import db
from random import random
from app.models import Entry

@app.route('/')
def show_entries():
    entries = Entry.query.order_by(Entry.id.desc()).all()
    return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    entry = Entry(
            title=request.form['title'],
            text=request.form['text']
            )
    db.session.add(entry)
    db.session.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))
