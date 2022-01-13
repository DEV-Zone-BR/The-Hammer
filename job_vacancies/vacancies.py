import urllib
import discord
from discord.ext import commands
from job_vacancies.scraping import get_all_vacanicies


@commands.command()
async def vacancies_search(ctx: discord, end: int, page: int):
    try:
        vacancies_list = get_all_vacanicies(end, page)
        if not vacancies_list:
            await ctx.send(f" ```It was not possible to make the request, please try again later !.```")
        await ctx.send(f"Ola, aqui está a sua lista de vagas")
        for vacancies in vacancies_list:
            embed = discord.Embed(
                title=vacancies.get('title'),
                url=vacancies.get('more_information'),
                description=f" ```\nPage - {vacancies.get('page')} | number - {vacancies.get('vacancie_number')}\nStatus: {vacancies.get('status')}\nEmpresa: {vacancies.get('empresa')}\nLevel: {vacancies.get('level')}\nLocal: {vacancies.get('local')}\nTechnologies: { vacancies.get('technologies')} ``` ",
                color=0xFF5733)
            embed.set_thumbnail(url="https://picsum.photos/500/500")

            embed.add_field(
                name="Dev Zone",
                value="Developer by devzone Comunnity.",
                inline=False)

            embed.set_footer(
                text=f"Information requested by: {ctx.author.display_name}")
            await ctx.send(embed=embed)
    except BaseException:
        await ctx.send(f" ```It was not possible to make the request, please try again later !.```")
