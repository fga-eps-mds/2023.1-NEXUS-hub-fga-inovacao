import requests
from bs4 import BeautifulSoup
import csv

def obter_informacoes(div, clas, indice, titulo, link):
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
   
    url = 'https://fga.unb.br/unb-gama/empresas-juniores'
    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')

    empresasJuniores = soup.find(div , clas)
    paragrafos = empresasJuniores.find_all('p')

    # Verifica se o índice é válido
    if indice < len(paragrafos):
        informacao = paragrafos[indice].get_text(strip=True)
    else:
        informacao = 'Índice inválido'

    return titulo, informacao, link

#Introdução
divIntrodução = 'div' 
classIntrodução = 'article-body article-body-text-article'
indiceIntrodução = 0
titulo = 'Introdução'
link = ''

Introdução = obter_informacoes(divIntrodução, classIntrodução, indiceIntrodução, titulo, link)

#Eletronjun
divEletronjun = 'div'
classEletronjun = 'article-body article-body-text-article'
indiceEletronjun = 3
titulo = 'Eletronjun'
link = ''

Eletronjun = obter_informacoes(divEletronjun, classEletronjun, indiceEletronjun, titulo, link)

#Orc'estra
divOrc = 'div'
classOrc = 'article-body article-body-text-article'
indiceOrc = 5
titulo = 'Orcestra'  
link = ''

Orc = obter_informacoes(divOrc, classOrc, indiceOrc, titulo, link)

#Matriz Energia
divMatriz = 'div'
classMatriz = 'article-body article-body-text-article'
indiceMatriz = 7
titulo = 'Matriz Energia'
link = ''

Matriz = obter_informacoes(divMatriz, classMatriz, indiceMatriz, titulo, link)

#Zenit Aerospace
divZenit = 'div'
classZenit = 'article-body article-body-text-article'
indiceZenit = 9
titulo = 'Zenit Aerospace'
link = ''

Zenit = obter_informacoes(divZenit, classZenit, indiceZenit, titulo, link)

#Engrena
divEngrena = 'div'
classEngrena = 'article-body article-body-text-article'
indiceEngrena = 11
titulo = 'Engrena'
link = ''

Engrena = obter_informacoes(divEngrena, classEngrena, indiceEngrena, titulo, link)

# Nome do arquivo CSV
nome_arquivo = 'EJs.csv'

# Abre o arquivo CSV para escrita
with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
    writer = csv.writer(arquivo_csv)
        
    # Escreve o texto da div em uma nova linha no arquivo CSV
    writer.writerow([Introdução])
    writer.writerow([Eletronjun])
    writer.writerow([Orc])
    writer.writerow([Matriz])
    writer.writerow([Zenit])
    writer.writerow([Engrena])
    

print(f'Dados armazenados no arquivo CSV: {nome_arquivo}')
