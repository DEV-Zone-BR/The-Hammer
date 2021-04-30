from discord.ext.commands import Bot

from bot_utils.checker import ping


def init(bot: Bot):
    bot.add_command(ping)

    return bot
