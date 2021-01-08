import discord
from discord.ext import commands
from os import getenv
import coms

client = commands.Bot(command_prefix="nn!")
token = getenv("DISCORD_TOKEN")

@client.event
async def on_ready() :
    await client.change_presence(status = discord.Status.online, activity = discord.Game("Multi-Tasks Bot - nn!"))
    
client.run(token)
