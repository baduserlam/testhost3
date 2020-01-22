import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='!')

@bot.command(pass_context=True)
async def test(ctx, arg):
    await ctx.send(arg)

token = os.environ.get('BOT_TOKEN')

bat.run(str(token))
