import discord 
import asyncio
import random
import json
import os

client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    
    
async def on_message(message):
    if message.content.startswith(club.creator):
        await client.send_message(message.channel, 'The creator of this bot is **MininDiamond123#7476**.')
       
client.run("TOKEN")
    
    
