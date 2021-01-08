import discord
from discord.ext import commands
import requests
client = commands.Bot()

@client.command()
async def ping(ctx) :
    """Check the ping time of the bot"""
    await ctx.send(f"🏓 Pong with {str(round(client.latency, 2))}")

@client.command()
async def clear(ctx, amount=3) :
    """Purge the indicated amount of messages (by default 3)"""
    await ctx.channel.purge(limit=amount)

@client.command()
async def uptime(ctx, url):
    """Ping a URL for check his uptime"""
    r = requests.get(url)
    if r.status_code == 200:
        await ctx.send(f"⏫ The URL is up! (HTTP code: " + str(r.status_code) + ")")
    else:
        await ctx.send(f"⏬ The URL is down! (HTTP code: " + str(r.status_code) + ")")