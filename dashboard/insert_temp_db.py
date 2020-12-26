import sys
import os
import json
import datetime
import sqlite3


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)

    return conn


date = datetime.datetime.now()

with open("temp.txt", "w") as f:
    pass
process = os.popen("sudo rtl_433 -R 03 -F json:temp.txt -T 60 | grep id")
str = process.read()
process.close()

print("hier kommt mein JSON:")

data = [json.loads(line) for line in open("temp.txt", "r")]
print(data)
# prepare list comprehension
for item in data:
    item.pop("time")
    item.pop("model")
    item.pop("subtype")
    item.pop("channel")
    item.pop("humidity")
    item.pop("button")
# using list comprehension to
# remove duplicates
res_list = [i for n, i in enumerate(data) if i not in data[n + 1 :]]
print("removed dublicates")
print(res_list)

# Prepare database insert

database = "db.db"
conn = create_connection(database)
with conn:
    cursor = conn.cursor()

    for entry in res_list:
        # print(entry)
        hour = date.hour
        day = date.day
        device_id = entry["id"]
        temperature = entry["temperature_C"]
        battery = entry["battery_ok"]
        sql = (
            (
                """
INSERT INTO entrys(
temperature,
battery,
hour,
day,
sensor_id)
VALUES(
%d,
%d,
%d,
%s,
(SELECT id from sensor where device_id=%d)
)
"""
            )
            % (temperature, battery, hour, day, device_id)
        )
        print(sql)
        cursor = conn.cursor()
        count = cursor.execute(sql)
        conn.commit()
        cursor.close()


print(data)
print(res_list)
