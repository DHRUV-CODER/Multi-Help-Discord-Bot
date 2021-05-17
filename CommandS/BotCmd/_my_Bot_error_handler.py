import discord
import datetime
from discord.ext import commands
import math

class FkError(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title=':x: Command Error', colour=0x992d22)
            embed.add_field(name='Error', value=error)
            embed.add_field(name='Guild', value=ctx.guild,inline=False)
            embed.add_field(name='Channel', value=ctx.channel)
            embed.add_field(name='User', value=ctx.author.mention)
            embed.add_field(name='Message', value=ctx.message.clean_content)
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed,delete_after=25)
            await ctx.message.delete()
        # elif isinstance(error, commands.CommandNotFound):
        #     embed = discord.Embed(title=':x: Command Error', colour=0x992d22)
        #     embed.add_field(name='Error', value=error)
        #     embed.add_field(name='Guild', value=ctx.guild,inline=False)
        #     embed.add_field(name='Channel', value=ctx.channel)
        #     embed.add_field(name='User', value=ctx.author.mention)
        #     embed.add_field(name='Message', value=ctx.message.clean_content)
        #     embed.timestamp = datetime.datetime.utcnow()
        #     await ctx.send(embed=embed,delete_after=25)
        #     await ctx.message.delete()
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(title=':x: Command Error', colour=0x992d22)
            embed.add_field(name='Error', value=error)
            embed.add_field(name='Guild', value=ctx.guild,inline=False)
            embed.add_field(name='Channel', value=ctx.channel)
            embed.add_field(name='User', value=ctx.author.mention)
            embed.add_field(name='Message', value=ctx.message.clean_content)
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed,delete_after=25)
            await ctx.message.delete()
        elif isinstance(error, commands.MissingRole):
            embed = discord.Embed(title=':x: Command Error', colour=0x992d22)
            embed.add_field(name='Error', value=error)
            embed.add_field(name='Guild', value=ctx.guild,inline=False)
            embed.add_field(name='Channel', value=ctx.channel)
            embed.add_field(name='User', value=ctx.author.mention)
            embed.add_field(name='Message', value=ctx.message.clean_content)
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed,delete_after=25)
            await ctx.message.delete()
        # elif isinstance(error, commands.CommandInvokeError):   
        #   await ctx.send(f"```fix\n-{error}\n```")         
        elif isinstance(error, commands.CommandOnCooldown):
          # await ctx.send(f"{error} ")
          cooldown_time = str(datetime.timedelta(seconds=math.trunc(error.retry_after)))
          if cooldown_time == "0:00:00":
            await ctx.send("ik you are too desperate wait for 1 sec atleast")
          elif cooldown_time == "0:00:01":
            await ctx.send("ik you are too desperate wait for 1 sec atleast")
          else:
            await ctx.send(f"Fam You Are On Cooldown . Wait For like  {cooldown_time}")
        else:
            raise error



def setup(bot):
    bot.add_cog(FkError(bot))
