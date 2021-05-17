import discord
from discord.ext import commands
import DiscordUtils

class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pagapi(self,ctx):
        embed1 = discord.Embed(color=ctx.author.color,description="```yaml\nThere Are 2 Commands In Here\n\nAlways Put Prefix Before Every Command\n```").add_field(name="Fort", value="```fix\nUsed As\nEg:- fort ninja\n```").add_field(name="Fort Code", value="```fix\nUsed As\nEg:- fortcode ninja\n```").set_footer(text="1/6")
        embed2 = discord.Embed(color=ctx.author.color,description="```yaml\nThere Are 10 Commands In Here\nFor Futher help Type 'apihelp'\nAlways Put Prefix Before Every Command\n```").add_field(name="Returns Animal images", value="```\nUsed As```\n\n```fix\nEg:-\n\n \nfox\nat\npanda\ndog\nrp\nbird\nkoala\nkangaroo\nracoon\nwhale\n```").set_footer(text="2/6")
        embed3 = discord.Embed(color=ctx.author.color,description="```yaml\nThere Are 5 Commands In Here\nFor Futher help Type 'filter'\nAlways Put Prefix Before Every Command\n```").add_field(name="Returns Filtered Image From The Requested Users Avatar", value="```\nUsed As```\n\n```fix\nEg:-\n\n \nwanted\ngay\ntrigger\nglass\nsepia\n```").set_footer(text="3/6")
        embed4 = discord.Embed(color=ctx.author.color,description="```yaml\nMust Add Prefix Before Each Comamnd```").add_field(name="Image Overlays", value="```fix\nimposter\nshoot\nrip\nslap\npewdme\nwanted\ncomment\n```").set_footer(text="4/6")
        embed5 = discord.Embed(color=ctx.author.color,description="```yaml\nMust Add Prefix Before Each Comamnd```").add_field(name="Wikipedia Search", value="```fix\nEg:-\n\nwb wikipedia\n```").set_footer(text="5/6")
        embed6 = discord.Embed(color=ctx.author.color,description="```yaml\nMust Add Prefix Before Each Comamnd```").add_field(name="Github User Search\n", value="```fix\nEg:-\n\ngit DHRUV-CODER\n```").set_footer(text="6/6")

        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx)
        paginator.add_reaction('1️⃣', "first")
        paginator.add_reaction('⏩', "next")
        paginator.add_reaction('⏪', "back")
        paginator.add_reaction('6️⃣', "last")
        paginator.add_reaction('🔐', "lock") 
        paginator.add_reaction('🗑️', "clear") 
        embeds = [embed1, embed2, embed3,embed4,embed5,embed6]
        await paginator.run(embeds)


def setup(bot):
    bot.add_cog(Stats(bot))
