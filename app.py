from flask import Flask, json, request, send_from_directory, jsonify
import sqlite3
import pandas as pd
import calendar

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')


@app.route('/static/<path:path>')
def send_file(path):
    return send_from_directory('static', path)


@app.route('/api/<year>')
def send_response(year):

    conn = sqlite3.connect("database.db")

    response = []

    for m in range(1,13):
        lb = int(str(year) + str(m).zfill(2) + '00')
        ub = int(str(year) + str(m).zfill(2) + '32')

        sql_template = 'SELECT sum(amount) FROM sales_2010_to_2020 st WHERE date > ? AND  date < ?'
        total_df = pd.read_sql(sql_template, conn, params=(lb, ub))

        month_dict = {
            'year': year,
            'month': m,
            'month_name':  calendar.month_name[m],
            'total_sales': int(total_df.iloc[0,0])
        }

        response.append(month_dict)

    return jsonify(response)


@app.route('/status')
def send_status():

    status_dict = {
        "status": "OK",
        "last_updated": "December 15th, 2021"
    }

    return jsonify(status_dict)


if __name__ == "__main__":
    app.run()