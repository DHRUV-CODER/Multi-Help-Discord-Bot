import random
import aiohttp
from discord.ext import commands
import discord
import requests
class Images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cat(self, ctx):
        url = 'https://some-random-api.ml/img/cat'
        res = requests.get(url)
        json = res.json()
        result = json['link']
        fact = requests.get('https://some-random-api.ml/facts/cat').json()       
        embed = discord.Embed(title=fact['fact'])
        embed.set_image(url=result)

        await ctx.send(embed=embed)



    @commands.command()
    async def dog(self, ctx):        
        url = 'https://some-random-api.ml/img/dog'
        res = requests.get(url)
        json = res.json()
        result = json['link']
        fact = requests.get('https://some-random-api.ml/facts/dog').json()       
        embed = discord.Embed(title=fact['fact'])
        embed.set_image(url=result)

        await ctx.send(embed=embed)  


    @commands.command()
    async def fox(self, ctx):
        url = 'https://some-random-api.ml/img/fox'
        res = requests.get(url)
        json = res.json()
        result = json['link']       
        fact = requests.get('https://some-random-api.ml/facts/fox').json()       
        embed = discord.Embed(title=fact['fact'])
        embed.set_image(url=result)

        await ctx.send(embed=embed)

    @commands.command()
    async def panda(self, ctx):
        url = 'https://some-random-api.ml/img/panda'
        res = requests.get(url)
        json = res.json()
        result = json['link']       
        fact = requests.get('https://some-random-api.ml/facts/panda').json()       
        embed = discord.Embed(title=fact['fact'])
        embed.set_image(url=result)

        await ctx.send(embed=embed)



    @commands.command()
    async def bird(self, ctx):
        url = 'https://some-random-api.ml/img/birb'
        res = requests.get(url)
        json = res.json()
        result = json['link']       
        fact = requests.get('https://some-random-api.ml/facts/bird').json()       
        embed = discord.Embed(title=fact['fact'])
        embed.set_image(url=result)

        await ctx.send(embed=embed)

    @commands.command()
    async def rp(self, ctx):
        url = 'https://some-random-api.ml/img/red_panda'
        res = requests.get(url)
        json = res.json()
        result = json['link']       
        fact = requests.get('https://some-random-api.ml/facts/panda').json()       
        embed = discord.Embed(title=fact['fact'])
        embed.set_image(url=result)

        await ctx.send(embed=embed)
    @commands.command()
    async def koala(self, ctx):
        url = 'https://some-random-api.ml/img/koala'
        res = requests.get(url)
        json = res.json()
        result = json['link']       
        fact = requests.get('https://some-random-api.ml/facts/koala').json()       
        embed = discord.Embed(title=fact['fact'])
        embed.set_image(url=result)

        await ctx.send(embed=embed)  

    @commands.command()
    async def kangaroo(self, ctx):
        url = 'https://some-random-api.ml/img/kangaroo'
        res = requests.get(url)
        json = res.json()
        result = json['link']       
        fact = requests.get('https://some-random-api.ml/facts/kangaroo').json()       
        embed = discord.Embed(title=fact['fact'])
        embed.set_image(url=result)

        await ctx.send(embed=embed)

    @commands.command()
    async def racoon(self, ctx):
        url = 'https://some-random-api.ml/img/racoon'
        res = requests.get(url)
        json = res.json()
        result = json['link']       
        fact = requests.get('https://some-random-api.ml/facts/racoon').json()       
        embed = discord.Embed(title=fact['fact'])
        embed.set_image(url=result)

        await ctx.send(embed=embed)
                               
    @commands.command()
    async def whale(self, ctx):
        url = 'https://some-random-api.ml/img/whale'
        res = requests.get(url)
        json = res.json()
        result = json['link']       
        fact = requests.get('https://some-random-api.ml/facts/whale').json()       
        embed = discord.Embed(title=fact['fact'])
        embed.set_image(url=result)

        await ctx.send(embed=embed)


      

def setup(bot):
    bot.add_cog(Images(bot))
