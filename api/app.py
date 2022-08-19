import json
from flask import Flask, jsonify
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
    return "Movie Database"


# ruta principal para obtener los datos de la base de datos
@app.route("/api/cines", methods=["GET"])
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM cine")
    data = cur.fetchall()
    return jsonify(data)


app.run()
