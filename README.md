# Loja_Store - Web Scraping e Site Atualizável

Neste projeto, realizamos web scraping de vários produtos na loja Magazine Luiza. Durante a raspagem, coletamos informações sobre os produtos, incluindo seus preços reais e promocionais, bem como suas imagens. Além disso, desenvolvemos um site que se atualiza automaticamente com os dados coletados. Este site estava hospedado em uma instância EC2 na AWS.

## Tecnologias Utilizadas

- Flask: Utilizamos o framework web Flask para criar o site.
- BeautifulSoup e Requests: Utilizamos essas bibliotecas Python para realizar o web scraping.
- Outras bibliotecas específicas para diferentes categorias de produtos.

## Como Executar

1. Certifique-se de ter todas as dependências instaladas. Você pode instalá-las usando o `pip`:

   ```bash
   pip install flask beautifulsoup4 requests
