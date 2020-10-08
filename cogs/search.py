import dao.history as history
import discord
from discord.ext import commands
import requests
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class Search(commands.Cog):
    """
    A class used to handle all commands related to google search and searching through history.
    It inherits Cog class.
    ...

    Methods
    -------
    google_search(ctx)
        Uses google apis to get the first five result for the query. 
        It is annotated as command and responds to !google <querY>

    recent_search(ctx)
        Uses dao to search through user history and return similar searches. 
        It is annotated as command and responds to !recent <querY>
    
    """

    def __init__(self, bot):
        self.bot = bot
        self.history = history.History()
        self.use_db = False if (os.environ.get("USE_DB").lower() == "false") else True
        self.api_key = os.environ.get("GOOGLE_API_KEY")
        self.cx = os.environ.get("GOOGLE_CX")

    # get google results for the query
    def get_google_results(self, query):
        params = {}
        params['key'] = self.api_key
        params['cx'] = self.cx
        params['q'] = query
        response = requests.get('https://www.googleapis.com/customsearch/v1', params=params)
        return response.json()

    @commands.command(name='google', help='Do a google search')
    async def google_search(self, ctx, query=""):
        user = ctx.message.author
        # if query is empty fail
        if query == "" :
            await ctx.send("Please provide the string to query. for example: !google <query string>")
            return
        
        # Flag to enable db
        if self.use_db:
            self.history.save_history(user, query)
        # get google results
        google_results = self.get_google_results(query)
        result = google_results['items']
        item_links = ""
        # retrieve first five google results and append them to item_links seperated by "/n"
        for i in range(5) :
            item_links = item_links + "\n" + str(result[i]['link'])
        await ctx.send(item_links)

    @commands.command(name='recent', help='search through history')
    async def recent_search(self, ctx, query=""):
        user = ctx.message.author
        
        recent_searches = ""

        # Flag to enable db. Get search results from db if db is enabled.
        if self.use_db:
            recent_searches = self.history.get_history(user, query)
        
        # Msg if recent searches is empty
        if not recent_searches:
            await ctx.send("No results found!!")
            return

        await ctx.send(recent_searches)

# add the cog to bot
def setup(bot):
    bot.add_cog(Search(bot))
    print('Search bot loaded.')
