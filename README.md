# Aria
Aria is a multi-utility discord bot.

## Currently it can:
- 1. Reply to "hi" and "bye aria" of the user.
- 2. Do a google search and display first five results. It also maintains search history of the users   and allows them to search the history.
- 3. It can play music from youtube. Currently it supports only playing and stopping it.

## Aria Commands:
- aria google "<query>" - to do a google search
- aria recent "<query>" - to search through history
- aria play "<song name>" - to play the music
- aria stop - to stop playing the music

## Notes:
- To enable searching through google, you will need google api key and custom search engine. If it is not available you can remove the feature by removing "search" from cogs in .env

- To enable search history you will need to start a mySql server and provide the relevant information in .env. History serach is part of "search" cog in cogs of .env.

- To enable the bot you will need a discord bot token and provide it in .env.



