import requests

def fetch_page(url):
    response = requests.get(url)  # Realiza a requisição HTTP para obter o conteúdo da página, retorna 200 se bem sucedido
    return response.text  # Retorna o HTML da página, em texto

# Teste da função
if __name__ == '__main__':
    url_1 = 'https://www.mercadolivre.com.br/apple-iphone-16-pro-1-tb-titnio-preto-distribuidor-autorizado/p/MLB1040287851#polycard_client=search-nordic&wid=MLB5054621110&sid=search&searchVariation=MLB1040287851&position=6&search_layout=stack&type=product&tracking_id=92c2ddf6-f70e-475b-b41e-fe2742459774'
    url_2 = 'https://www.mercadolivre.com.br/fritadeira-sem-oleo-air-fryer-4l-afn-40-bi-mondial-pretoinox-1500w/p/MLB19635464?pdp_filters=item_id:MLB5166667738#wid=MLB5166667738&sid=search&is_advertising=true&searchVariation=MLB19635464&position=1&search_layout=stack&type=pad&tracking_id=77f9e731-3bda-4ae7-95e8-c96eb9395be0&is_advertising=true&ad_domain=VQCATCORE_LST&ad_position=1&ad_click_id=N2FlNjA2YzUtMzg2Zi00NzFkLWJlMjItN2JlMTBhOTEyMWE3'
    page_content_1 = fetch_page(url_1)
    page_content_2 = fetch_page(url_2)
    print(page_content_1)  # Mostra os primeiros 500 caracteres do HTML
    print(page_content_2)  # Mostra os primeiros 500 caracteres do HTML
