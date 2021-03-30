#!/usr/bin/python3
import discord
import emojis
import logging
import json
import typing
from pathlib import Path
from discord.ext import commands

cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd}\n-----")

# Hiding the token
secret_file = json.load(open(cwd+'/bot_config/secrets.json'))
bot = commands.Bot(command_prefix='$', case_insensitive=True)
bot.config_token = secret_file['token']
logging.basicConfig(level=logging.INFO)


@bot.event
async def on_ready():
    print(f"-----\nLogged in as: {bot.user.name} : {bot.user.id}\n-----\nMy current prefix is: $\n-----")
    # Changing the bot activity:
    await bot.change_presence(activity=discord.Game(name=f"Hey! Listening to $help"))


@bot.command(name='hi', aliases=['hello'])
async def _hi(ctx):
    """ A simple command which says hi to the author """
    await ctx.send(f"Hi {ctx.author.mention}!")
    # Another way of doing this would be (user object).mention
    #await ctx.send(f"Hi <@{ctx.author.id}>!"


@bot.command()
async def echo(ctx, *, message=None):
    """ A simple command that repeats the user's input back to them"""
    message = message or "Please provide the message to be repeated"
    await ctx.message.delete()
    await ctx.send(message)

# Run the bot!
bot.run(bot.config_token)


