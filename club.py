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
async def nhie(ctx):
    nhie = ["failed a test", "had a crush on anyone", "eaten anything nasty", "used a door incorrectly", "cried during a movie", "missed a high-five"]
    choice = random.choice(nhie)
    await ctx.send("Never have I ever...", choice,"!")
bot.run(os.environ.get("TOKEN"))
