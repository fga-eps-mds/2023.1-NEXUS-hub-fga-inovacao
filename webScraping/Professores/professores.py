import requests
from bs4 import BeautifulSoup
import csv

url = "https://sigaa.unb.br/sigaa/public/departamento/professores.jsf?id=673"
site = requests.get(url)
soup = BeautifulSoup(site.content, 'html.parser')

# Dados para a tabela
dados = [
    ['Nome', 'Imagem', 'Pagina', 'Projetos de pesquisa', 'Projetos de extensão', 'Disciplinas ministradas']
]

#Função de conserto de strings
def conserto_strings(str1):
    if str1 != 'https':
        str1 ='https://sigaa.unb.br'+str1    
    return str1

# Nome do arquivo CSV
nome_arquivo = 'professores.csv'

# Abrir o arquivo CSV em modo de escrita
with open(nome_arquivo, 'w', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)

    escritor_csv.writerow(dados)

    # Escrever os dados na tabela
    for linha in dados:
        professores= soup.find('div', {'id': 'professores'})
        lista= professores.find_all('tr')

        for professor in lista:
            # Raspagem dos elementos da classe nome 
            nome = professor.find('span',class_='nome')
            # Retirada de tags e elementos não textuais
            nome = nome.get_text()
            # Retirada de newlines
            nome = nome.replace("\t", "").replace("\r", "").replace("\n", "")
            print(nome)

            # Raspagem das imagens dentro de tr
            imagens = professor.find('img')
            imagens = imagens['src']
            # Correção de links 
            imagens = conserto_strings(imagens)   
            print(imagens)          

            # Raspagem do link das paginas 
            pagina = professor.find('span',class_='pagina')
            pagina = pagina.find('a', href=True)['href']
            # Correção de links    
            pagina = conserto_strings(pagina) 
            print(pagina)

            # Scapring da pagina dos professores
            url2 = pagina
            site2 = requests.get(url2)
            soup = BeautifulSoup(site2.content, 'html.parser')

            # Link da pagina de projetos de pesquisa
            barra_professor = soup.find('div',class_='barra_professor')
            pagina_pesquisa = barra_professor.find('li',class_='projetos_pesquisa')
            pagina_pesquisa = pagina_pesquisa.find('a', href=True)['href']
            # Correção de links    
            pagina_pesquisa = conserto_strings(pagina_pesquisa) 
            print(pagina_pesquisa)

            # Link da pagina de atividades de extensão
            pagina_extensao = barra_professor.find('li',class_='projetos_extensao')
            pagina_extensao = pagina_extensao.find('a', href=True)['href']
            # Correção de links    
            pagina_extensao = conserto_strings(pagina_extensao) 
            print(pagina_extensao)

            # Link da pagina de disciplinas
            pagina_disciplinas = barra_professor.find('li', class_='disciplinas_ministradas')
            pagina_disciplinas = pagina_disciplinas.find('a', href=True)['href']
            # Correção de Links
            pagina_disciplinas = conserto_strings(pagina_disciplinas)
            print(pagina_disciplinas)

            # Scapring da pagina de projetos de pesquisa
            url3 = pagina_pesquisa
            site3 = requests.get(url3)
            soup = BeautifulSoup(site3.content, 'html.parser')

            projetos_pesquisa = soup.find('div',{'id':'pesquisa-docente'})
            projetos_pesquisa = projetos_pesquisa.get_text()
            projetos_pesquisa = projetos_pesquisa.replace("\t", " ").replace("\r", " ").replace("\n", " ")

            print(projetos_pesquisa)

            # Scraping da pagina de atividades de extensão
            url4 = pagina_extensao
            site4 = requests.get(url4)
            soup = BeautifulSoup(site4.content, 'html.parser')

            atividade_docente = soup.find('div',{'id':'atividade-docente'})
            projetos_coordenador = atividade_docente.get_text()
            projetos_coordenador = projetos_coordenador.replace("\t", " ").replace("\r", " ").replace("\n", " ")

            atividade_docente2 = atividade_docente.find_next('div')
            projetos_participa = atividade_docente2.get_text()
            projetos_participa = projetos_participa.replace("\t", " ").replace("\r", " ").replace("\n", " ")

            print(projetos_coordenador)
        
            print(projetos_participa)

            # Scraping da pagina de disciplinas
            url5 = pagina_disciplinas
            site5 = requests.get(url5)
            soup = BeautifulSoup(site5.content, 'html.parser')

            disciplinas_graduacao = soup.find('div',{'id':'turmas-graduacao'}) 
            disciplinas_graduacao = disciplinas_graduacao.get_text()
            disciplinas_graduacao = disciplinas_graduacao.replace("\t"," ").replace("\r", " ").replace("\n"," ")

            print(disciplinas_graduacao)
            print('\n')

            linha= nome, imagens, pagina, projetos_pesquisa, projetos_coordenador, projetos_participa, disciplinas_graduacao
            escritor_csv.writerow(linha)
print(f'Dados armazenados no arquivo CSV: {nome_arquivo}')