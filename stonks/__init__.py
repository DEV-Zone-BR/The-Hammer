from discord.ext.commands import Bot
from commands import stonks

def init(bot: Bot):
    bot.add_command(stonks)
