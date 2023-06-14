import pytest
import requests
from bs4 import BeautifulSoup

def obter_informacoes_Ejs(div, clas, indice, titulo, link):
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

def test_obter_informacoes_Ejs():
    # Configuração do cenário de teste
    div = 'div'
    clas = 'article-body article-body-text-article'
    indice = 0
    titulo = 'Introdução'
    link = ''

    # Chama a função a ser testada
    testeInformacoes = obter_informacoes_Ejs(div, clas, indice, titulo, link)

    # Verificação dos resultados
    resultadoEsperado = ('Introdução', 'Uma Empresa Júnior consiste em uma associação com fins educacionais formada exclusivamente por alunos de ensino superior ou técnico.\xa0Estas empresas auxiliam na formação de nossos alunos oferecendo-lhes a oportunidade de adquirir experiência profissional em tempo de graduação, contribuindo em uma melhor preparação destes para o mercado de trabalho.', '')
    assert testeInformacoes == resultadoEsperado
    
# Executa o teste
pytest.main()
