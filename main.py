import discord
from secrets import TOKEN
from discord.ext import commands
import os
import traceback

client = commands.Bot(command_prefix="*")


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name="EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"))


if __name__ == '__main__':
    for file in os.listdir("cogs"):
        if file.endswith(".py"):
            try:
                client.load_extension(f"cogs.{file[:-3]}")
            except (discord.ClientException, ModuleNotFoundError):
                print(traceback.format_exc())


client.run(TOKEN)
