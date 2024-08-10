import requests
from bs4 import BeautifulSoup

def coletar_partidas_time(liga_selecionada):
    #https://www.soccerstats.com/latest.asp?league=
    session = requests.session()

    jogos_liga = session.get(f'https://www.soccerstats.com/latest.asp?league=australia4')

    jogos_html = BeautifulSoup(jogos_liga.text,'html.parser')

    print(jogos_liga)
    jogos_links = jogos_html.find_all('//div[4]/table[1]/tbody/tr/td/table[1]//tr/td/a[@class="vsmall"]')

    return jogos_links