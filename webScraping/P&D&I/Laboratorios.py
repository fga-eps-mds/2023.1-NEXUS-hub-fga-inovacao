import requests
from bs4 import BeautifulSoup
import csv

def obter_informacoes(div, clas, indice, titulo, link):
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}

url = 'https://fga.unb.br/unb-gama/laboratorios'
site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')

labs = soup.find_all('div', class_='article-body article-body-text-article')
paragrafos = equipe.find_all('p')

#Introdução
divIntrodução = 'div' 
classIntrodução = 'article-body article-body-text-article'
indiceIntrodução = 0
titulo = 'Introdução'
link = ''

Introdução = obter_informacoes(divIntrodução, classIntrodução, indiceIntrodução, titulo, link)

#Fábrica de Software
divSoftware = 'div'
classSoftware = 'article-body article-body-text-article'
indiceSoftware = 3
titulo = 'Fabrica de Software'
link = ''

Software = obter_informacoes(divSoftware, classSoftware, indiceSoftware, titulo, link):

#LabNVH
divNVH = 'div'
classNVH = 'article-body article-body-text-article'
indiceNVH = 5
titulo = 'LabNVH'
link = ''

NVH = obter_informacoes(divNVH, classNVH, indiceNVH, titulo, link):

#Lappis
divLappis = 'div'
classLappis = 'article-body article-body-text-article'
indice = 7
titulo = 'Lappis'
link = ''

Lappis = obter_informacoes(divLappis, classLappis, indice, titulo, link):

#LART
divLart = 'div'
classLart = 'article-body article-body-text-article'
indiceLart = 9
titulo = 'LART'
link = ''

LART = obter_informacoes(divLart, classLart, indiceLart, titulo, link):

#LEI
divLei = 'div'
classLei = 'article-body article-body-text-article'
indiceLei = 11
titulo = 'LEI'
link = ''

LEI = obter_informacoes(divLei, classLei, indiceLei, titulo, link):

# Nome do arquivo CSV
nome_arquivo = 'labs.csv'

# Abre o arquivo CSV para escrita
with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    
    # Itera sobre as divs encontradas
    for lab in labs:
        texto = lab.get_text(strip=True)
        
        # Escreve o texto da div em uma nova linha no arquivo CSV
        writer.writerow([texto])

print(f'Dados armazenados no arquivo CSV: {nome_arquivo}')
