# Required to use
from discord.ext import commands
import discord


class DevOnly(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Commands
    @commands.command()
    async def shutdown(self, ctx):
        if ctx.author.id == 322708417540259841:
            myembed = discord.Embed(title=":wave:", description='See you next time', color=0x6136c2)
            await ctx.send(embed=myembed)
            quit()
        else:
            # Give troll to people trying to shutdown the bot
            myembed = discord.Embed(title="<:ohgod:815152759934287872>", description='Hey guys, did you know that in '
                                                                                     'terms of male human and female '
                                                                                     'Pokémon breeding, Vaporeon is '
                                                                                     'the most compatible Pokémon for '
                                                                                     'humans? Not only are they in '
                                                                                     'the field egg group, '
                                                                                     'which is mostly comprised of '
                                                                                     'mammals, Vaporeon are an '
                                                                                     'average of 3”03’ tall and 63.9 '
                                                                                     'pounds, this means they’re '
                                                                                     'large enough to be able handle '
                                                                                     'human d##ks, and with their '
                                                                                     'impressive Base Stats for HP '
                                                                                     'and access to Acid Armor, '
                                                                                     'you can be rough with one. Due '
                                                                                     'to their mostly water based '
                                                                                     'biology, there’s no doubt in my '
                                                                                     'mind that an aroused Vaporeon '
                                                                                     'would be incredibly wet, '
                                                                                     'so wet that you could easily '
                                                                                     'have s*x with one for hours '
                                                                                     'without getting sore. They can '
                                                                                     'also learn the moves Attract, '
                                                                                     'Baby-Doll Eyes, Captivate, '
                                                                                     'Charm, and Tail Whip, '
                                                                                     'along with not having fur to '
                                                                                     'hide n###les, so it’d be '
                                                                                     'incredibly easy for one to get '
                                                                                     'you in the mood. With their '
                                                                                     'abilities Water Absorb and '
                                                                                     'Hydration, they can easily '
                                                                                     'recover from fatigue with '
                                                                                     'enough water. No other Pokémon '
                                                                                     'comes close to this level of '
                                                                                     'compatibility. Also, fun fact, '
                                                                                     'if you pull out enough, '
                                                                                     'you can make your Vaporeon turn '
                                                                                     'white. Vaporeon is literally '
                                                                                     'built for human d##k. Ungodly '
                                                                                     'defense stat+high HP pool+Acid '
                                                                                     'Armor means it can take c##k '
                                                                                     'all day, all shapes and sizes '
                                                                                     'and still come for more'
                                                                                     ''
                                                                                     'Please dont run developer '
                                                                                     'commands '
                                    ,
                                    color=0x6136c2)
            await ctx.send(embed=myembed)


# Ending code
def setup(client):
    client.add_cog(DevOnly(client))
