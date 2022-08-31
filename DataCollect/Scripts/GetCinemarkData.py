import csv
import requests
import json
import numpy as np
import pandas as pd

from rich import print
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from datetime import date

BASE_URL = "https://api.cinemarkca.com/api/vista/data/billboard"
MOVIES = []

COUNTRY_LIST = [
    {"cine": "CR_Multiplaza Escazú", "codigo": 770},
    {"cine": "CR_Multiplaza Curridabat", "codigo": 773},
    {"cine": "CR_Citymall Alajuela", "codigo": 2204},
    {"cine": "CR_Oxigeno", "codigo": 2210},
    {"cine": "SV_Metrocentro San_Miguel", "codigo": 780},
    {"cine": "SV_Metrocento San_Salvador", "codigo": 782},
    {"cine": "SV_La Gran Via", "codigo": 784},
    {"cine": "GT_Arkadia", "codigo": 2202},
    {"cine": "GT_Metrocentro Villa_Nueva", "codigo": 2206},
    {"cine": "GT_Majadas Once", "codigo": 2208},
    {"cine": "HN_Multiplaza Tegucigalpa", "codigo": 771},
    {"cine": "HN_Citymall San Pedro Sula", "codigo": 774},
    {"cine": "HN_Galerias Del Valle", "codigo": 2200},
    {"cine": "HN_Citymall Tegucigalpa", "codigo": 2201},
    {"cine": "HN_Megaplaza La Ceiba", "codigo": 2207},
    {"cine": "NI_Metrocentro Managua", "codigo": 772},
    {"cine": "PA_Albrook Mall", "codigo": 795},
    {"cine": "PA_Pacific Center", "codigo": 2209},
]


def get_total_funciones(movie_versions):
    data = {}
    for version in movie_versions:
        # sum the value of all the sessions of the movie
        total_seats = 0
        hours = []
        for session in version["sessions"]:
            seats = session["seats_available"]
            total_seats += seats
            hours.append(session["hour"])

        data = {
            "Functions": len(version["sessions"]),
            #"total_seats": total_seats,
            "Hours": hours,
        }
    return data


def build_movie(movies, cinema, country):
    for movie in movies["movies"]:
        data = {
            "Country": country,
            "Theatre Name": cinema,
            "Title": movie["title"],
            "City": 'Unknown',
            "Circuit": 'Cinemark'           
        }
        data.update(get_total_funciones(movie["movie_versions"]))
        MOVIES.append(data)


def fetch_data(country):
    print(f"Obteniendo datos de {country['cine']}")
    print(f"{BASE_URL}?cinema_id={country['codigo']}")
    response = requests.get(f"{BASE_URL}?cinema_id={country['codigo']}")
    movies = response.json()
    movies_split = country["cine"].split("_")
    build_movie(movies[0], movies_split[1], movies_split[0])


def get_cinemark_data():
    for country in COUNTRY_LIST:
        fetch_data(country)

    # export to csv
    df = pd.DataFrame(MOVIES)

    # filename must have date
    df.to_csv(f"Cinemark_{date.today()}.csv", index=False)

    print(f"Datos de Cinemark exportados a Cinemark_{date.today()}.csv")


# get_cinemark_data()
