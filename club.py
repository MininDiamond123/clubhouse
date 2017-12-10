import discord
import os
import io
from discord.ext import commands

bot = commands.Bot(command_prefix="club.", description="small description", owner_id=ur id)

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!)"

bot.run(os.environ.get("TOKEN"))
