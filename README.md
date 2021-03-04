# albot
v1.0.0 - 11 luty 2021

Aby prawidlowo otworzyc bota, nalezy:

1. Zainstalowac Python (ZAZNACZYC PRZY INSTALLACJI "ADD TO PATH"!!! - ekstremalnie wazne)
2. Zainstalowac przez cmd windowsa (wpisac po prostu tam komende):

pip3 install selenium webdriver_manager

3. Zainstalowac Google Chrome oraz ChromeDriver (https://chromedriver.chromium.org/downloads),
nalezy wybrac pod odpowiednia wersje Chrome (chrome://settings/help)
4. Zmodyfikowac albot_settings.py swoimi danymi

Zalecam odpalac przez IDLE (bo ja tak robie i mi dziala).

Objasnienie:

G_nick - Obecnie nie uzywane, jest to nazwa profilu
G_login - Mail konta
G_haslo - Haslo konta
G_folderznajomych - Folder do zapisu nazw kont (mozna pominac)
G_pierwszaosoba - Nick osoby od ktorej ma zaczac sie poszukiwanie znajomych

5. Wykorzystac ktorys z gotowych skryptow

*******************
zbieranie.py

Nalezy upewnic sie czy folder domyslnie nazwany (G_folderznajomych) "znajomi" jest utworzony w katalogu ze skryptami.


Aby wczytac poprzednia liste, nalezy zmodyfikowac skrypt, a mianowicie przyrownac liste znajomych na samym poczatku do funkcji wczytywania.
Np.
zamiast
lista_znajomych = list()
wpisac
lista_znajomych = WczytajZnajomych("GIT.txt",G_folderznajomych)


*******************
dodawanie.py

Domyslnie dodawani sa ludzie z pliku GIT.txt, mozna to zmienic w linijce:

lista_znajomych = WczytajZnajomych("GIT.txt",G_folderznajomych)

Wystarczy zmienic zawartosc cudzyslowia (pamietac o .txt !!!!!!).

******************
Tworzenie wlasnych skryptow: opis funkcji


Wazne funckje:
Logowanie(browser,login,haslo)
Loguje do portalu.

SourceCodeDoListyZnajomych(source_code)
Zmienia source code strony z lista znajomych na liste osob.

ZapiszZnajomych(lista_znajomych,LISTY)
Zapisuje liste osob to txt.

WczytajZnajomych(FILENAME,G_folderznajomych)
Wczytuje liste osob z txt.

ListaZnajomych_JednaOsoba(browser,nazwa_konta, duza_lista_znajomych, lokacja_list)
Zbiera osoby z listy znajomych danej osoby do txt.

ListaZnajomych_Lista(browser,lista_znajomych, duza_lista_znajomych, lokacja_list)
Zbiera osoby z list znajomych osob zawartych w liscie do pliku txt. 

DodajZnajomego(browser,nick)
Dodaje pojedynczego znajomego.

DodajZnajomychZListy(browser,lista)
Dodaje cala liste znajomych.

Matryoshka(browser,pacjent_zero, lista_znajomych, lokacja_list)
Zapetla sie i caly czas zbiera nowe osoby, zeby przejzec ich listy.

Utility:
ZmienKolejnosc(lista)
Shuffluje liste.

UsunPodobienstwa(test_list)
Zwraca liste z usunietymi wyrazy ktore sie powtarzaja.

OdejmowanieList(a,b)
Zwraca liste z wyrazami, ktorych nie ma w liscie b.
