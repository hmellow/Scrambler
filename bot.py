import discord
from secrets import TOKEN

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name="EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"))
    reference_embed = discord.Embed(title="Up", color=0xADFF2F)
    reference_embed.add_field(name="Action", value="Rotate top face 90 degrees clockwise.", inline=False)
    reference_embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/738527822473068604/738821000011186296/U.png")
    reference_embed.set_footer(text='Notation')
    channel = client.get_channel(703071528882929748)
    await channel.send(embed=reference_embed)

client.run(TOKEN)