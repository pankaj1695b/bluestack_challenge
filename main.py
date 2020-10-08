import discord
from discord.ext import commands
import os
from dotenv import load_dotenv, find_dotenv

# find and load .env file
load_dotenv(find_dotenv())

# get discord token for the bot
TOKEN = os.environ.get("BOT_TOKEN")

# set ! as command prefix
bot = commands.Bot(command_prefix='!')

# get all the cogs to be loaded
cogs = os.environ.get("COGS").split(" ")

# load all the cogs specified in .env
for cog in cogs:
    bot.load_extension("cogs." + cog)

# Start the bot.
bot.run(TOKEN)