import discord
import requests
from discord.ext import commands
from os import getenv

# init the bot

bot = commands.Bot(command_prefix="nn!")
token = getenv("DISCORD_TOKEN")

# set status config
@bot.event
async def on_ready():
    await bot.change_presence(status = discord.Status.online, activity = discord.Game("Multi-Tasks Bot - nn!"))

# general cog
class General(commands.Cog):
    def __init__(self, sbot):
        self.sbot = bot
    
    @sbot.command()
    async def ping(self, ctx) :
        """Check the ping time of the bot"""
        await ctx.send(f"🏓 Pong with {str(round(bot.latency, 2))} seconds!")

    @sbot.command()
    async def clear(self, ctx, amount=3) :
        """Purge the indicated amount of messages (by default 3)"""
        await ctx.channel.purge(limit=amount)

    @sbot.command()
    async def check_url(self, ctx, url):
        """Ping a URL for check his activity"""
        try:
            await ctx.send(f"The URL have return the code " + str(requests.get(url).status_code) + "!")
        except:
            await ctx.send(f"We have a problem with this URL... (Try to add http:// or https:// in the URL)")
            
# add general cog
bot.add_cog(General(bot))

# start the bot
bot.run(token)
