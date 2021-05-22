import discord
from discord.ext import commands
import requests
import bs4


class Covid(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def covid(self, ctx, *,country="WorldWide"):
        
        url = f'https://www.worldometers.info/coronavirus/country/{country.replace(" ","-")}'
        
        if country == "WorldWide":
            url = "https://www.worldometers.info/coronavirus/"
        else:
            pass

        result = requests.get(url)

        soup = bs4.BeautifulSoup(result.text,'lxml')
        cases = soup.find_all('div', class_='maincounter-number')
        links = soup.find('div', {'style': 'display:inline'})
        latest_updated = soup.find('div', class_='news_date')
        try:
            last_updated = latest_updated.text
        except:
            last_updated = "Not Provided"

        data = []
        for i in cases:
            span = i.find('span')
            data.append(span.string)

        
        try:
            images = links.find('img')
            flag = f"https://www.worldometers.info/{images.attrs['src']}"
        except:
            flag = "https://static.wixstatic.com/media/2cd43b_af35a03a70e144ddba269287704a6465~mv2.png/v1/fill/w_256,h_256,q_90/2cd43b_af35a03a70e144ddba269287704a6465~mv2.png"

        try:
            embed = discord.Embed(title=f"{country.capitalize()} - Stats",
                                  url=url,
                                  description=f"Last Updated/News At **{last_updated}**",
                                  color=0x31d2dd)
            embed.set_thumbnail(url=flag)
            embed.add_field(name="Total Cases", value=data[0], inline=True)
            embed.add_field(name="Deaths", value=data[1], inline=True)
            embed.add_field(name="Recoverved", value=data[2], inline=True)
            await ctx.send(embed=embed)
        except:
            await ctx.send("Look For Spell Errors or Invalid Country :(")


def setup(bot):
    bot.add_cog(Covid(bot))
