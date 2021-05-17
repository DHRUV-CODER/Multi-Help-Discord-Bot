import discord
from discord.ext import commands
import aiohttp


class MEme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    # @commands.cooldown(3, 5.0, commands.BucketType.user)
    async def meme(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://meme-api.herokuapp.com/gimme/meme") as r:
                    data = await r.json()
                    if data['nsfw'] == False:
                        embed = discord.Embed(title=data['title'])
                        embed.set_image(url=data['url'])
                        embed.set_footer(text="👍 -> {}".format(data['ups']))
                        await ctx.send(embed=embed)
                        # print(data['nsfw'])
                        # await ctx.send(data['nsfw'])
                    else:
                        print(data['nsfw'])
                        await ctx.send("Sorry Ig That Had Some NSFW Content")
    @meme.error
    async def meme_error(self,ctx, error):
        if isinstance(error, commands.errors.CommandOnCooldown):
          await ctx.send(f"{ctx.author.mention} \n ik u are desperate but stop the spam my fam \n here is you punishment ")

def setup(bot):
    bot.add_cog(MEme(bot))
