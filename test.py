import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import schedule
from datetime import datetime, timedelta

import mysql.connector

# mydb = mysql.connector.connect(
#     host="localhost", user="root", password="", database="bi"
# )

today = datetime.now().strftime("%d/%m/%Y")
day = datetime.now().strftime("%d")

mycursor = mydb.cursor()
print(today)


# def insertDB(val):
#     sql = "INSERT INTO pelicula(nombre, idpeli, fecha, sala, hora, idcine, tipo) VALUES(%s, %s,%s, %s,%s, %s, %s)"
#     mycursor.execute(sql, val)
#     mydb.commit()


# def updateDB(val):
#     sql = "UPDATE pelicula set asistencias = %s WHERE id = %s"
#     mycursor.execute(sql, val)
#     mydb.commit()


# def cleanDB():
#     sql = "DELETE FROM pelicula WHERE fecha = %s"
#     val = (today,)
#     mycursor.execute(sql, val)
#     mydb.commit()


main_url = "https://www.cinepolis.com.sv/cartelera"
main_xpath = '//*[@id="main-app"]/div/div[5]/div/div[2]/section/div'
horario_xpath = "[2]/div[2]/div[1]/div/div[4]/ul/li/div[2]/div"
driver = None
catalogo = []


def getPelis(idciu, idcn, idcine, id_p, h_p, id):
    driver.get(main_url)
    driver.maximize_window()
    cmbciu = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="cityBillboardSearch"]'))
    )
    cmbciu.click()
    ciu = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, idciu)))
    ciu.click()
    cmbcine = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="cinemaBillboardSearch"]'))
    )
    cmbcine.click()
    cine = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, idcn)))
    cine.click()
    WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/main/div/div/div[5]/section[5]/div/div/div")
        )
    )
    peliculas = driver.find_elements_by_xpath(
        "/html/body/main/div/div/div[5]/section[5]/div/div/div"
    )

    ids = []
    if id_p == None:
        for p in peliculas:
            ids.append(p.get_attribute("id"))
    else:
        ids.append(id_p)
    for peli in ids:
        idpeli = peli
        driver.execute_script("window.scrollTo(0, {})".format(400))
        time.sleep(1)
        pelicula = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.ID, peli))
        )
        pelicula.click()
        driver.execute_script("window.scrollTo(0, {})".format(500))
        time.sleep(1)
        nombre = (
            WebDriverWait(driver, 60)
            .until(EC.presence_of_element_located((By.XPATH, (main_xpath + "[1]/h1"))))
            .text
        )
        fechaPeli = (
            WebDriverWait(driver, 60)
            .until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        '//*[@id="date"]/div/div[1]/div/label/div[2]/div/div/div[2]/span',
                    )
                )
            )
            .text
        )
        if fechaPeli != str(day):
            driver.back()
            continue
        try:
            tipos = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, (main_xpath + horario_xpath + "[1]/div[1]/span"))
                )
            )
        except:
            print("No tiene horarios")
            driver.back()
            continue
        horarios = []
        if h_p == None:
            horas = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, (main_xpath + horario_xpath + "/div[2]/div/label"))
                )
            )
            for h in horas:
                horarios.append(h.text)
        else:
            horarios.append(h_p)
        for h1 in horarios:
            time.sleep(2)
            hora = h1
            horas = WebDriverWait(driver, 60).until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, (main_xpath + horario_xpath + "/div[2]/div/label"))
                )
            )
            for h in horas:
                if h1 == h.text:
                    tipo = h.find_element_by_xpath("../../../div/span").text
                    tipo = tipo + h.find_element_by_xpath("../../../div/h5").text
                    driver.execute_script("window.scrollTo(0, {})".format(900))
                    time.sleep(1)
                    h.click()
                    WebDriverWait(driver, 60).until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="buyTickets"]'))
                    ).click()
                    sala = (
                        WebDriverWait(driver, 60)
                        .until(
                            EC.presence_of_element_located(
                                (
                                    By.XPATH,
                                    '//*[@id="containerMovieDetail"]/div[4]/span',
                                )
                            )
                        )
                        .text
                    )
                    x = sala.split(" ", 1)
                    if id == None:
                        val = (nombre, idpeli, today, x[1], hora, idcine, tipo)
                        insertDB(val)
                    else:
                        asistencias = (
                            len(
                                WebDriverWait(driver, 60).until(
                                    EC.presence_of_all_elements_located(
                                        (
                                            By.XPATH,
                                            "//*[contains(@src,'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADQAAAAtCAYAAADhoUi4AAAABHNCSVQICAgIfAhkiAAAAi9JREFUaEPtmktOwzAQhmfcx5Y62ZQVFReAHoEDIMQFgBugHgAJblBuUJbsegOKxBIhVmzhArW7pm0GTZRUTkhLQy0cwCNFlRJnPL/n87TyFKHAtNYtADgnojMA6BSNcXRviIjXUsrRsvkx/0BrvU9EdwDAoippRNQPw7BXFFxGEGeGiF6rLCYVgYg9KWU/LyojaDweDxDxNB1Ur9dBCFGJLBERzGYz4M/EJkEQyJWClFKcnXjPNBoNQPxEpHNx0+l0IQoRD/L7KROxUmohv9lsOg++KADOUhRF8SMiugrD8NIcFwtKqtoeES2qR61Wi8dxlqqAHaPG13w+N7EbIeIAAO6llG9xvFrrTlLVlpZnFsUIujLOCGdmhU2SIjFApdQQAI6+CtZVgeCs8L5Zw1hUlwVNAGCLX8ijlaY5fcaiftrM7DAp+UJlxshFggUtLQTm6rBYF4J4z/C1bFHNIuEF+QxZ2HAeOV8ULGBUxoVHziNXhhcLYz1yHjkLGJVx4ZHzyJXhxcJYj5xHzgJGZVx45DxyZXixMPZbyPHRkHEIbiEMNy7iUx+tNf0FMckSHmbO5dysq71Z+Tg4I6iqLZRVknPdiJtfL8jsFxGRF2QPeEue/leGqtqGXJXMogxxr2LtVnfVGsnmdygiXnCVewKAriWkXbqJEHGXfynwny1eAGDbZTQbzv0uhDhptVq3i7a+1noHAI4LHD9vOJm114UQ7SiK2qZDInoMguAhvfcBcs3yY6nLfpsAAAAASUVORK5CYII=')]",
                                        )
                                    )
                                )
                            )
                            - 1
                        )
                        val = (asistencias, id)
                        updateDB(val)
                    time.sleep(1)
                    driver.back()
                    break
        driver.back()


