from flask import Flask, redirect, url_for, request, render_template, jsonify
from dashboard import app


@app.route('/dashboard', methods = ['POST', 'GET'])
def dashboard():
    return render_template('dashboard.html')
