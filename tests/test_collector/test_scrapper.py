import pytest
import time
from unittest.mock import patch
from unittest.mock import Mock

from tech_news.collector.scrapper import ( fetch_content, scrape)

from tests.test_collector.faker import RESPONSE
# Caso a requisição seja bem sucedida retorne seu conteúdo de texto;
def test_validar_metodo_fetch_content_quando_status_200():
    teste = fetch_content('https://app.betrybe.com/') 

    assert "Aprenda a programar com uma formação de alta qualidade e só comece a pagar quando conseguir um bom trabalho." in teste