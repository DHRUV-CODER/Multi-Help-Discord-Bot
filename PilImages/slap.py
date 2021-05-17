import discord
from discord.ext import commands
import datetime
import asyncio
import random
from PIL import Image
from io import BytesIO


class Pewd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def slap(self,ctx, guy_who_wants_to_get_slapped: discord.Member ):

        user = ctx.author

        slap1 = Image.open("./images/slap.jpg")

        asset = user.avatar_url_as(size = 128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)

        pfp = pfp.resize((245,261))
        slap1.paste(pfp, (453,7))
        
        slap1.save("./images/slap1.jpg")
        

        slap2 = Image.open("./images/slap1.jpg")

        asset = guy_who_wants_to_get_slapped.avatar_url_as(size = 128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)

        pfp = pfp.resize((301,303))
        slap2.paste(pfp, (3,439))
        
        slap2.save("./finalimages/slap2.jpg")
        
        await ctx.send(file = discord.File("./finalimages/slap2.jpg"))


def setup(bot):
    bot.add_cog(Pewd(bot))
