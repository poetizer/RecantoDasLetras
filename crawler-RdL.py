#coding: utf-8
import requests
from bs4 import BeautifulSoup

def get_urls(url):
        urls = []
        r = requests.get(url)

        soup = BeautifulSoup(r.text, 'lxml')

        pagina_atual = soup.find_all('table', class_='indice-conteudo')
        url = 'https://www.recantodasletras.com.br'
        for tabela_urls in pagina_atual:
                lista_a = tabela_urls.find_all('a')
                for name in lista_a:
                        urls.append('{0}{1}'.format(url, name.get('href')))
        return urls

def get_poesia(url):
        r = requests.get(url)

        soup = BeautifulSoup(r.text, 'lxml')

        poesia_Nt = soup.find_all(class_='breakword')
        poesia_Tt = []
        for poesia in poesia_Nt:
                poesia_Tt.append(poesia.get_text())
        poesia_Tt.append('\n')
        return poesia_Tt

url_raiz = 'https://www.recantodasletras.com.br/quadras'
for i in range(1,100):
        pag_url = '{0}{1}'.format(url_raiz, '/?pag=' + str(i))
        urls_poesia = get_urls(pag_url)
        for url in urls_poesia:
                poesias = get_poesia(url)
                for poesia in poesias:
                        arquivo = open('quadras.txt', 'a')
                        arquivo.write(poesia.encode('utf-8') + '\n')
                        arquivo.close()
