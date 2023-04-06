from tqdm import tqdm
from urllib.request import urlopen
from bs4 import BeautifulSoup



# URLs alvo para Web Scraping
url_petiscos = 'https://receitas.globo.com/tipos-de-prato/lanches/petiscos/'
url_doces = 'https://receitas.globo.com/tipos-de-prato/doces-e-sobremesas/'

def get_recipes(url):
    try:
        print(f'Obtendo receitas de {url}')
        html = urlopen(url)
        
        # Parser das tags HTML
        bs = BeautifulSoup(html, 'html.parser')
        
        # Encontrando os links para as receitas
        recipes_links = bs.find_all('a', {'class': 'feed-post-link'})
        
        # Iterando pelos links das receitas
        for link in tqdm(recipes_links[:10]):
            recipe_url = link['href']
            get_recipe_info(recipe_url)
            
    except Exception as e:
        print(f'Ocorreu algum erro ao tentar acessar o site. {e}')

def get_recipe_info(recipe_url):
    try:
        print(f'Obtendo informações da receita {recipe_url}')
        html = urlopen(recipe_url)
        
        # Parser das tags HTML
        bs = BeautifulSoup(html, 'html.parser')
        
        # Obtendo a descrição da receita
        description = bs.find('ul', {'class': 'content-unordered-list'}).get_text()
        
        
        # Obtendo o título da receita
        title = bs.find('h1', {'class': 'content-head__title'}).get_text()
        
        # Salvando as informações em arquivos separados
        save_recipe(title, description)
        
    except Exception as e:
        print(f'Ocorreu algum erro ao tentar acessar o site. {e}')

def save_recipe(title, description):
    try:
        print('Nome: ',title,'\n','ingrdientes: ', description)
    except Exception as e:
        print(f'Ocorreu algum erro ao tentar gravar o arquivo. {e}')

# Capturando as receitas de petiscos e doces/sobremesas
get_recipes(url_petiscos)
get_recipes(url_doces)
