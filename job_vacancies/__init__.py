from discord.ext.commands import Bot
from job_vacancies.vacancies import vacancies_search


def init(bot: Bot):
    bot.add_command(vacancies_search)

    return bot