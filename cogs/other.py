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
        alp = discord.Embed(title="Click here to learn more!", url="https://bit.ly/2PZ6eR7", color=0x6b00ff)
        await ctx.send(embed=alp)

    @commands.command(
        name="purge",
        aliases=['Purge', 'PURGE', 'clean', 'Clean', 'CLEAN']
    )
    @commands.guild_only()
    @commands.has_guild_permissions(manage_messages=True)
    async def purge(self, ctx: commands.Context, amt=10):
        await ctx.channel.purge(limit=amt)


def setup(client: commands.Bot):
    client.add_cog(Other(client))
