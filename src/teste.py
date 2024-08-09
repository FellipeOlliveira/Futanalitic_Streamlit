import requests
import bs4

def requisicao_test() -> str:
    test = requests.get('https://www.google.com.br/')
    result = test.status_code
    if result == 200:
        return 'Sucesso'
    elif result == 404:
        return 'Deu Errado'

    else:
        return 'Ai é foda'