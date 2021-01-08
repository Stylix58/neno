import discord
from discord.ext import commands
from os import getenv
from uptime import monitor_uptime

client = commands.Bot(command_prefix="nn!")
token = getenv("DISCORD_TOKEN")

@client.event
async def on_ready() :
    await client.change_presence(status=discord.Status.online, activity = discord.Game(name = "Multi-tasks bot - nn!"))

@client.command()
async def ping(ctx) :
    """Check the ping time of the bot"""
    await ctx.send(f"🏓 Pong with {str(round(client.latency, 2))}")

@client.command()
async def clear(ctx, amount=3) :
    """Purge the indicated amount of messages (by default 3)"""
    await ctx.channel.purge(limit=amount)

@client.command()
async def uptime(ctx, url) :
    """Check the uptime of a URL"""
    await ctx.send(f"Checking the URL...")
    if monitor_uptime(url) == True:
        await ctx.send(f"✔ The URL is up!")
    else:
        await ctx.send(f"❌ The URL is down!")
    
client.run(token)
