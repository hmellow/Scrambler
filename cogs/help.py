import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command(
            name="help",
            aliases=["Help","HELP"]
    )
    @commands.guild_only()
    async def help(self, ctx: commands.Context):
        halp = discord.Embed(title="Help (Categories)", color=0xADFF2F)
        halp.add_field(name="Notation", value="\a", inline=False)
        halp.add_field(name="Information", value="\a", inline=False)
        halp.add_field(name="Scrambles", value="Coming soon.", inline=False)
        halp.set_footer(text="Do *help category name for lists of commands.")
        await ctx.send(embed=halp)


def setup(client: commands.Bot):
    client.add_cog(Help(client))
