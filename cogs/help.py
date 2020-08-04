import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command(
            name="help",
            aliases="Help,HELP"
    )
    @commands.guild_only()
    async def help(self, ctx: commands.Context):
        halp = discord.Embed(totle)


def setup(client: commands.Bot):
    client.add_cog(Help(client))
