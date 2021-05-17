import discord
import re
from discord.ext import commands


class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(helpinfo='For when plain text just is not enough')
    async def emojify(self, ctx, *, text: str):
        '''
        Converts the alphabet and spaces into emoji
        '''
        emojified = ''
        formatted = re.sub(r'[^A-Za-z ]+', "", text).lower()
        if text == '':
            await ctx.send('Remember to say what you want to convert!')
        else:
            for i in formatted:
                if i == ' ':
                    emojified += '     '
                else:
                    emojified += ':regional_indicator_{}: '.format(i)
            if len(emojified) + 2 >= 2000:
                await ctx.send(
                    'Your message in emojis exceeds 2000 characters!')
            if len(emojified) <= 25:
                await ctx.send('we dont support no`s ig')
            else:
                await ctx.send(emojified) 

def setup(bot):
    bot.add_cog(Stats(bot))

