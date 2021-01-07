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

@client.command()
async def ping(ctx) :
    """Check the ping time of the bot"""
    await ctx.send(f"🏓 Pong with {str(round(client.latency, 2))}")

@client.command()
async def clear(ctx, amount=3) :
    """Purge the indicated amount of messages (by default 3)"""
    await ctx.channel.purge(limit=amount)

@client.command()
async def ping_service(ctx, url):
    """Ping a url"""
    response = requests.get(url)
    print(int(response.status_code))
    if response.status_code == requests.codes.ok:
        await ctx.send(f"👍 The URL have return a good response (" + response.status_code + ")")
    else:
        await ctx.send(f"✖ The URL have return a bad response (" + response.status_code + ")")

client.run(token)
