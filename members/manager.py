import discord
from discord.ext import commands

from config import ETERNAL_ROLES


@commands.command()
async def joined(ctx: discord, member: discord.Member):
    """Says when a member joined."""
    print(member)
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))


@commands.command()
async def ban(ctx: discord, member: discord.Member):
    channel = [c for c in ctx.guild.channels if c.name.endswith('__geral')][0] or None
    # await channel.send(':hammer:')
    roles = set([r.name for r in member.roles]) & ETERNAL_ROLES
    if len(roles) > 0:
        await ctx.send('Você não pode remover um membro do conselho', )
    else:
        await ctx.send('{0.name} foi removido por inatividade'.format(member))
        # await ctx.guild.kick(member)