import requests
from bs4 import BeautifulSoup
import csv

url = 'https://fga.unb.br/unb-gama/empresas-juniores'

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')

labs = soup.find_all('div', class_='article-body article-body-text-article')

# Nome do arquivo CSV
nome_arquivo = 'EJs.csv'

# Abre o arquivo CSV para escrita
with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    
    # Itera sobre as divs encontradas
    for lab in labs:
        texto = lab.get_text(strip=True)
        
        # Escreve o texto da div em uma nova linha no arquivo CSV
        writer.writerow([texto])

print(f'Dados armazenados no arquivo CSV: {nome_arquivo}')
