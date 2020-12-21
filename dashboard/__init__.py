from flask import Flask

app = Flask(__name__)

# Geo-Location --> Herford
app.config['Latitude'] = '52.1152245'
app.config['Longitude'] = '8.6711118'

import dashboard.routes
