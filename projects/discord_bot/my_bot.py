#!/usr/bin/python3
import discord
import emojis
import logging
from pathlib import Path
import json
import typing
from discord.ext import commands

cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd}\n-----")

# Hiding the token
secret_file = json.load(open(cwd+'/bot_config/secrets.json'))

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
