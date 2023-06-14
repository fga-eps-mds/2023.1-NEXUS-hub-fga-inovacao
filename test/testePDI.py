from bs4 import BeautifulSoup
import requests
import pytest


def obter_informacoes_PDI(div, clas, indice, titulo):
    url = 'https://fga.unb.br/unb-gama/laboratorios'
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}

    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')

    labs = soup.find(div, clas)
    paragrafos = labs.find_all('p')

    if indice < len(paragrafos):
        informacao = paragrafos[indice].get_text(strip=True)
    else:
        informacao = 'Índice inválido'

    return titulo, informacao


def test_obter_informacoes_PDI():
    div = 'div'
    clas = 'article-body article-body-text-article'
    indice = 3
    titulo = 'Introducao'

    resultado_esperado = ('Introdução',
                          'Como nosso Campus possui uma série de cursos voltados para as áreas de engenharia, é muito importante para uma\xa0melhor experiência dentro da graduação que seus alunos possuam uma experiência atuando em seus campos de interesse.')

    assert obter_informacoes_PDI(div, clas, indice, titulo) == resultado_esperado

pytest.main()