import pytest
import time
from unittest.mock import patch
from unittest.mock import Mock

from tech_news.collector.scrapper import ( fetch_content, scrape)

from tests.test_collector.faker import RESPONSE
## FECTH_CONTENT
# Caso a requisição seja bem sucedida retorne seu conteúdo de texto;
def test_validar_metodo_fetch_com_sucesso():
    print(fetch_content('https://app.betrybe.com/'))
    assert 'content=\"Aprenda a programar com uma formação de alta qualidade e só comece a pagar quando conseguir um bom trabalho.\"' in fetch_content('https://app.betrybe.com/')

# O tempo máximo de resposta do servidor deve ser configurado como parâmetro e por padrão será 3 segundos;
def test_validar_metodo_fetch_com_tempo_maximo_maior_que_3():
    print(fetch_content('https://httpbin.org/delay/10'))
    assert "" == fetch_content('https://httpbin.org/delay/10')

#Caso a resposta tenha o código de status diferente de 200, deve-se retornar uma str vazia;
def test_validar_metodo_fetch_com_status_diferente_de_200():
    print(fetch_content('https://httpbin.org/status/404'))
    assert "" == fetch_content('https://httpbin.org/status/404')

## SCRAPPER

# Por padrão deve-se raspar apenas as notícias da primeira página;

# validar os campos se e string etc

# validar se retorna uma list

#Um número de páginas para serem raspadas pode ser passado para a função. Caso o número de páginas seja definido, deve-se raspar os dados das N primeiras páginas;


# INSERT_OR_UPDATE

# Insira uma notícia no banco;

# Caso a notícia já exista no banco de dados, ela deve ser atualizada;

# Deve retornar True caso a notícia seja inserida senão False.

# IMPORTER

# Caso a extensão do arquivo seja diferente de .csv, uma exceção deve ser lançada;

# Caso o arquivo CSV não exista, uma exceção deve ser lançada;

# A função deve retornar uma lista com cada notícia em no seguinte formato.

# EXPORTER

# O arquivo exportado deve possuir o formato CSV. Caso contrário, uma exceção deve ser lançada;

# Caso já exista um arquivo com o mesmo nome, ele deve ser substituído;

# O arquivo CSV deve possuir um cabeçalho contendo url, title, timestamp, writer, shares_count, comments_count, summary, sources e categories;

# Todas as notícias salvas no banco de dados devem ser exportadas.

# SEARCH BY TITLE

# A busca deve ser case insensitive e deve retornar uma lista de lista de tuplas [("title", "url")];

# Caso nenhuma notícia seja encontrada, deve-se retornar uma lista vazia.

# SEARCH BY DATE

# A busca deve retornar uma lista de tuplas [("title", "url")];

# A data deve estar no formato "aaaa-mm-dd" e deve ser válida. Caso seja inválida, uma exceção deve ser lançada.

# Caso nenhuma notícia seja encontrada, deve-se retornar uma lista vazia.

# SEARCH BY SOURCE

# A busca deve ser case insensitive e deve retornar uma lista de tuplas [("title", "url")];

# Caso nenhuma notícia seja encontrada, deve-se retornar uma lista vazia.

# SEARCH BY CATEGORY

# A busca deve ser case insensitive e deve retornar uma lista de tuplas [("title", "url")];

# Caso nenhuma notícia seja encontrada, deve-se retornar uma lista vazia.

# TOP 5 NEWS

#  As top 5 notícias da análise devem ser retornadas em uma lista de tuplas [("title", "url")];

# Caso haja menos de cinco notícias, no banco de dados, deve-se retornar todas as notícias existentes;

# Caso não haja notícias disponíveis, deve-se retornar uma lista vazia.

# TOP 5 CATEGORIES

# As top 5 categorias da análise devem ser retornadas em uma lista no formato ["category"];

# Caso haja menos de cinco categorias, no banco de dados, deve-se retornar todas as categorias existentes;

# Caso não haja categorias disponíveis, deve-se retornar uma lista vazia.