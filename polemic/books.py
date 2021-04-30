import requests
import urllib
import discord
from discord.ext import commands

@commands.command()
async def book_search(ctx: discord, book:str):
  
  try:
    response = requests.get(f'https://plmcbks.amanoteam.com/search/books?query_name={book}&search_type=fast&page_number=0&max_items=3')

    print(response.status_code)

    if(response.status_code==200):

      print("here")

      await ctx.send(f'Olá, Aqui está sua lista de livros polêmicos')

      books = response.json()["results"]["items"]      

      for book in books:

        await ctx.send(f'https://plmcbks.amanoteam.com/view/{book["id"]} \n ```Título: {book["title"]}\nCategoria:{book["category"]["name"]}\nAuthor:{book["author"]["name"]}```\n**Link Para Download**:https://plmcbks.amanoteam.com/download/{book["id"]}')        

      # https://plmcbks.amanoteam.com/view/13637
    
    else:
      pass
  except Exception as e:
    print(e)
    print(response.status_code)