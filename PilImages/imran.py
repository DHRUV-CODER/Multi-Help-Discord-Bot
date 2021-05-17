import discord
from discord.ext import commands
import datetime
import asyncio
import random
from PIL import Image
from io import BytesIO


class selfiewithimran(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def imran(self, ctx, user: discord.Member = None):
        # if not user:
        #     user = ctx.author

        # wanted = Image.open("./images/imran.jpg")

        # asset = user.avatar_url_as(size=128)
        # data = BytesIO(await asset.read())
        # pfp = Image.open(data)

        # pfp = pfp.resize((236,285))
        # wanted.paste(pfp, (395,3))

        # wanted.save("./finalimages/selfie.jpg")

        # await ctx.send(file=discord.File("./finalimages/selfie.jpg"))
        await ctx.send("aww cmd closed doesnt make sense with bot 🙄,wanna talk to devloper use **?message**")


def setup(bot):
    bot.add_cog(selfiewithimran(bot))
