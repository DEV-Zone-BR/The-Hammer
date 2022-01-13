from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup
import time
import re
from .types import StonksResult


class Handler:
    """
    Insert Your FII code to get the information about it
     INPUT
     - Ex: HGLG11

     OUTPUT
       {price: '00,00', div_yield: '0,00%', equity_value: '00,00', name:'HGLG11' }
    """
    base_url = 'https://www.fundsexplorer.com.br/funds'
    beautiful_soup = BeautifulSoup()

    def __init__(self):
        options = Options()
        options.headless = True
        self.driver = webdriver.Firefox(
            options=options,
            executable_path=GeckoDriverManager().install())

    def navigate(self):
        self.driver.get(self.base_url)
        time.sleep(2)

    def insert_value(self, symbol: str):
        self.driver.get(f'{self.base_url}/{symbol.upper()}')

    def get_page(self):
        source_page = self.driver.page_source
        return BeautifulSoup(source_page, 'html.parser')

    def get_price(self, parser):
        price = parser.select(
            'div#stock-price-wrapper div#stock-price span.price')[0].string
        return re.search(r'(R\$).(\d+.\d+)', price).group(2)

    def get_div_yield(self, parser):
        div_yield = parser.select(
            'div.carousel-cell.is-selected:nth-child(3) span.indicator-value')[0].string
        return re.search(r'(\d{0,}[,.]{0,1}\d+%)', div_yield).group(1)

    def get_equity_value(self, parser):
        equity_value = parser.select(
            'div.carousel-cell.is-selected:nth-child(5) span.indicator-value')[0].string
        return re.search(r'(R\$).(\d+.\d+)', equity_value).group(2)

    def get_values(self) -> StonksResult:
        parser = self.get_page()
        price = self.get_price(parser)
        div_yield = self.get_div_yield(parser)
        equity_value = self.get_equity_value(parser)
        result = {"preco": price, "valor_patrimonial": equity_value,
                  "dividend_yield": div_yield}
        return result

    def handle(self, symbol_code):
        self.navigate()
        self.insert_value(symbol_code)
        return self.get_values()
