import discord
from discord.ext import commands
import members

from config import TOKEN

bot = commands.Bot(command_prefix='--')
bot = members.init(bot)

bot.run(TOKEN)
