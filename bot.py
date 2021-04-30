from discord.ext import commands

import bot_utils
import members
from config import TOKEN

bot = commands.Bot(command_prefix='--')
bot = members.init(bot)
bot = bot_utils.init(bot)

bot.run(TOKEN)
