from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime
from playsound import playsound
from pyvirtualdisplay import Display
import yaml

display = Display(visible=0, size=(800, 600))
display.start()
count = 0
while True:
    browser = webdriver.Firefox()
    with open('config.yaml', "r") as file:
            try:
                databaseConfig = yaml.safe_load(file)   
                browser.get((databaseConfig["website"]))
                choise = (databaseConfig["website"])
            except yaml.YAMLError as exc:
                print(exc)  
            

    if choise == "https://shop.flipperzero.one/":
        soldOut = browser.find_element(By.XPATH, "/html/body/div[3]/main/div[2]/div/div/div[2]/div/div[1]/div[1]/dl/div[1]/div[3]/span[2]/span").text
        sito = "[SITO]"
    elif choise == "https://lab401.com/products/flipper-zero?_pos=6&_sid=2bdd63fb5&_ss=r&variant=42927883452646":
        soldOut = browser.find_element(By.CSS_SELECTOR, "#addToCartText-product-template") 
        sito = "[lab401]"
    else:
        print("Link errato. Verifica di averlo digitato correttamente come riportato sul config.YAML e di aver salvato il file con CTRL + S")

    if soldOut == "SOLD OUT":
        count+=1
        now = datetime.now()
        print(sito + "\n" + "NUM CONTROLLO: " + str(count) + "\n" + "Non è disponibile" + " " + "\n" "Data controllo: " + str(now) + "\n")
    else:
        print("Disponibile")
        playsound("Allerta.mp3")

        