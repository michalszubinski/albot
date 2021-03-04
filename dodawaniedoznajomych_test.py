from albot_core import *

browser = webdriver.Chrome(ChromeDriverManager().install())
    
lista_znajomych = list()
Logowanie(browser,G_login,G_haslo)
DodajZnajomego(browser,"KurtCobain")
