import discord
from discord.ext import commands
from stonks.event import Handler

@commands.command()
async def stonks(ctx: discord, code: str):
    result_message = Handler(ctx, code).handle()
    await ctx.send(result_message)
