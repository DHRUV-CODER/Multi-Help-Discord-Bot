from discord.ext import commands
import discord
import datetime
import aiohttp


class base64cmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def encode(self, ctx,*,encodetext):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get(
                        f"https://some-random-api.ml/base64?encode={encodetext}"
                ) as r:
                    data = await r.json()
                    embed=discord.Embed(title="Base 64 - Encoder", description=data["base64"])
                    embed.timestamp = datetime.datetime.utcnow()
                    await ctx.send(embed=embed)


    @commands.command()
    async def decode(self, ctx,*,encodetext):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get(
                        f"https://some-random-api.ml/base64?decode={encodetext}"
                ) as r:
                    data = await r.json()
                    embed=discord.Embed(title="Base 64 - Decoder", description=data["text"])
                    embed.timestamp = datetime.datetime.utcnow()
                    await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(base64cmd(bot))
