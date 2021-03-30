import discord
import emojis
import typing

class ReactionRolesNotSetup(commands.CommandError):
    """ Reaction roles are not setup for this guild """
    pass


def is_setup():
    async def wrap_func(ctx):
        data = await ctx.bot.config.find(ctx.guild.id)


