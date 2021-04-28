from discord.ext.commands import Bot

from members.manager import ban, joined


def init(bot: Bot):
    bot.add_command(ban)
    bot.add_command(joined)

    return bot
