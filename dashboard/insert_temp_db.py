import sys
import os
import json
import datetime
import subprocess
import sqlite3
from dashboard import app


 # Try to catch Data from Sensor

def read_temperature_from_sensor(conn=None):

    with open("temp.txt", "w+") as fout:

        #process = subprocess.check_call('sudo rtl_433 -R 03 -F json:temp.txt -T 60 | grep id', shell=True, timeout=180)
        process = subprocess.run(['sudo rtl_433 -R 03 -F json:temp.txt -T 60 | grep id'], shell=True, check=False, stdout=subprocess.PIPE, universal_newlines=True)
        output = process.stdout

        app.logger.info(output)
        #print (output)


    data = [json.loads(line) for line in open("temp.txt", "r")]

    print('Catched Data:')
    app.logger.info(data)
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

        known_devices = []

        # Device id is known?

        for entry in res_list:

            device_id = entry["id"]

            is_known_device_q = (
                """
                SELECT id from sensor where device_id=%d
                """
            ) % (device_id)

            cursor.execute(is_known_device_q)
            res = cursor.fetchall()

            if res:
                known_devices.append(device_id)
        print("devices:")
        known_devices.append(239)
        print(known_devices)



        for entry in res_list:

            device_id = entry["id"]
            known_device_id = entry["id"] if entry["id"] in known_devices else False
            temperature = entry["temperature_C"]
            battery = entry["battery_ok"]
            print(temperature)

            print("device id:")
            print(device_id)

            if not known_device_id:
                for device in known_devices:

                    update_sensor_q = (
                    """
                    UPDATE sensor
                    SET device_id = %d
                    WHERE NOT device_id = %d
                    """ ) % (device_id, device)

                    cursor.execute(update_sensor_q)
                    conn.commit()


            sql = (
                (
                    """
    INSERT INTO entrys(
    temperature_numeric,
    battery,
    modtime,
    sensor_id)
    VALUES(
    %s,
    %d,
    (SELECT datetime('now','localtime')),
    (SELECT id from sensor where device_id=%d)
    )
    """
                )
                % (temperature, battery, device_id)
            )
            app.logger.info('SQL:')
            app.logger.info(sql)
            cursor = conn.cursor()
            count = cursor.execute(sql)
            conn.commit()
            cursor.close()


    app.logger.info(res_list)

    return "ok"
