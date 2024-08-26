import requests
from engine import data_coletor , link_coletor
from lxml import etree
from lxml.html import fromstring

class Casa:

    def __init__(self,jogo):
        self.jogo = jogo
        self.session = requests.session()
        self.conteudo_html = self.__extrair_conteudo_html(self.session,self.jogo)
        self.tbl_scoring_rate = self.__extrair_scoring_rate(self.conteudo_html)

    def __extrair_conteudo_html(self , session ,jogo):
        requisicao = session.get(jogo)

        content = requisicao.text

        return content

    def __extrair_scoring_rate(self, content):
        dom = fromstring(content)

        tables = dom.xpath("//div[3]/div[3]/div[2]/table")

        for table in tables:
            # Encontre todas as linhas dentro da tabela
            rows = table.xpath('.//tr')
            for row in rows:
                # Encontre todas as células na linha
                cells = row.xpath('.//td|.//th')
                cell_texts = [cell.text_content().strip() for cell in cells]
                print(cell_texts)
            print('---')