# Import Discord.py and all the other shit to make it work
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

client = commands.Bot(command_prefix='p!')


# Startup. Sends message in console and discord
@client.event
async def on_ready():
    activity = discord.Activity(type=discord.ActivityType.watching, name="private channels")
    await client.change_presence(status=discord.Status.online, activity=activity)
    print('========================')
    print('✅ Logged in as')
    print("Name: " + client.user.name)
    print("Id: " + str(client.user.id))
    print("Wasting my resources in " + f"{len(client.guilds)} servers! (╯°□°）╯︵ ┻━┻")
    print('========================')

# Load Cog
@client.command()
async def load(ctx, extension):
    if ctx.author.id == 322708417540259841:
        client.load_extension(f'cogs.{extension}')
        my_embed = discord.Embed(title=":white_check_mark: Command load complete",
                                 description="Loaded " + f'{extension}!', color=0x6136c2)
        await ctx.send(embed=my_embed)
    else:
        my_embed = discord.Embed(title=":x: Error", description="Only the bot owner can use this command",
                                 color=0x6136c2)
        await ctx.send(embed=my_embed)


# Reload Cog
@client.command()
async def reload(ctx, extension):
    if ctx.author.id == 322708417540259841:
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')
        my_embed = discord.Embed(title=":white_check_mark: Command reload complete",
                                 description="Reloaded " + f'{extension}!', color=0x6136c2)
        await ctx.send(embed=my_embed)
    else:
        my_embed = discord.Embed(title=":x: Error", description="Only the bot owner can use this command",
                                 color=0x6136c2)
        await ctx.send(embed=my_embed)


# Unload Cog
@client.command()
async def unload(ctx, extension):
    if ctx.author.id == 322708417540259841:
        client.unload_extension(f'cogs.{extension}')
        my_embed = discord.Embed(title=":white_check_mark: Command unload complete",
                                 description="Unloaded " + f'{extension}!', color=0x6136c2)
        await ctx.send(embed=my_embed)
    else:
        my_embed = discord.Embed(title=":x: Error", description="Only the bot owner can use this command",
                                 color=0x6136c2)
        await ctx.send(embed=my_embed)


# Read Cogs folder and load them
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run(os.getenv("BOT_TOKEN"))
