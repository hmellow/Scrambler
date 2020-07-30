import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name="Maintinence."))

client.run('NzAzMDc5MzgzNDcyMjc1NTA4.XqJXsw.5TwV1Gd_oVAWxeMsYe2V7TqGbF8')

