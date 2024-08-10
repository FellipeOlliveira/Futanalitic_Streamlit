import requests

def requisicao_test() -> str:
    test = requests.get('https://www.google.com.br/')
    result = test.status_code
    if result == 200:
        #content = BeautifulSoup(test.content,'html.parser')
        return 'Sucesso'
    elif result == 404:
        return 'Deu Errado'

    else:
        return 'Ai é foda'