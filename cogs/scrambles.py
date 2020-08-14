from discord.ext import commands
import random
from scrambles.scram import Scram


class Scrambles(commands.Cog, Scram):
    def __init__(self, client: commands.Bot):
        self.client = client
    # 4x4:
    @commands.command(
        name="4x4",
        aliases=['4', '4X4', '4x', '4X', 'Four', 'four', 'FOUR']
    )
    @commands.guild_only()
    @commands.cooldown(2, 3, commands.BucketType.user)
    async def scram4(self, ctx: commands.Context):
        self.scram(4, 4, 42, 49)

        s4 = "**" + self.convert() + "**"

        await ctx.send(s4)
    # 3x3:
    @commands.command(
        name="3x3",
        aliases=['3', '3X3', '3x', '3X', 'Three', 'three', 'THREE']
    )
    @commands.guild_only()
    @commands.cooldown(2, 3, commands.BucketType.user)
    async def scram3x3(self, ctx: commands.Context):
        self.scram(3, 3, 17, 25)

        s3 = "**" + self.convert() + "**"

        await ctx.send(s3)
    # 2x2:
    @commands.command(
        name="2x2",
        aliases=['2', '2X2', '2x', '2X', 'Two', 'two', 'TWO']
    )
    @commands.guild_only()
    @commands.cooldown(2, 3, commands.BucketType.user)
    async def scram2x2(self, ctx: commands.Context):
        self.scram(2, 2, 9, 10)

        s2 = "**" + self.convert() + "**"

        await ctx.send(s2)
    # 1x1:
    @commands.command(
        name="1x1",
        aliases=['1', '1X1', '1x', '1X', 'One', 'one', 'ONE']
    )
    @commands.guild_only()
    @commands.cooldown(2, 3, commands.BucketType.user)
    async def scr1(self, ctx: commands.Context):
        await ctx.send("No. That's stupid.")

    @commands.command(
        name='5x5',
        aliases=['5', '5X5', '5x', '5X', 'Five', 'five', 'FIVE']
    )
    @commands.guild_only()
    @commands.cooldown(2, 3, commands.BucketType.user)
    async def scr5(self, ctx: commands.Context):
        self.scram(5, 5, 60, 60)

        s5 = "**" + self.convert() + "**"

        await ctx.send(s5)

    @commands.command(
        name='Skewb',
        aliases=['skewb', 'SKEWB']
    )
    @commands.guild_only()
    @commands.cooldown(2, 3, commands.BucketType.user)
    async def skewb(self, ctx: commands.Context):
        self.scram(37, 37, 8, 9)

        sk = "**" + self.convert() + "**"

        await ctx.send(sk)

    @commands.command(
        name="Megaminx",
        aliases=['megaminx', 'MEGAMINX', 'mega', 'MEGA', 'Mega', 'dodecahedron', 'Dodecahedron', 'DODECAHEDRON']
    )
    @commands.guild_only()
    @commands.cooldown(2, 3, commands.BucketType.user)
    async def mega(self, ctx: commands.Context):
        self.scram(41, 41, 10, 10)

        mga = self.convert()

        self.scram(42, 42, 1, 1)

        mga2 = self.convert()

        mg = "**" + mga + " " + mga2 + "**"

        await ctx.send(mg)

#    @commands.command(
#        name='Pyraminx',
#        aliases=['pyraminx', 'PYRAMINX', 'PYRA', 'pyra', 'Pyra', 'Pyramid', 'PYRAMID', 'pyramid']
#    )
#    @commands.guild_only()
#    @commands.cooldown(2, 3, commands.BucketType.user)
#    async def pyra(self, ctx: commands.Context):
#        self.scram(38, 38, 8, 9)


def setup(client: commands.Bot):
    client.add_cog(Scrambles(client))
