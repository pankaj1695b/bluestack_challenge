import youtube_dl
import asyncio
import urllib.request
import re
import discord
from discord.ext import commands


class Music(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        self.ydl = youtube_dl.YoutubeDL({
        'format': 'bestaudio/best',
        'quiet': 'true',
        'outtmpl': 'downloads/%(extractor)s-%(id)s-%(title)s.%(ext)s',
        })
        self.queue = None

    def search_youtube(self, query):
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + query)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        return "https://www.youtube.com/watch?v=" + video_ids[0]

    @commands.command(name='play', help='play music')
    async def play_music(self, ctx, song):
        loop = asyncio.get_event_loop()
        voice_channel = ""
        try :
            voice_channel = ctx.author.voice.channel
        except :
            await ctx.send(":notes: Please join voice channel!")
            return
            
        voice = ctx.channel.guild.voice_client
        url = self.search_youtube(song.replace(" ", "+"))
        data = await loop.run_in_executor(None, lambda: self.ydl.extract_info(url=url, download = True))
        if 'entries' in data:
            data = data['entries'][0]
        
        await ctx.send(f':notes: Added to queue: **{data["title"]}**')

        filename = self.ydl.prepare_filename(data)

        if voice is None:
            voice = await voice_channel.connect()
        
        if voice.channel.id != voice_channel.id:
            await voice.move_to(voice_channel)

        await ctx.send(f':notes: Playing: **{data["title"]}**')
        voice.play(discord.FFmpegPCMAudio(filename))

    @commands.command(name='stop', help='stop music')
    async def stop_music(self, ctx):
        voice = ctx.channel.guild.voice_client
        voice.stop()
        await ctx.send('**:notes: Ok, Stopping Music!!**')

def setup(bot):
    bot.add_cog(Music(bot))
    print('Music bot loaded.')
