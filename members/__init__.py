from discord.ext.commands import Bot

from members.manager import ban, joined, stonks


def init(bot: Bot):
    bot.add_command(ban)
    bot.add_command(joined)
    bot.add_command(stonks)

    return bot
