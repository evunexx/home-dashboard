import requests
from flask import Flask, redirect, url_for, request, render_template, jsonify
from dashboard import app

#Config files this has to be excluded


@app.route('/dashboard', methods = ['POST', 'GET'])
def dashboard():
    return render_template('dashboard.html')

@app.route('/data/sunrise', methods = ['GET'])
def sunrise():
    response = requests.get(
        'https://api.sunrise-sunset.org/json?lat=%s&lng=%s&formatted=0' % (
            app.config['Latitude'], app.config['Longitude']
        )
    )

    data = response.json()
    return data



