import requests

def busca_autor(autor):
    url = f'http://localhost:5000/autores/{autor}'
    response = requests.get(url)

    print(response.content)

if __name__ == '__main__':
    while True:
        autor = input('Qual autor deseja pesquisar? ')
        busca_autor(autor)
        resposta = input('Deseja continuar pesquisando? (s/n) ')
        if resposta.lower() == 'n':
            break
        
        