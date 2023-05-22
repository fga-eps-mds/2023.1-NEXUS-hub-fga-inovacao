import requests
from bs4 import BeautifulSoup
import csv

def obter_informacoes(url, div, clas, indice, titulo):
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}

    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')

    equipe = soup.find(div , clas)
    paragrafos = equipe.find_all('p')

    # Verifica se o índice é válido
    if indice < len(paragrafos):
        informacao = paragrafos[indice].get_text(strip=True)
    else:
        informacao = 'Índice inválido'

    return titulo, informacao

#Titans
urlTitans = 'http://eletronica.unb.br/organizacoes/equipes'
divTitans= 'div'  # Substitua pela classe correta
clasTitans = 'item-page'
indiceTitans = 4  # Substitua pelo índice desejado
titulo = 'Titans'

Titans = obter_informacoes(urlTitans, divTitans, clasTitans, indiceTitans, titulo)

#FGR
urlFGR = 'http://automotiva.unb.br/extensao/projeto-formula-sae-eletrico'
divFGR= 'div'  # Substitua pela classe correta
clasFGR = 'item-page'
indiceFGR = 0 # Substitua pelo índice desejado
titulo = 'FGR'

Fgr = obter_informacoes(urlFGR,divFGR,clasFGR,indiceFGR, titulo)

#baja
urlbaja = 'http://automotiva.unb.br/extensao/projeto-unbaja'
divbaja = 'div'  # Substitua pela classe correta
clasbaja = 'item-page'
indicebaja = 1 # Substitua pelo índice desejado
titulo = 'UNBAJA'

baja = obter_informacoes(urlbaja,divbaja,clasbaja,indicebaja, titulo)

#edra

urledra = 'https://fga.unb.br/aeroespacial/equipes'
divedra = 'div'  # Substitua pela classe correta
clasedra = 'article-body article-body-text-article'
indiceedra = 22 # Substitua pelo índice desejado
titulo = 'Equipe de Robótica Aerea(EDRA)'

edra = obter_informacoes(urledra,divedra,clasedra,indiceedra, titulo)

#mamutes

urlmamutes = 'https://fga.unb.br/aeroespacial/equipes'
divmamutes = 'div'  # Substitua pela classe correta
clasmamutes = 'article-body article-body-text-article'
indicemamutes = 4 # Substitua pelo índice desejado
titulo = 'Mamutes do Cerrado'

mamutes = obter_informacoes(urlmamutes,divmamutes,clasmamutes,indicemamutes, titulo)

#Capital

urlcapital = 'https://fga.unb.br/aeroespacial/equipes'
divcapital = 'div'  # Substitua pela classe correta
clascapital = 'article-body article-body-text-article'
indicecapital = 13 # Substitua pelo índice desejado
titulo = 'Capital Rocket Team'

capital = obter_informacoes(urlcapital,divcapital,clascapital,indicecapital, titulo)

#cube design

urlcube = 'https://gamacubedesign.wixsite.com/website'
divcube = 'div'  # Substitua pela classe correta
clascube = 'BaOVQ8 tz5f0K comp-kkvrtq9t wixui-rich-text'
indicube = 0 # Substitua pelo índice desejado
titulo = 'Gama Cube Design'

cube = obter_informacoes(urlcube,divcube,clascube,indicube, titulo)



# Nome do arquivo CSV
nome_arquivo = 'equipes.csv'

# Abre o arquivo CSV para escrita
with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
    writer = csv.writer(arquivo_csv)

    # Escreve o cabeçalho do CSV
    writer.writerow(['Equipes'])

    # Escreve a informação coletada
    writer.writerow([Titans])
    writer.writerow([Fgr])
    writer.writerow([baja])
    writer.writerow([edra])
    writer.writerow([mamutes])
    writer.writerow([capital])   
    writer.writerow([cube])


print(f'Dados armazenados no arquivo CSV: {nome_arquivo}')
