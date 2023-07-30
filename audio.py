import requests
from bs4 import BeautifulSoup
import pandas as pd

class Audio:
    def __init__(self, opcao):
        self.opcao = opcao

    def format_price(self, price):
        # Implemente sua lógica para formatar o preço aqui, se necessário
        return price

    def audio(self):
        if self.opcao.lower() == 'audio':
            base_url = 'https://www.magazinevoce.com.br/magazinemocelinn/audio/l/ea/'
            headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
            
            res = requests.get(base_url, headers=headers)
            soup = BeautifulSoup(res.content, 'html.parser')
            
            dados_h2 = soup.find_all('div', attrs={'data-testid': 'product-card-content'})
            dados_link = soup.find_all('li', class_='sc-gQSkpc jFWfzG')
            dados_o = soup.find_all('p', attrs={'data-testid': ['price-original']})
            dados_p = soup.find_all('p', attrs={'data-testid': ['price-value']})
            div_tags = soup.find_all('div', class_='sc-fwwElh bjQZYx')
            
            data_dict = {'titulo': [],'urls': [], 'original_prices': [], 'current_prices': [], 'image_urls': []}
            
            for dado in dados_h2:
                h2 = dado.find_all('h2')
                for titulo in h2:
                    data_dict['titulo'].append(titulo.get_text())

            for link in dados_link:
                a_tag = link.find('a')
                if a_tag and 'href' in a_tag.attrs:
                    href = a_tag['href']
                    full_url = f'https://www.magazinevoce.com.br{href}'
                    data_dict['urls'].append(full_url)

            for dado in dados_o:
                data_dict['original_prices'].append(self.format_price(dado.text))

            for dado in dados_p:
                data_dict['current_prices'].append(self.format_price(dado.text))

            for div_tag in div_tags:
                img_tag = div_tag.find('img', attrs={'data-testid': 'image'})
                if img_tag and 'src' in img_tag.attrs:
                    image_url = img_tag['src']
                    data_dict['image_urls'].append(image_url)

            return data_dict