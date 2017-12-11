import discord
import os
import io
import random
from discord.ext import commands

bot = commands.Bot(command_prefix = "ch.", description = "The bot for The Clubhouse", owner_id = 389472478545575937)

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! :ping_pong: ")
    
@bot.command()
async def flip(ctx):
    list = []
    for heads in range(0, 49):
        list.append("It landed on Heads.")
    for tails in range(0, 49):
        list.append("It landed on Tails.")
    for side in range(0, 2):
        list.append("It landed on the side!")
    flipped = random.choice(list)
    await ctx.send(flipped)
    
@bot.command()
async def test(ctx):
    await ctx.send({embed: {color:FF0000, description:"Simple text"}})

bot.run(os.environ.get("TOKEN"))
