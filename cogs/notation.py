import discord
from discord.ext import commands


class Notation(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command(
        name='Up',
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
        aliases=['Left, left, LEFT']
    )
    @commands.guild_only()
    async def left(self, ctx: commands.Context):
        left = discord.Embed(title="Left", color=0xADFF2F)
        left.add_field(name="Action", value="Rotate left face 90 degrees clockwise.", inline=False)
        left.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/738890956912459777/738891015217217616/L-Notation-Colored.png")
        left.set_footer(text='View from front face.')
        await ctx.send(embed=left)

    @commands.command(
        name="L'",
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

    @commands.command(
        name='R',
        aliases=['Right', 'right', 'RIGHT']
    )
    @commands.guild_only()
    async def right(self, ctx: commands.Context):
        rgt = discord.Embed(title="Right", color=0xADFF2F)
        rgt.add_field(name="Action", value="Rotate right face 90 degrees clockwise.", inline=False)
        rgt.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/738890956912459777/738891018035921026/R-Notation-Colored.png")
        rgt.set_footer(text='View from front face.')
        await ctx.send(embed=rgt)

    @commands.command(
        name="R'",
        description='Notation command',
        aliases=[]
    )
    @commands.guild_only()
    async def rightinverted(self, ctx: commands.Context):
        rin = discord.Embed(title="Right Inverted", color=0xADFF2F)
        rin.add_field(name="Action", value="Rotate right face 90 degrees anticlockwise.", inline=False)
        rin.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/738890956912459777/738891019508121701/R-Notation-Colored.png")
        rin.set_footer(text='View from front face.')
        await ctx.send(embed=rin)

    @commands.command(
        name="Net",
        aliases=['net', 'NET', 'unfold', 'UNFOLD', 'Unfold']
    )
    @commands.guild_only()
    async def net(self, ctx: commands.Context):
        netm = discord.Embed(title="Net", color=0xADFF2F)
        netm.add_field(name="Right", value="Blue", inline=True)
        netm.add_field(name="Left", value="Green", inline=True)
        netm.add_field(name="Front", value="Red", inline=True)
        netm.add_field(name="Back", value="Orange", inline=True)
        netm.add_field(name="Top (Up)", value="White", inline=True)
        netm.add_field(name="Bottom (Down)", value="Yellow", inline=True)
        netm.set_image(
            url="https://cdn.discordapp.com/attachments/738890956912459777/738955476439662632/Cube_Net-Labeled.png")
        await ctx.send(embed=netm)

    @commands.command(
        name="E",
        aliases=['e']
    )
    @commands.guild_only()
    async def emid(self, ctx: commands.Context):
        mnot = discord.Embed(title="Horizontal Slice", color=0xADFF2F)
        mnot.add_field(name="Action",
                       value="Rotate the horizontal middle section of the cube 90 degrees to the right.", inline=False)
        mnot.add_field(name="Acknowledgements", value="Slice move.", inline=False)
        mnot.set_thumbnail(
          url="https://cdn.discordapp.com/attachments/738890956912459777/739892528521805986/E-Notation-Colored.png")
        mnot.set_footer(text='View from front face.')
        await ctx.send(embed=mnot)

    @commands.command(
        name="E'",
        aliases=["e'"]
    )
    @commands.guild_only()
    async def emidinv(self, ctx: commands.Context):
        mpr = discord.Embed(title="Horizontal Slice Inverted", color=0xADFF2F)
        mpr.add_field(name="Action",
                      value="Rotate the horizontal middle section of the cube 90 degrees to the left.", inline=False)
        mpr.add_field(name="Acknowledgements", value="Slice move.", inline=False)
        mpr.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/738890956912459777/739892527494332426/E-Notation-Colored.png")
        mpr.set_footer(text='View from front face.')
        await ctx.send(embed=mpr)

    @commands.command(
        name="M",
        aliases=["m"]
    )
    @commands.guild_only()
    async def mid(self, ctx: commands.Context):
        ems = discord.Embed(title="Vertical Slice", color=0xADFF2F)
        ems.add_field(name="Action",
                      value="Rotate the vertical middle section of the cube 90 degrees down.", inline=False)
        ems.add_field(name="Acknowledgements", value="Slice move.", inline=False)
        ems.set_thumbnail(url="https://cdn.discordapp.com/attachments/738890956912459777/739892524235358288/M"
                              "-Notation-Colored.png")
        ems.set_footer(text='View from front face.')
        await ctx.send(embed=ems)

    @commands.command(
        name="M'",
        aliases=["m'"]
    )
    @commands.guild_only()
    async def invertmid(self, ctx: commands.Context):
        ein = discord.Embed(title="Vertical Slice Inverted", color=0xADFF2F)
        ein.add_field(name="Action",
                      value="Rotate the vertical middle section of the cube 90 degrees up.", inline=False)
        ein.add_field(name="Acknowledgements", value="Slice move.", inline=False)
        ein.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/738890956912459777/739892528656154734/M-Notation-Colored.png")
        ein.set_footer(text='View from front face.')
        await ctx.send(embed=ein)

    @commands.command(
        name="u",
        aliases=[]
    )
    @commands.guild_only()
    async def doblu(self, ctx: commands.Context):
        debu = discord.Embed(title="Double Layer Up", color=0xADFF2F)
        debu.add_field(name="Action", value="Rotate top two layers 90 degrees clockwise", inline=False)
        debu.add_field(name="Acknowledgements", value="Double layer move.", inline=False)
        debu.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/738890956912459777/739926781548691566/ud-notation-colored.png")
        debu.set_footer(text='View from front face.')
        await ctx.send(embed=debu)

    @commands.command(
        name="u'",
        aliases=[]
    )
    @commands.guild_only()
    async def indu(self, ctx: commands.Context):
        indu = discord.Embed(title="Double Layer Up Inverted", color=0xADFF2F)
        indu.add_field(name="Action", value="Rotate top two layers 90 degrees anticlockwise", inline=False)
        indu.add_field(name="Acknowledgements", value="Double layer move.", inline=False)
        indu.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/738890956912459777/739926788976934944/ud-notation-colored.png")
        indu.set_footer(text='View from front face.')
        await ctx.send(embed=indu)

    @commands.command(
        name="d",
        aliases=[]
    )
    @commands.guild_only()
    async def dldow(self, ctx: commands.Context):
        dwn = discord.Embed(title="Double Layer Down", color=0xADFF2F)
        dwn.add_field(name="Action", value="Rotate bottom two layers 90 degrees clockwise", inline=False)
        dwn.add_field(name="Acknowledgements", value="Double layer move.", inline=False)
        dwn.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/738890956912459777/739926790570770582/dd-notation-colored.png")
        dwn.set_footer(text="View from front face.")
        await ctx.send(embed=dwn)

    @commands.command(
        name="d'",
        aliases=[]
    )
    @commands.guild_only()
    async def dddinv(self, ctx: commands.Context):
        ddinv = discord.Embed(title="Double Layer Down Inverted", color=0xADFF2F)
        ddinv.add_field(name="Action", value="Rotate bottom two layers 90 degrees anticlockwise.", inline=False)
        ddinv.add_field(name="Acknowledgements", value="Double layer move.", inline=False)
        ddinv.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/738890956912459777/739926786095317093/dd-notation-colored.png")
        ddinv.set_footer(text="View from front face.")
        await ctx.send(embed=ddinv)

    @commands.command(
        name="r",
        aliases=[]
    )
    @commands.guild_only()
    async def rar(self, ctx: commands.Context):
        rar = discord.Embed(title="Double Layer Right", color=0xADFF2F)
        rar.add_field(name="Action", value="Rotate right two layers 90 degrees clockwise.", inline=False)
        rar.add_field(name="Acknowledgements", value="Double layer move.", inline=False)
        rar.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/738890956912459777/739926784534904852/rd-notation-colored.png")
        rar.set_footer(text="View from front face.")
        await ctx.send(embed=rar)

    @commands.command(
        name="r'",
        aliases=[]
    )
    @commands.guild_only()
    async def rainv(self, ctx: commands.Context):
        rain = discord.Embed(title="Double Layer Right Inverted", color=0xADFF2F)
        rain.add_field(name="Action", value="Rotate right two layers 90 degrees anticlockwise.", inline=False)
        rain.add_field(name="Acknowledgements", value="Double layer move.", inline=False)
        rain.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/738890956912459777/739926787454402560/rd-notation-colored.png")
        rain.set_footer(text="View from front face.")
        await ctx.send(embed=rain)

    @commands.command(
        name="l",
        aliases=[]
    )
    @commands.guild_only()
    async def laul(self, ctx: commands.Context):
        lanm = discord.Embed(title="Double Layer Left", color=0xADFF2F)
        lanm.add_field(name="Action", value="Rotate left two layers 90 degrees clockwise.", inline=False)
        lanm.add_field(name="Acknowledgements", value="Double layer move.", inline=False)
        lanm.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/738890956912459777/739926791866548324/ld-notation-colored.png")
        lanm.set_footer(text="View from front face.")
        await ctx.send(embed=lanm)

    @commands.command(
        name="l'",
        aliases=[]
    )
    @commands.guild_only()
    async def lane(self, ctx: commands.Context):
        lma = discord.Embed(title="Double Layer Left Inverted", color=0xADFF2F)
        lma.add_field(name="Action", value="Rotate left two layers 90 degrees anticlockwise.", inline=False)
        lma.add_field(name="Acknowledgements", value="Double layer move.", inline=False)
        lma.set_thumbnail(url="")
        lma.set_footer(text="View from front face.")
        await ctx.send(embed=lma)


def setup(client: commands.Bot):
    client.add_cog(Notation(client))

# url="https://cdn.discordapp.com/attachments/738890956912459777/739926783016566804/ld-notation-colored.png")