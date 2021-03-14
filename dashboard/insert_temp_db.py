import sys
import os
import json
import datetime
import subprocess
import sqlite3


 # Try to catch Data from Sensor

def read_temperature_from_sensor(conn):

    with open("temp.txt", "w+") as fout:
        try_count = 0
        error = False
        while try_count <5:
            try:
                process = subprocess.check_call('rtl_433 -R 03 -F json:temp.txt -T 60 | grep id', shell=True, timeout=180)
                break

            except subprocess.CalledProcessError as e:
                print("Try to Catch Data from Sensor: .. "+ str(try_count))
                try_count += 1
                error = True

    if error:
        return False

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

    # using list comprehension to remove duplicates
    res_list = [i for n, i in enumerate(data) if i not in data[n + 1 :]]

    with conn:
        cursor = conn.cursor()

        for entry in res_list:
            
            device_id = entry["id"]
            temperature = entry["temperature_C"]
            battery = entry["battery_ok"]

            sql = (
                (
                    """
    INSERT INTO entrys(
    temperature,
    battery,
    modtime,
    sensor_id)
    VALUES(
    %d,
    %d,
    (SELECT datetime('now','localtime')),
    (SELECT id from sensor where device_id=%d)
    )
    """
                )
                % (temperature, battery, device_id)
            )
            print(sql)
            cursor = conn.cursor()
            count = cursor.execute(sql)
            conn.commit()
            cursor.close()


    print(data)
    print(res_list)

    return "ok"
