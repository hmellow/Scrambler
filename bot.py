import discord
from secrets import TOKEN

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name="Maintinence."))



client.run(TOKEN)

