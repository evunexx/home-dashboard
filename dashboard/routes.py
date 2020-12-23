import requests
from flask import Flask, redirect, url_for, request, render_template, jsonify
from flask.logging import create_logger
from dashboard import app
import datetime
from csv_ical import Convert
import csv
import re
import json
import os

# Config files this has to be excluded

LOG = create_logger(app)


@app.route("/dashboard", methods=["POST", "GET"])
def dashboard():
    return render_template("dashboard.html")


@app.route("/data/sunrise", methods=["GET"])
def sunrise():
    response = requests.get(
        "https://api.sunrise-sunset.org/json?lat=%s&lng=%s&formatted=0"
        % (app.config["Latitude"], app.config["Longitude"])
    )

    data = response.json()
    return data


@app.route("/data/bin")
def bin():

    now = datetime.datetime.now()
    year = now.year
    next_year = year + 1
    month = now.strftime("%m")

    url = (
        "https://swk.herford.de/output/abfall_export.php?csv_export=1&mode=vcal&ort=393.9&strasse=395.501.1&vtyp=2&vMo=%s&vJ=%s&bMo=%s"
        % (month, year, month)
    )

    url_year = (
        "https://swk.herford.de/output/abfall_export.php?csv_export=1&mode=vcal&ort=393.9&strasse=395.501.1&vtyp=2&vMo=01&vJ=%s&bMo=12"
        % (year)
    )

    ical_file_current_year = requests.get(url_year)

    ical = open("ical3.ics", "wb")
    ical.write(ical_file_current_year.content)
    ical.close()

    csv_file = convert_ics_to_csv(ical.name)
    csv_reader = csv.reader(open(csv_file, "r"), delimiter=",")

    green = []
    blue = []
    yellow = []
    grey = []

    for row in csv_reader:
        if re.search("Restabfall", row[0]):
            grey.append(row[1])

        if re.search("Biotonne", row[0]):
            green.append(row[1])

        if re.search("Gelber Sack", row[0]):
            yellow.append(row[1])
            blue.append(row[1])

    LOG.warning(green)
    LOG.warning(grey)
    LOG.warning(yellow)
    summary = {}

    date_green = next_closest_date(green)
    date_blue = next_closest_date(blue)
    date_yellow = next_closest_date(yellow)
    date_grey = next_closest_date(grey)

    if date_green:
        summary["green"] = date_green

    if date_blue:
        summary["blue"] = date_blue

    if date_yellow:
        summary["yellow"] = date_yellow

    if date_grey:
        summary["grey"] = date_grey

    summary_json = jsonify(summary)

    return summary_json


def convert_ics_to_csv(ics_data):
    csv = open("temp.csv", "wb")
    csv.close()

    convert = Convert()
    convert.CSV_FILE_LOCATION = csv.name
    convert.SAVE_LOCATION = ics_data

    convert.read_ical(convert.SAVE_LOCATION)
    convert.make_csv()
    convert.save_csv(convert.CSV_FILE_LOCATION)

    return csv.name


def next_closest_date(list):
    """ Takes list of dates pass them to date objects and find closest_dates """

    date_format = "%Y-%m-%d"
    today = datetime.datetime.now()

    # Create an temporarily list to handle data
    temp = []
    future_dates = []

    for date_raw in list:
        temp.append(datetime.datetime.strptime(date_raw, date_format))

    # filter out dates that take place in future (after today)
    for date in temp:
        if date >= today:
            future_dates.append(date)

    next_closest_date = min(future_dates, default=None)

    return next_closest_date