import json

from datetime import date

from flask import Flask, jsonify, send_file, render_template
from flask_mysqldb import MySQL


app = Flask(__name__)
app.config["DEBUG"] = True

app.config["MYSQL_HOST"] = "127.0.0.1"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "cine"
app.config["MYSQL_DB"] = "cine"
app.config["MYSQL_PORT"] = 3306
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


# ruta principal para obtener los datos de la base de datos
@app.route("/api/cines", methods=["GET"])
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM cine")
    data = cur.fetchall()
    return jsonify(data)


@app.route("/api/cines/data_collect", methods=["GET"])
def collect_data():
    import data_collect

    return "Data Collected"


# make an endpoint to dowloand Data.csv
@app.route("/api/cines/download", methods=["GET"])
def download():
    return send_file(
        f"Datos_{date.today()}.csv",
        download_name=f"Datos_{date.today()}.csv",
        as_attachment=True,
    )


app.run()
