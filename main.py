from selenium import webdriver
import time


sito = "http://prenotacolloqui.altervista.org"      # Sito da testare
chrome = webdriver.Chrome()     # Apro Chrome
chrome.get(sito)                # Richiedo il sito
f = open('biennio.txt', 'r')    # Apro il file con i codici degli alunni
codici = [x for x in f.readlines()]  # Ottengo tutti i codici
f.close()       # Chiudo il file
for x in codici:
    codice = int(x)     # Prendo un codice
    inputElement = chrome.find_element_by_id("inp")     # Identifica la casella di testo
    inputElement.send_keys(codice)      # Inserisce il codice nella casella di testo
    inputElement = chrome.find_element_by_id("sub")     # Identifica il bottone login
    inputElement.click()        # Effettua il login
    time.sleep(5)       # Aspetta che la pagina venga caricata
    inputElement = chrome.find_element_by_id("conferma")  # Identifica il bottone conferma prenotazione
    inputElement.click()        # Conferma prenotazione
    time.sleep(5)       # Aspetta che la pagina venga caricata
    inputElement = chrome.find_element_by_id("lgo")     # Identifica il bottone di logout
    inputElement.click()        # Effettua il logout
    time.sleep(5)       # Aspetta che venga ricaricato l'index
chrome.close()      # Chiude il browser
