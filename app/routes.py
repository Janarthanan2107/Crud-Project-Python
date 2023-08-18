from flask import render_template, request, redirect, url_for
from app import app, mongo

@app.route('/')
def home():
    return render_template('dashboard.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/add_details', methods=['GET', 'POST'])
def add_details():
    if request.method == 'POST':
        name = request.form['name']
        details = request.form['details']
        age = request.form['age']
        detail = {'name': name, 'details': details,'age':age,}
        mongo.db.details.insert_one(detail)
        return redirect(url_for('add_details'))
    return render_template('add_details.html')

@app.route('/show_details')
def show_details():
    details = mongo.db.details.find()
    return render_template('show_details.html', details=details)