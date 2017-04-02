from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
'''
Copyright by Nicola Iacovelli 2017
Tutti i diritti sono riservati
'''

sito = "http://prenotacolloqui.altervista.org"      # Sito da testare
chrome = webdriver.Chrome()     # Apro Chrome
chrome.get(sito)                # Richiedo il sito
tempoiniziale = time.time()     # Ottengo il tempo iniziale
print("Tempo iniziale:"+str(tempoiniziale))     # Stampo il tempo iniziale
f = open('biennio.txt', 'r')    # Apro il file con i codici degli alunni
codici = [x for x in f.readlines()]  # Ottengo tutti i codici
f.close()       # Chiudo il file
i = 1
for x in codici:
    codice = int(x)     # Prendo un codice
    inputElement = chrome.find_element_by_id("inp")     # Identifica la casella di testo
    inputElement.send_keys(codice)      # Inserisce il codice nella casella di testo
    inputElement = chrome.find_element_by_id("sub")     # Identifica il bottone login
    inputElement.click()        # Effettua il login
    time.sleep(3)       # Aspetta che la pagina venga caricata
    inputElement = chrome.find_element_by_id("conferma")  # Identifica il bottone conferma prenotazione
    inputElement.click()        # Conferma prenotazione
    try:
        WebDriverWait(chrome, 5).until(EC.alert_is_present(), 'Timed out')
        alert = chrome.switch_to.alert.accept()
        print("Già prenotato")
    except TimeoutException:
        print("Sto prenotando")
    time.sleep(4)       # Aspetta che la pagina venga caricata
    inputElement = chrome.find_element_by_id("lgo")     # Identifica il bottone di logout
    inputElement.click()        # Effettua il logout
    try:
        WebDriverWait(chrome, 5).until(EC.alert_is_present(), 'Timed out')
        alert = chrome.switch_to.alert.dismiss()
        print("Logout effettuato")
    except TimeoutException:
        print("No alert")
    print("Ho prenotato il "+str(i)+"° alunno con codice: "+x)
    i += 1
    time.sleep(3)       # Aspetta che venga ricaricato l'index
tempofinale = time.time()       # Ottengo il tempo finale
print("Tempo finale: "+str(tempofinale))        # Stampo il tempo iniziale
print("Lo script ha impiegato "+str(tempofinale-tempoiniziale)+" secondi")  # Stampo il tempo di esecuzione dello script
chrome.close()      # Chiude il browser
