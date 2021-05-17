import discord
from discord.ext import commands
import datetime

class SupportHere(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def message(self, ctx, *, message):
        # channel = self.bot.get_channel(809419973544902717)
        if len(message) > 1024:
            await ctx.send(f"Less Than **1024** Words ;/ {ctx.author.mention}")
        elif len(message) < 50:
            await ctx.send(
                f"Your Message Should Be More Than 100 Words {ctx.author.mention}"
            )
        else:
            channel = self.bot.get_channel(809419973544902717)
            embed = discord.Embed(title='Message By:',
                                  description=f"{ctx.author.mention}")
            embed.add_field(name='Message', value=message)
            embed.timestamp = datetime.datetime.utcnow()
            await channel.send(embed=embed)
            await ctx.message.delete()
            await ctx.send(
                f"{ctx.author.mention} Your Message Was Sent Successfully This is how it looks like",
                delete_after=25)
            await ctx.send(embed=embed, delete_after=25)
            await ctx.send(
                "Message Can Be Found Here https://discord.gg/PWGVdBDvvK",
                delete_after=25)

def setup(bot):
    bot.add_cog(SupportHere(bot))
