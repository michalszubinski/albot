from albot_core import *

browser = webdriver.Chrome(ChromeDriverManager().install())
    
lista_znajomych = list()
Logowanie(browser,G_login,G_haslo)
lista_znajomych = WczytajZnajomych("GIT2.txt",G_folderznajomych)
lista_znajomych = ZmienKolejnosc(lista_znajomych)
DodajZnajomychZListy(browser,lista_znajomych)
