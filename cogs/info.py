import discord
from discord.ext import commands


class Info(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command(
        name="ping",
        aliases=['latency, Ping, Latency']
    )
    @commands.guild_only()
    async def ping(self, ctx: commands.Context):
        await ctx.send(f"Latency: **{round(self.client.latency * 1000)}ms**")

    @commands.command(
        name="invite",
        aliases=['Invite']
    )
    @commands.guild_only()
    async def invite(self, ctx: commands.Context):
        await ctx.send("**PineCube server invite:** https://discord.gg/55nrRkr")


def setup(client: commands.Bot):
    client.add_cog(Info(client))
