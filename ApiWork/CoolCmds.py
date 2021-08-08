import discord
from discord.ext import commands
import aiohttp
from discord import Webhook, AsyncWebhookAdapter
import aiohttp
import datetime
import io
import time
import requests
import os
my_secret = os.environ['WB_SECREAT']

class CoolCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def wink(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get(
                        "https://some-random-api.ml/animu/wink") as r:
                    data = await r.json()

                    embed = discord.Embed(title="😉")
                    embed.set_image(url=data['link'])
                    

                    await ctx.send(embed=embed)

    @commands.command()
    async def hug(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://some-random-api.ml/animu/hug") as r:
                    data = await r.json()

                    embed = discord.Embed(title="")
                    embed.set_image(url=data['link'])

                    await ctx.send(embed=embed)

    @commands.command()
    async def pat(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://some-random-api.ml/animu/pat") as r:
                    data = await r.json()

                    embed = discord.Embed(title="")
                    embed.set_image(url=data['link'])

                    await ctx.send(embed=embed)

    @commands.command(aliases=["face_palm"])
    async def fp(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://some-random-api.ml/animu/face-palm") as r:
                    data = await r.json()

                    embed = discord.Embed(title="")
                    embed.set_image(url=data['link'])

                    await ctx.send(embed=embed)

    @commands.command()
    async def wb(self,ctx,*,msg="no msg"):
        # await ctx.message.delete()
        async with aiohttp.ClientSession() as session:
            # await ctx.channel.create_webhook(name="mywebhook")
            webhook = Webhook.from_url(f'https://discord.com/api/webhooks/855005984719896576/{my_secret}', adapter=AsyncWebhookAdapter(session))
            msg1 = msg.replace("@everyone","everyone")
            message = msg1.replace("@here","here")
            await webhook.send(f'{message} \n\n\n**Message Sent From** \n{ctx.guild.name}', username=f"{ctx.author.name}", avatar_url=ctx.author.avatar_url)
                    
def setup(bot):
    bot.add_cog(CoolCmd(bot))
