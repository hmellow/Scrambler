import discord
from discord.ext import commands


class Other(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command(
        name="test",
        aliases=["t", "T", "Test", "TEST"]
    )
    @commands.guild_only()
    @commands.is_owner()
    async def test(self, ctx: commands.Context):
        await ctx.send("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.")

    @commands.command(
        name="Alpha",
        aliases=['alpha', 'ALPHA']
    )
    @commands.guild_only()
    @commands.cooldown(2, 3, commands.BucketType.user)
    async def alpha(self, ctx: commands.Context):
        await ctx.send("This is for alpha to ask to put something idk man.")


def setup(client: commands.Bot):
    client.add_cog(Other(client))