def init():
    global driver
    mycursor.execute("select * from cine where estado = 1")
    cines = mycursor.fetchall()
    driver = webdriver.Chrome()
    for x in cines:
        getPelis(x[2], x[3], x[0], None, None, None)
    driver.quit()


init()


def job():
    global catalogo
    global driver
    h_1 = (datetime.now() + timedelta(minutes=-3)).strftime("%H:%M")
    h_2 = (datetime.now() + timedelta(minutes=3)).strftime("%H:%M")
    h = datetime.now().strftime("%H:%M")

    if len(catalogo) > 0:
        trash = []
        for p in catalogo:
            if str(p[4]) == h_2:
                trash.append(p)
        if len(trash) > 0:
            driver = webdriver.Chrome()
            for p in trash:
                print(h, "-> Buscando asistencias de:", p[6], "Hora:", p[4])
                getPelis(p[0], p[1], p[2], p[3], p[4], p[5])
                catalogo.remove(p)
                print("Quedan:", len(catalogo), "funciones")
            driver.quit()


def customSchedule():
    global catalogo
    par = (today,)
    mycursor.execute(
        "select c.idciu, c.idcn,c.idcine,p.idpeli, p.hora, p.id, p.nombre from pelicula p join cine c on c.idcine = p.idcine where p.fecha = %s and isnull(p.asistencias)",
        par,
    )
    catalogo = mycursor.fetchall()
    job()
    schedule.every(1).minutes.do(job)
    while len(catalogo) > 0:
        schedule.run_pending()
        time.sleep(1)
    schedule.clear()


customSchedule()
