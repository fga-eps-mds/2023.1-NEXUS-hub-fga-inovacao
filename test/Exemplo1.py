from webScraping.Professores import teste1

def test_textos_titulos_paragrafos():

    page_content = teste1.get_page_content()
    
    
    paragraphs = page_content.get('paragraphs', [])
    

    for paragraph in paragraphs:
        assert 'title' in paragraph, "Paragraph doesn't have a title."
        assert 'content' in paragraph, "Paragraph doesn't have content."
