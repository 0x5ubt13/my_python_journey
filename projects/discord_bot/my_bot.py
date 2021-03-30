#!/usr/bin/python3
import discord
import emojis
import logging
import json
import typing
from pathlib import Path
import os
from discord.ext import commands

cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd}\n-----")

# Hiding the token and defining info
secret_file = json.load(open(cwd+'/bot_config/secrets.json'))
bot = commands.Bot(command_prefix='$', case_insensitive=True, owner_id=339875659692113922)
bot.config_token = secret_file['token']
logging.basicConfig(level=logging.INFO)

bot.version = '0.1'


# If the bot is up and running, print the message to console and change the Game overlay
@bot.event
async def on_ready():
    print(f"-----\nLogged in as: {bot.user.name} : {bot.user.id}\n-----\nMy current prefix is: $\n-----")
    # Changing the bot activity:
    await bot.change_presence(activity=discord.Game(name=f"Hey! Listening to $help"))


@bot.event
async def on_command_error(ctx, error):
    # Ignoring this errors to avoid cluttering the terminal
    ignored_commands = (commands.CommandNotFound, commands.UserInputError)
    if isinstance(error, ignored_commands):
        return

    # Begin error handling
    if isinstance(error, commands.CommandOnCooldown):
        minutes, seconds = divmod(error.retry_after, 60)
        hours, minutes = divmod(minutes, 60)
        if int(hours) == 0 and int(minutes) == 0:
            await ctx.send(f"You must wait {int(seconds)} seconds to use this command!")
        elif int(hours) == 0 and int(minutes) != 0:
            await ctx.send(f"You must wait {int(minutes)} minutes and {int(seconds)} seconds to use this command!")
        else:
            await ctx.send(f"You must wait {int(hours)} hours, {int(minutes)} minutes and {int(seconds)} seconds to use this!")
    elif isinstance(error, commands.CheckFailure):
        await ctx.send("Listen mate... You lack permission to use this command.")
    raise error


@bot.command(name='hi', aliases=['hello'])
async def _hi(ctx):
    """ A simple command which says hi to the author """
    await ctx.send(f"Hi {ctx.author.mention}!")
    # Another way of doing this would be (user object).mention:
    # await ctx.send(f"Hi <@{ctx.author.id}>!"


@bot.command()
async def echo(ctx, *, message=None):
    """ A simple command that repeats the user's input back to them"""
    message = message or "Please provide the message to be repeated"
    await ctx.message.delete()
    await ctx.send(message)

# Run the bot!
# When running this file, if it is the 'main' file
# i.e. it's not being imported from another python file, run this
if __name__ == '__main__':
    bot.reaction_roles = Document(bot.db, "reaction_roles")

    for file in os.listdir(cwd+"/cogs"):
        # Ignoring all the files starting with underscore
        if file.endswith(".py") and not file.startswith("_"):
            bot.load_extension(f"cogs.{file[:-3]}")

    bot.run(bot.config_token)
