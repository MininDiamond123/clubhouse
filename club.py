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
    flipped = random.choice(["It landed on Heads.", "It landed on Tails", "OMG IT LANDED ON THE EDGE!!"])
    await ctx.send(flipped)

bot.run(os.environ.get("TOKEN"))
