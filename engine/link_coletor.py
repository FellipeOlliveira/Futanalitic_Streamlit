import requests
from lxml import etree

def coletar_partidas_time(liga_selecionada):
    #https://www.soccerstats.com/latest.asp?league=
    session = requests.session()

    jogos_liga = session.get(f'https://www.soccerstats.com/latest.asp?league={liga_selecionada}')

    parser = etree.HTMLParser()
    tree = etree.fromstring(jogos_liga.content, parser)

    link_table = tree.xpath('//table[1]//tr//td//table[@id="btable"]')

    if len(link_table) == 0:
        return 'Não Ha partidas nesse periodo'
    if len(link_table) == 1:
        return 'Ja houve partidas nesses periodo'
    else:
        links_partidas = tree.xpath('//table[1]//tr//td//table[@id="btable"][1]//td//a[@class ="vsmall"]/@href')
        links_partidas = list(map(lambda links: r"https://www.soccerstats.com/" + links, links_partidas))
        return links_partidas