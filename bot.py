import discord
from discord.ext import commands
import members
import job_vacancies

from config import TOKEN

bot = commands.Bot(command_prefix='--')
bot = members.init(bot)
bot = bot_utils.init(bot)
# bot = job_vacancies.init(bot)z

bot.run(TOKEN)
