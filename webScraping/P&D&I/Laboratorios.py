import requests
from bs4 import BeautifulSoup
import csv

def obter_informacoes(div, clas, indice, titulo):
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}

    url = 'https://fga.unb.br/unb-gama/laboratorios'
    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')

    labs = soup.find(div , clas)
    paragrafos = labs.find_all('p')
    
    # Verifica se o índice é válido
    if indice < len(paragrafos):
        informacao = paragrafos[indice].get_text(strip=True)
    else:
        informacao = 'Índice inválido'

    return titulo, informacao

#Introdução
divIntrodução = 'div' 
classIntrodução = 'article-body article-body-text-article'
indiceIntrodução = 0
titulo = 'Introdução'

Introdução = obter_informacoes(divIntrodução, classIntrodução, indiceIntrodução, titulo)

#Fábrica de Software
divSoftware = 'div'
classSoftware = 'article-body article-body-text-article'
indiceSoftware = 3
titulo = 'Fabrica de Software'

Software = obter_informacoes(divSoftware, classSoftware, indiceSoftware, titulo)

#LabNVH
divNVH = 'div'
classNVH = 'article-body article-body-text-article'
indiceNVH = 5
titulo = 'LabNVH'

nvh = obter_informacoes(divNVH, classNVH, indiceNVH, titulo)

#Lappis
divLappis = 'div'
classLappis = 'article-body article-body-text-article'
indice = 7
titulo = 'Lappis'

Lappis = obter_informacoes(divLappis, classLappis, indice, titulo)

#LART
divLart = 'div'
classLart = 'article-body article-body-text-article'
indiceLart = 9
titulo = 'LART'

lart = obter_informacoes(divLart, classLart, indiceLart, titulo)

#LEI
divLei = 'div'
classLei = 'article-body article-body-text-article'
indiceLei = 11
titulo = 'LEI'

lei = obter_informacoes(divLei, classLei, indiceLei, titulo)

# Nome do arquivo CSV
nome_arquivo = 'labs.csv'

# Abre o arquivo CSV para escrita
with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    
    writer.writerow([Introdução])
    writer.writerow([Software])
    writer.writerow([nvh])
    writer.writerow([Lappis])
    writer.writerow([lart])
    writer.writerow([lei])
    writer.writerow([lart])
    

print(f'Dados armazenados no arquivo CSV: {nome_arquivo}')
