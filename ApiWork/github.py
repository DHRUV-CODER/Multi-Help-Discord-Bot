import discord
from discord.ext import commands
import requests as r

class GithubProfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def git(self,ctx,*,name):
        url  = f'https://api.github.com/users/{name}'
        res = r.get(url)
        data = res.json()
        try:
            embed=discord.Embed(title=f"Showing profo of {data['name']}",description=f"```fix\n{data['bio']}\n```\n`Blog`:- **[Blog]({data['blog']})**\n`Email` :- **[Email]({data['email']})**")
            embed.set_thumbnail(url=f"{data['avatar_url']}")
            embed.add_field(name="Companies", value=f" {data['company']}", inline=False)
            embed.add_field(name="Location", value=f" {data['location']}", inline=True)
            embed.add_field(name="More Info", value=f" About `{data['login']}`", inline=False)
            embed.add_field(name="`Followers`", value=f" **{data['followers']}**", inline=True)
            embed.add_field(name="`Following`", value=f" **{data['following']}**", inline=True)
            embed.add_field(name="`Hireable ??`", value=f" **{data['hireable']}**", inline=False)
            embed.add_field(name="`Public Repos`", value=f" **{data['public_repos']}**", inline=True)
            embed.add_field(name="`Public Gists`", value=f" **{data['public_gists']}**", inline=True)
            embed.add_field(name="Know More", value=f"**[{data['name']}]({data['html_url']})**", inline=False)
            embed.set_footer(text=f"Created At *{data['created_at']}*")
            await ctx.send(embed=embed)     
        except:
            await ctx.reply(f"Does **{name}** Even Exists {ctx.author.mention} 🤔")




def setup(bot):
    bot.add_cog(GithubProfo(bot))
