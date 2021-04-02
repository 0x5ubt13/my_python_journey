import platform
import discord
from discord.ext import commands


class Commands(commands.Cog, name="bot_commands"):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Commands Cog has been loaded!\n")

    @commands.command()
    async def stats(self, ctx):
        """ A useful command that displays bot statistics """
        python_version = platform.python_version()
        dpy_version = discord.__version__
        server_count = len(self.bot.guilds)
        member_count = len(set(self.bot.get_all_members()))

        embed = discord.Embed(title=f'{self.bot.user.name} Stats', description='\uFEFF', colour=ctx.author.colour, timestamp=ctx.message.created_at)

        embed.add_field(name='Bot Version:', value=0.2)
        embed.add_field(name='Python Version:', value=python_version)
        embed.add_field(name='Discord.py Version', value=dpy_version)
        embed.add_field(name='Total Guilds:', value=server_count)
        embed.add_field(name='Total Users:', value=member_count)

        embed.set_footer(text=f"Try harder! | {self.bot.user.name}")
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)

        await ctx.send(embed=embed)

    @commands.command(aliases=['disconnect', 'close', 'stopbot'])
    @commands.is_owner()
    async def logout(self, ctx):
        """ If you are the owner, you can manually kill the bot using this command """
        await ctx.send(f"Beep bop. Hey {ctx.author.mention}, I'm logging out now :wave:")
        await ctx.bot.logout()


def setup(bot):
    bot.add_cog(Commands(bot))



