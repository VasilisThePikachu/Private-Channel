# Required to use
import discord
from discord.ext import commands


class Bot(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Commands
    @commands.command()
    async def ping(self, ctx):
        myembed = discord.Embed(title="Ping info", description=f'Pong! {round(self.client.latency * 1000)}ms', color=0x6136c2)
        await ctx.send(embed=myembed)


# Ending code
def setup(client):
    client.add_cog(Bot(client))
