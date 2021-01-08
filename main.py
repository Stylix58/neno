import discord
import requests
from discord.ext import commands
from os import getenv

bot = commands.Bot(command_prefix="nn!")
token = getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    await bot.change_presence(status = discord.Status.online, activity = discord.Game("Multi-Tasks Bot - nn!"))

# help message

@bot.command()
async def help(ctx):
    helptext = "**Neno Bot**\nhttps://cdn.discordapp.com/app-icons/796854915850567720/ac273fdf92876b8d2e7945012a482829.png\nNeno is a multi-tasks bot made for help people.\n\n**Commands**:\n"
    for command in self.bot.commands:
        helptext+=f"**{command}**: \n{exec(command + '.__doc__')}\n\n"
    await ctx.send(helptext)

# general

@bot.command()
async def ping(ctx) :
    """Check the ping time of the bot"""
    await ctx.send(f"🏓 Pong with {str(round(bot.latency, 2))} seconds!")

@bot.command()
async def clear(ctx, amount=3) :
    """Purge the indicated amount of messages (by default 3)"""
    await ctx.channel.purge(limit=amount)

@bot.command()
async def check_url(ctx, url):
    """Ping a URL for check his activity"""
    try:
        await ctx.send(f"The URL have return the code " + str(requests.get(url).status_code) + "!")
    except:
        await ctx.send(f"We have a problem with this URL... (Try to add http:// or https:// in the URL)")

bot.run(token)
