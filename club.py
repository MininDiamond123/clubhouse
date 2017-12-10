import discord
import os
import io
import random
from discord.ext import commands

bot = commands.Bot(command_prefix = "club.", description = "The bot for The Clubhouse", owner_id = 389472478545575937)

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")
    
@bot.command()
async def flip(ctx):
    list = []
    for heads in range(0, 49):
        list.append("It landed on Heads.")
    for tails in range(0, 49):
        list.append("It landed on Tails.")
    list.append("It landed on the side!")
    flipped = random.choice(list)
    await ctx.send(flipped)

bot.run(os.environ.get("TOKEN"))
