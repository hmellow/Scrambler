import discord
from secrets import TOKEN
from discord.ext import commands

client = commands.Bot(command_prefix="*")


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name="EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"))


# Notation u or just u
# Find a way to make aliases
@client.command()
async def u(ctx: commands.Context):
    up = discord.Embed(title="Up", color=0xADFF2F)
    up.add_field(name="Action", value="Rotate top face 90 degrees clockwise.", inline=False)
    up.set_thumbnail(url="https://cdn.discordapp.com/attachments/738890956912459777/738891020862881819/U-Notation-Colored.png")
    up.set_footer(text='View from front face.')
    await ctx.send(embed=up)


@client.command()
async def upprime(ctx: commands.Context):
    upr = discord.Embed(title="Up Inverted", color=0xADFF2F)
    upr.add_field(name="Action", value="Rotate top face 90 degrees anticlockwise.", inline=False)
    upr.set_thumbnail(url="https://cdn.discordapp.com/attachments/738890956912459777/738891022636941394/U-Notation-Colored.png")
    upr.set_footer(text='View from front face.')
    await ctx.send(embed=upr)


client.run(TOKEN)
