import discord
from discord.ext import commands
import aiohttp
import datetime
import io
import time


class Filter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def wasted(self,ctx, member: discord.Member=None):
        member = member or ctx.author
        async with aiohttp.ClientSession() as ses:
            async with ses.get(f"https://some-random-api.ml/canvas/wasted?avatar={member.avatar_url_as(format='png')}") as r:
                if r.status in range(200, 299):
                  data = io.BytesIO(await r.read())
                  await ctx.send(file=discord.File(data, 'wasted.jpg'))
                  await ses.close()
                else:
                  await ctx.send('encountered error')

    @commands.command()
    async def gay(self,ctx, member: discord.Member=None):
        member = member or ctx.author
        async with aiohttp.ClientSession() as ses:
            async with ses.get(f"https://some-random-api.ml/canvas/gay?avatar={member.avatar_url_as(format='png')}") as r:
                if r.status in range(200, 299):
                  data = io.BytesIO(await r.read())
                  await ctx.send(file=discord.File(data, 'gay.jpg'))
                  await ses.close()
                else:
                  await ctx.send('encountered error')

    @commands.command()
    async def trigger(self,ctx, member: discord.Member=None):
        member = member or ctx.author
        async with aiohttp.ClientSession() as ses:
            async with ses.get(f"https://some-random-api.ml/canvas/triggered?avatar={member.avatar_url_as(format='png')}") as r:
                if r.status in range(200, 299):
                  data = io.BytesIO(await r.read())
                  await ctx.send(file=discord.File(data, 'trigger.gif'))
                  await ses.close()
                else:
                  await ctx.send('encountered error')



    @commands.command()
    async def glass(self,ctx, member: discord.Member=None):
        member = member or ctx.author
        async with aiohttp.ClientSession() as ses:
            async with ses.get(f"https://some-random-api.ml/canvas/glass?avatar={member.avatar_url_as(format='png')}") as r:
                if r.status in range(200, 299):
                  data = io.BytesIO(await r.read())
                  await ctx.send(file=discord.File(data, 'glass.jpg'))
                  await ses.close()
                else:
                  await ctx.send('encountered error')

    @commands.command()
    async def sepia(self,ctx, member: discord.Member=None):
        member = member or ctx.author
        async with aiohttp.ClientSession() as ses:
            async with ses.get(f"https://some-random-api.ml/canvas/sepia?avatar={member.avatar_url_as(format='png')}") as r:
                if r.status in range(200, 299):
                  data = io.BytesIO(await r.read())
                  await ctx.send(file=discord.File(data, 'sepia.jpg'))
                  await ses.close()
                else:
                  await ctx.send('encountered error')

    @commands.command()
    async def bloddy(self,ctx, member: discord.Member=None):
        member = member or ctx.author
        async with aiohttp.ClientSession() as ses:
            async with ses.get(f"https://some-random-api.ml/canvas/red?avatar={member.avatar_url_as(format='png')}") as r:
                if r.status in range(200, 299):
                  data = io.BytesIO(await r.read())
                  await ctx.send(file=discord.File(data, 'sepia.jpg'))
                  await ses.close()
                else:
                  await ctx.send('encountered error')

    @commands.command()
    async def comment(self,ctx,*,comment="no comment", member: discord.Member=None):
        member = member or ctx.author
        async with aiohttp.ClientSession() as ses:
            async with ses.get(f"https://some-random-api.ml/canvas/youtube-comment?avatar={member.avatar_url_as(format='png')}&comment={comment}&username={ctx.author}") as r:
                if r.status in range(200, 299):
                  data = io.BytesIO(await r.read())
                  await ctx.send(file=discord.File(data, 'commmentedd.jpg'))
                  await ses.close()
                else:
                  await ctx.send('encountered error')



def setup(bot):
    bot.add_cog(Filter(bot))