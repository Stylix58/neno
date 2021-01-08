import discord
import requests
from discord.ext import commands
from os import getenv

client = commands.Bot(command_prefix="nn!")
token = getenv("DISCORD_TOKEN")

@client.event
async def on_ready() :
    await client.change_presence(status = discord.Status.online, activity = discord.Game("Multi-Tasks Bot - nn!"))

# general

@client.command()
async def ping(ctx) :
    """Check the ping time of the bot"""
    await ctx.send(f"🏓 Pong with {str(round(client.latency, 2))}")

@client.command()
async def clear(ctx, amount=3) :
    """Purge the indicated amount of messages (by default 3)"""
    await ctx.channel.purge(limit=amount)

@client.command()
async def check_url(ctx, url):
    """Ping a URL for check his activity"""
    try:
        await ctx.send(f"The URL have return the code " + str(requests.get(url).status_code) + "!")
    except:
        await ctx.send(f"We have a problem with this URL...")

client.run(token)