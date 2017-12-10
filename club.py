import discord
import os
import io
from discord.ext import commands

bot = commands.Bot(command_prefix = "club.", description = "The bot for The Clubhouse", owner_id = 389472478545575937)

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!)"

bot.run(os.environ.get("TOKEN"))
