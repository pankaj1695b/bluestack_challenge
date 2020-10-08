import discord
from discord.ext import commands
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

TOKEN = os.environ.get("BOT_TOKEN")

bot = commands.Bot(command_prefix='aria ')

cogs = os.environ.get("COGS").split(" ")

for cog in cogs:
    bot.load_extension("cogs." + cog)

bot.run(TOKEN)