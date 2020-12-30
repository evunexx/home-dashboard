from flask import Flask

app = Flask(__name__)

# Geo-Location --> Herford
app.config["Latitude"] = "52.1152245"
app.config["Longitude"] = "8.6711118"
app.config["APIKEY"] = "b82d9062e7325bbfd4df8f4a57ecea52"
app.config["CITY"] = "Elverdissen"

import dashboard.routes
