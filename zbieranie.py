from albot_core import *

browser = webdriver.Chrome(ChromeDriverManager().install())
    
lista_znajomych = list()
Logowanie(browser,G_login,G_haslo)
Matryoshka(browser,G_pierwszaosoba,lista_znajomych,G_folderznajomych)
