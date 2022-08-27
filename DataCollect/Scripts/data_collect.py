import os
import pandas as pd

import GetCinemarkData as cinemark

# import GetCinepolisData as cinepolis

from datetime import date

from rich import print
from art import *
from fuzzywuzzy import fuzz, process

print(text2art("Recoleccion de datos"))

print("Obteniendo datos de Cinemark")
try:
    cinemark.get_cinemark_data()
except Exception as e:
    print(e)
    print("Error al obtener datos de Cinemark")

print("Obteniendo datos de Cinepolis")
try:
    cinepolis.DataCollectCinepolis()
except Exception as e:
    print(e)
    print("Error al obtener datos de Cinepolis")

print("Obteniendo datos de Cinemas")
try:
    import GetCinemasData as cinemas
except Exception as e:
    print(e)
    print("Error al obtener datos de Cinemas")

# read data from csv
cinemark_data = pd.read_csv(f"Cinemark_{date.today()}.csv")
cinemas_data = pd.read_csv(f"Cinemas_{date.today()}.csv")
cinepolis_data = pd.read_csv("Cinepolis-sv-Data-Collection-26.csv")

# merge data
merged_data = pd.merge(cinemark_data, cinemas_data, on="title")

# export to csv
merged_data.to_csv(f"Merged_{date.today()}.csv", index=False)

original_data = []

# for each file in the directory original_data
for file in os.listdir("original_data"):
    df = pd.read_excel(f"original_data/{file}")
    df = df.iloc[2:]

    # remove first 2 column
    df = df.iloc[:, 2:]

    # remove from fifth column to 31th column
    df = df.drop(df.columns[4:31], axis=1)

    # remove from 5th column to end
    df = df.drop(df.columns[5:], axis=1)

    # give column names
    df.columns = [
        "Theatre Name",
        "title",
        "City",
        "Circuit",
        "admission",
    ]
    original_data.append(df)

origin_data = pd.concat(original_data)

# use fuzzywuzzy to find the best match bewteen original data and merged data
for index, row in origin_data.iterrows():
    # get the title of the movie
    title = row["title"]
    # get the theatre name
    theatre = row["Theatre Name"]
    # get the city of the theatre
    city = row["City"]
    # get the circuit of the theatre
    circuit = row["Circuit"]
    # get the admission of the theatre
    admission = row["admission"]

    # get the best match from the merged data
    best_match = process.extractOne(title, merged_data["title"])
    # get the best match from the original data
    best_match_original = process.extractOne(title, origin_data["title"])

    # if the best match is greater than 80%
    if best_match[1] > 80:
        # print the best match
        print(f"{title} - {theatre} - {best_match[0]} - {best_match[1]}")
        # print the best match from the original data
        print(
            f"{title} - {theatre} - {best_match_original[0]} - {best_match_original[1]}"
        )
        # print the city of the theatre
        print(f"{theatre} - {city}")
        # print the circuit of the theatre
        print(f"{theatre} - {circuit}")
        # print the admission of the theatre
        print(f"{theatre} - {admission}")
        # print the difference between the best match and the best match from the original data
        print(
            f"{title} - {theatre} - {best_match[0]} - {best_match[1]} - {best_match_original[0]} - {best_match_original[1]}"
        )
        # print the difference between the best match and the best match from the original data
        print(
            f"{title} - {theatre} - {best_match[0]} - {best_match[1]} - {best_match_original[0]} - {best_match_original[1]}"
        )
        # print the difference between the best match and the best match from the original data
        print(
            f"{title}) - {theatre} - {best_match[0]} - {best_match[1]} - {best_match_original[0]} - {best_match_original[1]}"
        )

# export to csv
# origin_data.to_csv(f"Datos_{date.today()}.csv", index=False)
