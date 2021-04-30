import discord
from discord.ext import commands
import members
import polemic

from config import TOKEN

bot = commands.Bot(command_prefix='--')
bot = members.init(bot)
bot = polemic.init(bot)

bot.run(TOKEN)
