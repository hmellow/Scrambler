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
        scram = Scram(3, 3, 17, 25)
        scram.scram()
        scram.convert()

        s3 = "**" + scram.scramble + "**"

        await ctx.send(s3)

    @commands.command(
        name="2x2",
        aliases=['2', '2X2', '2x', '2X', 'Two', 'two', 'TWO']
    )
    @commands.guild_only()
    async def scram2x2(self, ctx: commands.Context):
        scram = Scram(2, 2, 9, 10)
        scram.scram()
        scram.convert()

        s3 = "**" + scram.scramble + "**"

        await ctx.send(s3)

    @commands.command(
        name="1x1",
        aliases=['1', '1X1', '1x', '1X', 'One', 'one', 'ONE']
    )
    @commands.guild_only()
    async def scr1(self, ctx: commands.Context):
        await ctx.send("No. That's stupid.")


def setup(client: commands.Bot):
    client.add_cog(Scrambles(client))
