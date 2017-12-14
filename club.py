import discord
import os
import io
import random
from discord.ext import commands
from contextlib import redirect_stdout
import traceback
import textwrap

bot = commands.Bot(command_prefix = "ch.", description = "The bot for The Clubhouse", owner_id = 389472478545575937)

def cleanup_code(content):
    """Automatically removes code blocks from the code."""
    # remove ```py\n```
    if content.startswith('```') and content.endswith('```'):
        return '\n'.join(content.split('\n')[1:-1])

    return content.strip('` \n')

devs = [
    292690616285134850,
    241653137868455947
]
    

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
    
    
@bot.command(pass_context=True, hidden=True, name='eval')
async def _eval(ctx, *, body: str):
        """Evaluates a code"""
        if ctx.author.id not in devs: return
        
        env = {
                'bot': bot,
                'ctx': ctx,
                'channel': ctx.channel,
                'author': ctx.author,
                'guild': ctx.guild,
                'message': ctx.message,
        }

        env.update(globals())

        body = cleanup_code(body)
        stdout = io.StringIO()

        to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

        try:
            exec(to_compile, env)
        except Exception as e:
            return await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')

        func = env['func']
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except Exception as e:
            value = stdout.getvalue()
            await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
        else:
            value = stdout.getvalue()
            try:
                await ctx.message.add_reaction('\u2705')
            except:
                pass

            if ret is None:
                if value:
                    await ctx.send(f'```py\n{value}\n```')
            else:
                await ctx.send(f'```py\n{value}{ret}\n```')

bot.run(os.environ.get("TOKEN"))
