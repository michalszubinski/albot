from albot_settings import G_nick,G_login,G_haslo,G_folderznajomych,G_pierwszaosoba
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import date
import random
#import numpy as np


def Logowanie(browser,login,haslo):
    browser.get("https://albicla.com/login")
    # Fill credentials
    browser.find_element_by_name("email").send_keys(login)
    browser.find_element_by_name("pass").send_keys(haslo)
    # Click Log In
    browser.find_element_by_name("signin").click();

def SourceCodeDoListyZnajomych(source_code):
    
    lista_znajomych = list()

    if '<h5 class="mb-1 mt-1"><b><a href="/' in source_code:
        test = source_code.split('<h5 class="mb-1 mt-1"><b><a href="/')
        #print(test)
        lista_len = len(test)
        print(str(lista_len))
        test.pop(lista_len-1)
        
        for line in test:
            new_line=line.split('"')[0]

            if new_line != '<html class=':
                lista_znajomych.append(new_line)
                #ilosc_znajomych +=1
                #print("ZNALEZIONO: ",new_line)

    return lista_znajomych
    

def UsunPodobienstwa(test_list):
    res = [i for n, i in enumerate(test_list) if i not in test_list[:n]]
    return res

def OdejmowanieList(a,b):
    for x in b:
        a.remove(x)
    return a

def ZapiszZnajomych(lista_znajomych,LISTY):
	today = date.today()
	d3 = today.strftime("%d%m%y")
	t = time.localtime()
	current_time = time.strftime("%H%M%S", t)
	filename=d3+" "+current_time+".txt"
	f = open(LISTY+"/"+filename, "w", encoding="utf-8")
	linebuf=""
	ppl=0
	for x in lista_znajomych:
		f.write(x)
		f.write("\n")
		ppl+=1
	print(str(ppl)+" ZAPISANYCH ZNAJOMYCH")
	f.close()

def WczytajZnajomych(FILENAME,G_folderznajomych):
    
	linelist = list()
	ppl=0
	
	file = open(G_folderznajomych+"/"+FILENAME, "r", encoding="utf-8")
	for x in file:
		#print(x)
		#x=x.split("\n")[0]
		linelist.append(x)
		ppl += 1
	file.close()

	print(str(ppl)," - LICZBA OSOB WCZYTANYCH Z ",FILENAME)

	return linelist
    
def ListaZnajomych_JednaOsoba(browser,nazwa_konta, duza_lista_znajomych, lokacja_list):
    url = "https://albicla.com/"+str(nazwa_konta)+"/znajomi"

    # Open the Website
    browser.get(url)
    lista_znajomych = list()

    source_code = browser.page_source
    lista_znajomych = SourceCodeDoListyZnajomych(source_code)

    nowa_lista_znajomych = duza_lista_znajomych + lista_znajomych
    nowa_lista_znajomych = UsunPodobienstwa(nowa_lista_znajomych)

    ZapiszZnajomych(nowa_lista_znajomych,lokacja_list)

    return nowa_lista_znajomych

def ListaZnajomych_Lista(browser,lista_znajomych, duza_lista_znajomych, lokacja_list):
    nowa_lista_znajomych = lista_znajomych

    for osoba in lista_znajomych:
        nowa_lista_znajomych = ListaZnajomych_JednaOsoba(browser,osoba,nowa_lista_znajomych,lokacja_list)

    return nowa_lista_znajomych

def DodajZnajomego(browser,nick):
    url = "https://albicla.com/"+str(nick)
    browser.get(url)

    source = browser.page_source

    if 'Profil tymczasowo niedost' in source:
        print("[INFO] DODAWNIE ZNAJOMYCH: NIE MOZNA DODAC OSOBY ZBANOWANEJ: ",nick)
    else:
        if 'data-action="add"' in source:
            #print("in")
            browser.find_element_by_xpath('//button[@data-action="add"]').click();
        else:
            print("[INFO] DODAWNIE ZNAJOMYCH: DODANY LUB NIE MOZNA DODAC: ",nick)

def DodajZnajomychZListy(browser,lista):
    for osoba in lista:
        DodajZnajomego(browser,osoba)

def ZmienKolejnosc(lista):
    return random.shuffle(lista)


def Matryoshka(browser,pacjent_zero, lista_znajomych, lokacja_list):
    
    poprzednia_lista = list()
    poprzednia_lista.append(pacjent_zero)
    lista_znajomych = list()
    lista_znajomych = poprzednia_lista

    lista_znajomych = ListaZnajomych_JednaOsoba(browser,pacjent_zero, lista_znajomych, lokacja_list)

    nowi_znajomi = list()

    while 1:
        poprzednia_lista_znajomych = lista_znajomych
        nowi_znajomi = OdejmowanieList(lista_znajomych,poprzednia_lista)
        #print(nowi_znajomi)
        
        for osoba in nowi_znajomi:
            lista_znajomych = ListaZnajomych_JednaOsoba(browser,osoba, lista_znajomych, lokacja_list)
            
