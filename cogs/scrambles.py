import discord
from discord.ext import commands


class Scrambles(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client


    @commands.command(
        name="",
        aliases=
    )
    @commands.guild_only()
    async def scram3x3



def setup(client: commands.Bot):
    client.add_cog(Scrambles(client))