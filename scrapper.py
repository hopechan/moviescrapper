import json
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

# import By
from selenium.webdriver.common.by import By

# url a scrapear
URL = "https://www.cinemarkca.com/el-salvador/cine?tag=784"

options = Options()
options.headless = True
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get(URL)
driver.implicitly_wait(15)

# obtenemos el titulo de las peliculas
movies_titles = driver.find_elements(by=By.XPATH, value="//div[@class='movie-title']/a")

# obtenemos el rating de las peliculas
movies_ratings = driver.find_elements(
    by=By.XPATH, value="//div[@class='movie-details']/ul//li[1]"
)

# obtenemos la duracion de las peliculas
movies_duration = driver.find_elements(
    by=By.XPATH, value="//div[@class='movie-details']/ul//li[2]"
)

# obtenemos las funciones de las peliculas
movies_functions = driver.find_elements(
    by=By.XPATH, value="//div[@class='movie-times']"
)

# create a merged list of titles.text and ratings.text
movies = [
    (movie_title.text, movie_rating.text, movie_duration.text)
    for movie_title, movie_rating, movie_duration in zip(
        movies_titles, movies_ratings, movies_duration
    )
]

# print a json list of movies
print(json.dumps(movies))

driver.quit()
