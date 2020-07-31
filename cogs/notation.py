import discord
from discord.ext import commands


class notation(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command()
    @commands.guild_only()
    async def u(self, ctx: commands.Context):
        up = discord.Embed(title="Up", color=0xADFF2F)
        up.add_field(name="Action", value="Rotate top face 90 degrees clockwise.", inline=False)
        up.set_thumbnail(url="https://cdn.discordapp.com/attachments/738890956912459777/738891020862881819/U-Notation-Colored.png")
        up.set_footer(text='View from front face.')
        await ctx.send(embed=up)

    @commands.command()
    @commands.guild_only()
    async def invertu(self, ctx: commands.Context):
        upr = discord.Embed(title="Up Inverted", color=0xADFF2F)
        upr.add_field(name="Action", value="Rotate top face 90 degrees anticlockwise.", inline=False)
        upr.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/738890956912459777/738891022636941394/U-Notation-Colored.png")
        upr.set_footer(text='View from front face.')
        await ctx.send(embed=upr)


def setup(client: commands.Bot):
    client.add_cog(notation(client))
