import discord
from discord.ext import commands

class Events(commands.Cog):
    """
    A class used to handle all user generated events
    This class handles hi and bye responses for the bot.
    It inherits Cog class.
    ...

    Methods
    -------
    on_message(message)
        Replies hi or bye if hi and bye are contained in user message.
        It gets the name of sender from the context to reply to the particular person.
    
    """
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        # If sender of the message is bot itself then return. Avoid infinite loop.
        if message.author == self.bot.user:
            return
        
        user = str(message.author)

        # If user message has "hi" then reply "Hey <name> !!"
        if  message.content.lower() == 'hi' :
            response = "Hey {} !!".format(user.split('#')[0])
            await message.channel.send(response)

        # If user message has "bye" then reply "Bye <name> !!"
        if  message.content.lower() == 'bye' :
            response = "Bye {} !!".format(user.split('#')[0])
            await message.channel.send(response)
        
# Add the current class as a cog to the bot.
def setup(bot):
    bot.add_cog(Events(bot))
    print('Events bot loaded.')