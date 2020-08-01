import discord
from discord.ext import commands


class notation(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command(
        name='Up',
        description='Notation command.',
        aliases=['up', 'UP', 'uP', 'U']
    )
    @commands.guild_only()
    async def up(self, ctx: commands.Context):
        up = discord.Embed(title="Up", color=0xADFF2F)
        up.add_field(name="Action", value="Rotate top face 90 degrees clockwise.", inline=False)
        up.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/738890956912459777/738891020862881819/U-Notation-Colored.png")
        up.set_footer(text='View from front face.')
        await ctx.send(embed=up)

    @commands.command(
        name="U'",
        description='Notation command.',
        aliases=[]
    )
    @commands.guild_only()
    async def upinverted(self, ctx: commands.Context):
        upr = discord.Embed(title="Up Inverted", color=0xADFF2F)
        upr.add_field(name="Action", value="Rotate top face 90 degrees anticlockwise.", inline=False)
        upr.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/738890956912459777/738891022636941394/U-Notation-Colored.png")
        upr.set_footer(text='View from front face.')
        await ctx.send(embed=upr)

    @commands.command(
        name='D',
        description='Notation command.',
        aliases=['down', 'Down', 'DOWN']
    )
    @commands.guild_only()
    async def down(self, ctx: commands.Context):
        down = discord.Embed(title="Down", color=0xADFF2F)
        down.add_field(name="Action", value="Rotate bottom face 90 degrees clockwise.", inline=False)
        down.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/738890956912459777/738891012549902356/D-Notation-Colored.png")
        down.set_footer(text='View from front face.')
        await ctx.send(embed=down)

    @commands.command(
        name="D'",
        description='Notation command.',
        aliases=[]
    )
    @commands.guild_only()
    async def downinverted(self, ctx: commands.Context):
        din = discord.Embed(title="Down Inverted", color=0xADFF2F)
        din.add_field(name="Action", value="Rotate bottom face 90 degrees anticlockwise.", inline=False)
        din.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/738890956912459777/738891014093406288/D-Notation-Colored.png")
        din.set_footer(text='View from front face.')
        await ctx.send(embed=din)

    @commands.command(
        name="L",
        description='Notation command.',
        aliases=['Left, left, LEFT']
    )
    @commands.guild_only()
    async def left(self, ctx: commands.Context):
        left = discord.Embed(title="Left", color=0xADFF2F)
        left.add_field(name="Action", value="Rotate left face 90 degrees clockwise.", inline=False)
        left.set_thumbnail(
            url="url=https://cdn.discordapp.com/attachments/738890956912459777/738891015217217616/L-Notation-Colored"
                ".png")
        left.set_footer(text='View from front face.')
        await ctx.send(embed=left)

    @commands.command(
        name="L'",
        description='Notation command',
        aliases=[]
    )
    @commands.guild_only()
    async def leftinverted(self, ctx: commands.Context):
        linv = discord.Embed(title="Left Inverted", color=0xADFF2F)
        linv.add_field(name="Action", value="Rotate left face 90 degrees anticlockwise.", inline=False)
        linv.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/738890956912459777/738891016752332840/L-Notation-Colored.png")
        linv.set_footer(text='View from front face.')
        await ctx.send(embed=linv)


def setup(client: commands.Bot):
    client.add_cog(notation(client))
