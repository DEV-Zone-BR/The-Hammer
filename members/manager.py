import discord
from discord.ext import commands
from stonks import Handler
from config import ETERNAL_ROLES, ALLOWED_ROLES
from authorization import check_member


@commands.command()
async def joined(ctx: discord, member: discord.Member):
    """Says when a member joined."""
    print(member)
    await ctx.send("{0.name} joined in {0.joined_at}".format(member))


@commands.command()
async def ban(ctx: discord, member: discord.Member):
    if not await check_member(ctx, ALLOWED_ROLES["ban"]):
        return

    channel = [c for c in ctx.guild.channels if c.name.endswith(
        "__geral")][0] or None
    roles = set([r.name for r in member.roles]) & ETERNAL_ROLES
    print(roles)
    if len(roles) > 0:
        await ctx.send(
            "Você não pode remover um membro do conselho",
        )
    else:
        await channel.send(
            ":hammer: {0.name} estava muito tempo sem dar um oi para os amigos".format(
                member
            )
        )
        await ctx.send("{0.name} foi removido por inatividade".format(member))
        await ctx.guild.kick(member)


@commands.command()
async def stonks(ctx: discord, code: str):
    result = Handler.handle(code)
    ctx.send(f"{code} - preço: {result['preco']}"
             f" - dividend yield {result['dividend_yield']}"
             f" - valor_patrimonial {result['valor_patrimonial']}")
