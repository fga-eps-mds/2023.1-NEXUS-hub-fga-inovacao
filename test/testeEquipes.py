import pytest
import requests
from bs4 import BeautifulSoup

def obter_informacoes_Equipes(url, div, clas, indice, titulo, link):
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

    return titulo, informacao, link


def test_obter_informacoes_Equipes():
    # Configuração do cenário de teste
    div = 'div'
    clas = 'item-page'
    indice = 4
    titulo = 'Titans'
    link = 'https://www.instagram.com/robotictitans/'

    # Chama a função a ser testada
    testeInformacoes = obter_informacoes_Equipes(div, clas, indice, titulo, link)

    # Verificação dos resultados
    resultadoEsperado =('Titans', 'AEquipe de robótica Titansé um projeto que foi criado na FGA em 2016. Tem o objetivo de colocar em prática os conhecimentos do curso de Engenharia Eletrônica por meio de projetos e da criação de robôs para competição, incluindo robôs autônomos e/ou controlados. No ano de 2019, participamos da competição Winter Challenge XV 2018, nos apresentamos na Campus Party Brasília 2019 e apresentamos a equipe e a FGA na escola CEM 01 Guará. Além de que durante a pandemia, oferecemos consultoria para realização de um robô alvo para policiais militares.', 'https://www.instagram.com/robotictitans/')

    assert testeInformacoes == resultadoEsperado
# Executa o teste
pytest.main()
