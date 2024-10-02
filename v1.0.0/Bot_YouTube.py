from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import logging
import datetime

options = Options()
options.add_argument("--disable-extensions") 

driver = webdriver.Chrome(options=options)
driver.get("https://www.youtube.com.ar")

logging.basicConfig(
    filename='anuncios_omitidos.log',
    level=logging.INFO,
)

contador = 0     
    
def sileciar_patrocinado():
    try:
        Estado = driver.find_element(By.CSS_SELECTOR, "button[data-title-no-tooltip='Silenciar']")
        if Estado:
            silenciar = driver.find_element(By.CSS_SELECTOR, ".ytp-mute-button")
            silenciar.click()
    except:
        return False

def activar_Sonido():
    try:
        Estado = driver.find_element(By.CSS_SELECTOR, "button[data-title-no-tooltip='Activar sonido']")

        if Estado:
            activa_Sonido = driver.find_element(By.CSS_SELECTOR, ".ytp-mute-button")
            activa_Sonido.click()
    except:
        return False

def valida_patrocinado():
    try:
        elemento_patrocinado = driver.find_element(By.CSS_SELECTOR, ".ad-simple-attributed-string")
        if elemento_patrocinado.is_displayed():
            return True
    except:
        return False  

def saltar_patrocinado():
    button = driver.find_element(By.CSS_SELECTOR, ".ytp-skip-ad-button")
    if button.is_displayed():
        button.click()
        return True
    else: 
        return False 

def guardar_log():
    ftFecha = datetime.datetime.now().strftime("%d/%m/%Y %I:%M %p")
    logging.info(f'{contador} Anuncio Omitido. {ftFecha}')

def button_Play():
    try:     
        Button_Play = driver.find_element(By.CLASS_NAME, "ytp-play-button")
        if Button_Play.is_displayed():
            Button_Play.click()
    except:
        return False


while True:
    try:  
        if valida_patrocinado():
            sileciar_patrocinado() 
            if saltar_patrocinado():
                contador += 1
                guardar_log()  
        else:
            activar_Sonido()       
    except: 
        continue
