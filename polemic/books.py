import requests
import urllib
import discord
from discord.ext import commands

@commands.command()
async def book_search(ctx: discord, book:str):
  
  try:
    request = requests.get(f'https://plmcbks.amanoteam.com/search/books?query_name={book}&search_type=fast&page_number=0&max_items=1000')

    print(request.status_code, requests.json())

    if(request.status_code==200):
      pass
    else:
      pass
  except Exception:
    pass