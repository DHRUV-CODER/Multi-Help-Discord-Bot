import discord
from discord.ext import commands
import datetime
import urllib.request
import re
import random
import asyncio
from random import choice


class Common(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ping command

    
    @commands.command(aliases=['avatar'])
    async def av(self,ctx,*,member: discord.Member = None):  # set the member object to None
      if not member:  # if member is no mentioned
          member = ctx.message.author  # set member as the author
      userAvatar = member.avatar_url
      embed=discord.Embed(title="",colour=member.colour,description=f"Showing {member.mention}'s avatar")
      embed.set_image(url=userAvatar)
      embed.timestamp = datetime.datetime.utcnow()
      await ctx.send(embed=embed)
        

    @commands.command()
    async def ping(self,ctx):
        randommessage = ["smooth..","hitting around ","close on ","oof ","ezzz getting around"]
        embed=discord.Embed(title="",description=f"{random.choice(randommessage)} **{round(self.bot.latency * 1000)}** ms")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

    @commands.command()
    async def status(self,ctx,*,member: discord.Member = None):
      if not member:  # if member is no mentioned
          member = ctx.message.author
      if member.status == discord.Status.online:
        await ctx.send(f"{member.mention} Has kept 🟢 **{str(member.status)}** As Status.")
      elif member.status == discord.Status.offline:
        await ctx.send(f"{member.mention} Has kept ⚫ **{str(member.status)}** As Status or he is really offline 🙄")
      elif member.status == discord.Status.dnd:
        await ctx.send(f"{member.mention} Has kept 🔴 **{str(member.status)}** As Status.")
      elif member.status == discord.Status.idle:
        await ctx.send(f"{member.mention} Has kept 🟡 **{str(member.status)}** As Status.")


def setup(bot):
    bot.add_cog(Common(bot))
