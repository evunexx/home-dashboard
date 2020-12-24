from flask import Flask

app = Flask(__name__)

# Geo-Location --> Herford
app.config["Latitude"] = "52.1152245"
app.config["Longitude"] = "8.6711118"
app.config["APIKEY"] = "124461e37ae9cb09ac472ae7cdf6caf0"
app.config["CITY"] = "Elverdissen"

import dashboard.routes
