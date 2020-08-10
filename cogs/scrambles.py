from discord.ext import commands
import random
from scrambles.scram import Scram


class Scrambles(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command(
        name="3x3",
        aliases=['3', '3X3', '3x', '3X', 'Three', 'three', 'THREE']
    )
    @commands.guild_only()
    async def scram3x3(self, ctx: commands.Context):

        scram = Scram({'moves': (('U', 'D'), ('F', 'B'), ('R', 'L')), 'directions': ('', "'", '2')}, 17, 25)
        scram.scram()
        scram.convert()

        s3 = "**" + convert(scram.scramble) + "**"

        await ctx.send(s3)


def setup(client: commands.Bot):
    client.add_cog(Scrambles(client))
