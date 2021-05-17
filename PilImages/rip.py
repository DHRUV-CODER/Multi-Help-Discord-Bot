import discord
from discord.ext import commands
import datetime
import asyncio
import random
from PIL import Image
from io import BytesIO


class ded(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rip(self, ctx, user: discord.Member = None):
        if not user:
            user = ctx.author

        wanted = Image.open("./images/ded.jpg")

        asset = user.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)

        pfp = pfp.resize((154,157))
        wanted.paste(pfp, (92,212))

        wanted.save("./finalimages/rip.jpg")

        await ctx.send(file=discord.File("./finalimages/rip.jpg"))


def setup(bot):
    bot.add_cog(ded(bot))
