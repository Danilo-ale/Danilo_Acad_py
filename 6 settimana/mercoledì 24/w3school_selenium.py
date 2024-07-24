"""
Visita https://www.w3schools.com/html/html_tables.asp
Estrai i dati dalla prima tabella sulla pagina e stampali in formato leggibile

"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

def setup_driver():
    driver=webdriver.Chrome()
    return driver

def dati_tab(driver):
    driver.get("https://www.w3schools.com/html/html_tables.asp")
    print(driver.title)
    time.sleep(1)
    button_privacy = driver.find_element(By.ID, "accept-choices")
    button_privacy.click()
    time.sleep(2)

    tabella=driver.find_element(By.XPATH,"/html/body/div[5]/div[1]/div[1]/div[3]/div/table")
    df_col=[]
    col=driver.find_element(By.XPATH,"/html/body/div[5]/div[1]/div[1]/div[3]/div/table/tbody/tr[1]/th[1]")
    df_col.append(col.text)

    col=driver.find_element(By.XPATH,"/html/body/div[5]/div[1]/div[1]/div[3]/div/table/tbody/tr[1]/th[2]")
    df_col.append(col.text)

    col=driver.find_element(By.XPATH,"/html/body/div[5]/div[1]/div[1]/div[3]/div/table/tbody/tr[1]/th[3]")
    df_col.append(col.text)
    print(df_col)
    riga_path="/html/body/div[5]/div[1]/div[1]/div[3]/div/table/tbody/tr["
    #/html/body/div[5]/div[1]/div[1]/div[3]/div/table/tbody/tr[2]
    #/html/body/div[5]/div[1]/div[1]/div[3]/div/table/tbody/tr[2]/td[1]
    #/html/body/div[5]/div[1]/div[1]/div[3]/div/table/tbody/tr[2]/td[3]
    #/html/body/div[5]/div[1]/div[1]/div[3]/div/table/tbody/tr[7]
    righe=[]
    for riga in range(2,8):
        riga_spec=f"{riga_path}{riga}]/td[1]"
        Company=driver.find_element(By.XPATH, riga_spec)
        riga_spec=f"{riga_path}{riga}]/td[2]"
        Contact=driver.find_element(By.XPATH, riga_spec)
        riga_spec=f"{riga_path}{riga}]/td[3]"
        Country=driver.find_element(By.XPATH, riga_spec)
        righe.append({"Company":Company.text, "Contact":Contact.text, "Country":Country.text})

    print(righe)
    df=pd.DataFrame(righe, columns=df_col)
    print(df)


driver=setup_driver()
dati_tab(driver)
