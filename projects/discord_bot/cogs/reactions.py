import discord
import emojis
import typing
from discord.ext import commands


class ReactionRolesNotSetup(commands.CommandError):
    """ Reaction roles are not setup for this guild """
    pass


def is_setup():
    async def wrap_func(ctx):
        data = await ctx.bot.config.find(ctx.guild.id)
        if data is None:
            raise ReactionRolesNotSetup

        if data.get("message_id") is None:
            raise ReactionRolesNotSetup

        return True
    return commands.check(wrap_func)


class Reactions(commands.Cog, name="ReactionRoles"):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(
        aliases=['rr'], invoke_without_command=True
    )
    @commands.guild_only()
    async def reactionroles(self, ctx):
        await ctx.invoke(self.bot.get_command("help"), entity="reactionroles")

    @reactionroles.command(name="channel")
    @commands.guild_only()
    @commands.has_guild_permissions(manage_channels=True)
    async def rr_channel(self, ctx, channel: discord.TextChannel = None):
        if channel is None:
            await ctx.send("You didn't give me a channel, so I'll use the current one!")

        channel = channel or ctx.channel
        try:
            await channel.send("testing whether I can send messages here", delete_after=0.05)
        except discord.HTTPException:
            await ctx.send("I can't send a message to that channel! Please give me permissions and try again")
            return

        embed = discord.Embed(title="Reaction Roles!!")

        desc = ""
        reaction_roles = await self.bot.reaction_roles.get
        reaction_roles = list(filter(lambda r: r['guild_id'] == ctx.guild.id, reaction_roles))
        for item in reaction_roles:
            role = ctx.guild.get_role(item["role"])
            desc += f"{item['_id']}: {role.mention}\n"
        embed.description = desc

        m = await channel.send(embed=embed)
        for item in reaction_roles:
            await m.add_reaction(item['_id'])

        await self.bot.config.upsert(
            {
                "_id": ctx.guild.id,
                "message_id": m.id,
                "channel_id": m.channel.id,
                "is_enabled": True,
            }
        )


def setup(bot):
    bot.add_cog(Reactions(bot))
