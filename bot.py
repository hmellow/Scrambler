import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='/')


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))


    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

# token = os.environ.get("token")


client = MyClient()


client.run('NzAzMDc5MzgzNDcyMjc1NTA4.XsWQWw.5084K3AU3IYTHlksEPpWwOxWRIw')
# Startup

