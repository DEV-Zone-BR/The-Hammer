from discord.ext.commands import Bot

from polemic.books import book_search


def init(bot: Bot):
    bot.add_command(book_search)

    return bot