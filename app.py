import discord
from discord.ext import commands

from music import music
bot = commands.Bot(command_prefix='__')
bot.add_cog(music(bot))

import os
 
# token = "" 
# with open("tokens.txt") as file:
#     token = file.read()



bot.run(os.getenv('TOKEN'))
