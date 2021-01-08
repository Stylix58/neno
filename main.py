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
    await bot.change_presence(status = discord.Status.online, activity = discord.Game("Multi-Tasks Bot - nn! - " +
    "https://discord.bots.gg/bots/796854915850567720"))

# general cog
class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def ping(self, ctx) :
        """Check the ping time of the bot"""
        await ctx.send(f"🏓 Pong with {str(round(bot.latency, 2))} seconds!")

    @commands.command()
    async def clear(self, ctx, amount=3) :
        """Purge the indicated amount of messages (by default 3)"""
        await ctx.channel.purge(limit=amount)

    @commands.command()
    async def check_url(self, ctx, url):
        """Ping a URL for check his activity"""
        await ctx.send("Checking the URL...")
        try:
            await ctx.send("The URL have return the code " + str(requests.get(url).status_code) + "!")
        except:
            await ctx.send("We have a problem with this URL... (Try to add http:// or https:// in the URL)")

    @commands.command()
    async def eval(self, ctx, code):
        """ONLY FOR BOT'S OWNER: Eval the indicated code"""
        try:
            if ctx.message.author.id == "706493774338981949":
                await ctx.send(eval(code))
            else:
                await ctx.send("You don't are the owner of the bot!")
        except:
            await ctx.send("A error is happened...")

# add general cog
bot.add_cog(General(bot))

# start the bot
bot.run(token)
