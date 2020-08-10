import discord
from discord.ext import commands


class Scrambles(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client


    @commands.command(
        name="3x3",
        aliases=['3', '3X3', '3x', '3X', 'Three', 'three', 'THREE']
    )
    @commands.guild_only()
    async def scram3x3(self, ctx: commands.Context):
        # Make a variable called s3x then set it to the generated scramble. Uncomment line below and delete this one.
        # ctx.send(s3x)



def setup(client: commands.Bot):
    client.add_cog(Scrambles(client))