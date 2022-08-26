
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import pandas as pd
from datetime import date

#Endpoints para obtener informacion de las peliculas por cines
URL_BASE = 'https://www.cinepolis.com'
URI_GET_CINEMA_BRANCHS = '/manejadores/CiudadesComplejos.ashx'
URI_GET_MOVIES = '/Cartelera.aspx/GetNowPlayingByCity'



CountryList = ['gt','sv','hn','cr','pa']
EndPoint = ''

#Obtiene Sucursales por paises
def GetCinemasBranchByCountry(Country):

    if(Country == 'cr'):
        EndPoint = URL_BASE[:-1]  + '.' + Country + URI_GET_CINEMA_BRANCHS
    else:
        EndPoint = URL_BASE  + '.' + Country + URI_GET_CINEMA_BRANCHS

    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    res = session.get(EndPoint)
    Cinemasresponse = res.json()
    return Cinemasresponse
    
#Obtiene Peliculas por cinema y por pais
def GetMoviesByCinemaBranchAndCountry(CinemaBranch, Country):

    bodyVariables = {
      "claveCiudad": CinemaBranch,
      "esVIP": False
    }
    
    if(Country == 'cr'):
        EndPoint = URL_BASE[:-1]  + '.' + Country + URI_GET_MOVIES
    else:
        EndPoint = URL_BASE  + '.' + Country + URI_GET_MOVIES

    data = requests.post(EndPoint, json=bodyVariables)
    if data != None or data != '':
        return data.json()

#Obtiene las peliculas del dia actual
def filterTodayMovies(data):
  objMovie = next(filter(lambda movies: str(date.today().day) in movies["ShowtimeDate"], data), None)
  if objMovie != None:
    return objMovie["Movies"]
  else:
    return objMovie

# Obtiene los horarios de las peliculas
def getAllHours(formatsHours):
  hoursArray = []
  for format in formatsHours:
    for showtime in format['Showtimes']:
      hoursArray.append(showtime['Time'])
  return hoursArray


def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        ("Á", "A"),
        ("É", "E"),
        ("Í", "I"),
        ("Ó", "O"),
        ("Ú", "U"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

GlobalData = pd.DataFrame(columns=['Country',
                                   'CityKey',
                                   'CityName',
                                   'Id',
                                   'Key',
                                   'Name',
                                   'Title',
                                   'Hours'])#Creando nuevo dataframe para el nuevo Archivo
                                   


#Funcion principal 
def DataCollectCinepolis():
    indexLLenado = 0
    for country in CountryList:

        CinemaBranches = GetCinemasBranchByCountry(country)
        BranchsData = pd.DataFrame(CinemaBranches)

        Movies = BranchsData["Clave"].map(lambda Branch: GetMoviesByCinemaBranchAndCountry(Branch,country))
        Cinemas = list(map(lambda x: x['d']['Cinemas'], Movies))

        MoviesByCinemas = [element for sublist in Cinemas for element in sublist]
        MoviesData = pd.DataFrame(MoviesByCinemas)
        MoviesData["TodayMovies"] = MoviesData["Dates"].apply(filterTodayMovies)
        MoviesData = MoviesData.explode("TodayMovies")
        MoviesData = MoviesData.reset_index(drop=True)
        MoviesData = MoviesData.drop(columns=['IsPresale', 'Children', 'Order', 'TimeZoneDifference', 'Status', 'VistaId', 'Dates'])
        MoviesData['Title'] = MoviesData["TodayMovies"].apply(lambda todaysMovie: todaysMovie['Title'])
        MoviesData["Hours"] = MoviesData["TodayMovies"].apply(lambda todaysMovie: getAllHours(todaysMovie['Formats']))
        MoviesData = MoviesData.drop(columns=['TodayMovies'])

        for index, MovieRow in MoviesData.iterrows():
          GlobalData.at[indexLLenado,'Country'] = country
          GlobalData.at[indexLLenado,'CityKey'] = MovieRow['CityKey']
          GlobalData.at[indexLLenado,'CityName'] = MovieRow['CityName']
          GlobalData.at[indexLLenado,'Id'] = MovieRow['Id']
          GlobalData.at[indexLLenado,'Key'] = MovieRow['Key']
          GlobalData.at[indexLLenado,'Name'] = normalize(MovieRow['Name'])
          GlobalData.at[indexLLenado,'Title'] = normalize(MovieRow['Title'])
          GlobalData.at[indexLLenado,'Hours'] = MovieRow['Hours'] 
          
          indexLLenado = indexLLenado + 1

    GlobalData.to_csv('Cinepolis-'+ "Generico" +'-Data-Collection-'+str(date.today().day)+'.csv', sep=',', encoding='utf-8', index=False)

DataCollectCinepolis()
