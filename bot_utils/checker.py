from discord.ext import commands


@commands.command()
async def ping(ctx):
    print('pong')
    await ctx.send('pong')
