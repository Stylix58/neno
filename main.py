import discord
from discord.ext import commands
from os import getenv
import requests
import time

client = commands.Bot(command_prefix="n!")
token = getenv("DISCORD_TOKEN")

@client.event
async def on_ready() :
    await client.change_presence(status = discord.Status.idle, activity = discord.Game("Multi-tasks bot - n!"))
    print("I am online")

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def ping(ctx) :
        """Check the ping time of the bot"""
        await ctx.send(f"🏓 Pong with {str(round(client.latency, 2))}")

    @commands.command()
    async def clear(ctx, amount=3) :
        """Purge the indicated amount of messages (by default 3)"""
        await ctx.channel.purge(limit=amount)

    @commands.command()
    async def ping_service(ctx, url):
        """Ping a url"""
        await ctx.send(f"Pinging the URL...")
        response = requests.get(url)
        await ctx.send(f"The URL have return " + response.status_code + " code")

bot.add_cog(Greetings(client))
client.run(token)
