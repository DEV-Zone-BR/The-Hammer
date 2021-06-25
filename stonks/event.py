from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup
import discord
import time
import re
import os


class ExtractedValues:
    os.environ['STONKS_TARGET_URL'] = 'https://www.fundsexplorer.com.br/funds'

    def __init__(self, price, div_yield, get_equity_value):
        self.price = price
        self.div_yield = div_yield
        self.get_equity_value = get_equity_value

    def format_values(self, code: str):
        """Return the formated values of investment fund"""
        return f"{code} - preço: {self.price}- dividend yield " \
               f"{self.div_yield} - valor_patrimonial {self.get_equity_value}"


class Handler:
    """Return the informations about your investment fund"""
    base_url = os.getenv('STONKS_TARGET_URL')
    beautiful_soup = BeautifulSoup()

    def __init__(self, ctx: discord, symbol_code: str):
        options = Options()
        options.headless = True
        self.driver = webdriver.Firefox(options=options, executable_path=GeckoDriverManager().install())
        self.ctx = ctx
        self.symbol_code = symbol_code

    def navigate(self):
        """Navigate to the URL"""
        self.driver.get(self.base_url)
        time.sleep(2)

    def insert_value(self, symbol: str):
        """Search for your inputed fund

        Keyword arguments:
        symbol -- investment fund of code
        """
        self.driver.get(f'{self.base_url}/{symbol.upper()}')

    def get_page(self):
        """Return HTML elements"""
        source_page = self.driver.page_source

        return BeautifulSoup(source_page, 'html.parser')

    def get_price(self, parser) -> str:
        """Get price of your investment fund

        Keyword arguments:
        parser -- HTML page parsed
        """
        try:
            price = parser.select('div#stock-price-wrapper div#stock-price span.price')[0].string
            price_result = re.search(r'(R\$).(\d+.\d+)', price).group(2)
            if price_result is not None:
                return price_result

            else:
                await self.ctx.send('Preço com formato incorreto')

        except (NoSuchElementException, TimeoutException):
            await self.ctx.send("O preço não foi encontrado na página")

    def get_div_yield(self, parser) -> str:
        """Get dividend yield of your investment fund

        Keyword arguments:
        parser -- HTML page parsed
        """
        try:
            div_yield = parser.select('div.carousel-cell.is-selected:nth-child(3) span.indicator-value')[0].string
            dividend_result = re.search(r'(\d{0,}[,.]{0,1}\d+%)', div_yield).group(1)
            if dividend_result is not None:
                return dividend_result

            else:
                await self.ctx.send('Dividend yield com formato incorreto')

        except (NoSuchElementException, TimeoutException):
            await self.ctx.send("O dividend yield não foi encontrado na página")

    def get_equity_value(self, parser) -> str:
        """Get equity value of your investment fund

        Keyword arguments:
        parser -- HTML page parsed
        """
        try:
            equity_value = parser.select('div.carousel-cell.is-selected:nth-child(5) span.indicator-value')[0].string
            equity_value_result = re.search(r'(R\$).(\d+.\d+)', equity_value).group(2)
            if equity_value_result is not None:
                return equity_value_result

            else:
                await self.ctx.send('Valor patrimonial com formato incorreto')

        except (NoSuchElementException, TimeoutException):
            await self.ctx.send("Valor patrimonial não encontrado na página")

    def get_values(self):
        """Return all values of investment fund"""
        parser = self.get_page()
        price = self.get_price(parser)
        div_yield = self.get_div_yield(parser)
        equity_value = self.get_equity_value(parser)
        extracted_values = ExtractedValues(price, div_yield, equity_value)

        return extracted_values

    def handle(self):
        """Execute all functions"""
        if self.symbol_code:
            self.navigate()
            self.insert_value(self.symbol_code)

            return self.get_values().format_values(self.symbol_code)

        else:
            await self.ctx.send('Ocorreu um erro ao enviar codigo do seu FII')