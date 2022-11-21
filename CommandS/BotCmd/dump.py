import discord
from discord.ext import commands
import datetime
import urllib.request
import pyshorteners
import re
import time
import json
import random 
import aiohttp
from aiohttp import ClientSession
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType
import asyncio
class Dump(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['convey', 'speak'])
    async def say(self, ctx, *, msg):
        embed = discord.Embed(title="")
        embed = discord.Embed(description=f"**{msg}**")
        await ctx.send(embed=embed)

    @commands.command()
    async def emo(self, ctx):
        await ctx.send(" <:gold:803174264445861888> ")

    @commands.command()
    async def hi(self, ctx):
        await ctx.message.add_reaction('🙋‍♂️')
        await ctx.message.add_reaction('🇭')
        await ctx.message.add_reaction('🇮')

    # @commands.command()
    # async def u_suck(self, ctx):
    #     await ctx.message.add_reaction('💢')
    #     await ctx.message.add_reaction('🇲')
    #     await ctx.message.add_reaction('🇩')
    #     await ctx.message.add_reaction('🇫')
    #     await ctx.message.add_reaction('🇰')
    #     await ctx.message.add_reaction('🇰')
    #     await ctx.message.add_reaction('🤏')

    @commands.command()
    async def XavierAnna(self, ctx):
        await ctx.message.add_reaction('<:xavier:799176988387573760>')

    @commands.command()
    async def shutdown(self, ctx):
        if ctx.message.author.id == 701146789348376607:
            print("shutdown")
            try:
                await ctx.send(f"Salute {ctx.author.mention} you created me you destroyed me 😭")
                await self.bot.logout()
            except:
                print("EnvironmentError")
                self.bot.clear()
        else:
            await ctx.send("nice try ,You do not own this bot anyways join our developer team currently solo https://discord.gg/j2NeBaCWYy", delete_after=25.0)


    @commands.command(aliases=['slots', 'bet'])
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def slot(self, ctx):
        """ Roll the slot machine """
        emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
        a = random.choice(emojis)
        b = random.choice(emojis)
        c = random.choice(emojis)

        slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"

        if (a == b == c):
            await ctx.reply(f"{slotmachine}thats rare, All matching, you won! 🎉")
        elif (a == b) or (a == c) or (b == c):
            await ctx.reply(f"{slotmachine} 2 in a row, close though but idc u didnt win")
        else:
            await ctx.reply(f"{slotmachine} No match, you lost 😢")





    @commands.command()
    async def ytb(self,ctx,search_keyword):
      html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
      video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    #   print(video_ids)
      await ctx.send("https://www.youtube.com/watch?v=" + video_ids[0])

    @commands.command()
    async def hack(self, ctx,*,member: discord.Member = None):
      async with ctx.typing():
        if not member:  # if member is no mentioned
          member = ctx.message.author
        message = await ctx.send("Bruh...")
        await message.edit(content=f"found {member.mention} credit card details")
        time.sleep(2)
        await message.edit(content=f"my g {member.mention} cm on so ezz password")
        time.sleep(2)
        await message.edit(content="wait what")
        time.sleep(2)
        await message.edit(content=f"{member.mention} dont mine i took ur **onlyfan** sub")
        time.sleep(2)
        await message.edit(content=f"{member.mention} bruh u have bad taste")
        time.sleep(2)
        await message.edit(content=f"00010101010fsfes3030")
        await message.edit(content=f"0001dwadwdaw303efsef0")
        await message.edit(content=f"0004242030ttred30")
        await message.edit(content=f"0001010fsefesfes053")
        await message.edit(content=f"00010422dwfghytrdgtrd3030")
        await message.edit(content=f"0001010dw7543555wa03030")
        await message.edit(content=f"0001010dwa335rw35ggggdww3330")
        await message.edit(content=f"00010101wdwad30rrrehhn30")
        await message.edit(content=f"fbi open up")
        time.sleep(3)
        await message.edit(content=f"https://media.tenor.com/images/a1912e38f72c5df9050d931853fafddb/tenor.gif")
        time.sleep(5)
        time.sleep(2)
        await message.edit(content=f"cmon {member.mention} u dont need to call cops for that prank")
        time.sleep(2)
        await message.edit(content=f"😐☠⚰.....🤙")
        await message.edit(content=f"Peace")

    # @commands.command()
    # async def lyrics(self, ctx,*,song):
    #     async with ctx.channel.typing():
    #         async with aiohttp.ClientSession() as cs:
    #             async with cs.get(
    #                     f"https://some-random-api.ml/lyrics?title={song}"
    #             ) as r:
    #               try:
    #                 data = await r.json()
    #                 embed=discord.Embed(title=data["title"], description="```yaml\n{}```".format(data["lyrics"]))
    #                 embed.set_thumbnail(url=data["thumbnail"]['genius'])
    #                 await ctx.send(embed=embed)
    #               except:
    #                 await ctx.send("either it doesnt exists or its too long;/")


    @commands.command(aliases=['lrcs'])
    async def lyrics(self, ctx, *, arg):

        await ctx.trigger_typing()
        arg.replace(' ', '+')
        
        lrcsession = aiohttp.ClientSession()
        lrcgetlnk = await lrcsession.get('https://some-random-api.ml/lyrics?title={}'.format(arg))
        lrcdata = json.loads(await lrcgetlnk.text())

        lyrrc = (str(lrcdata['lyrics']))

        try:
            for chunk in [lyrrc[i:i+2000] for i in range(0, len(lyrrc), 2000)]:
                embed = discord.Embed(title=f"**{(str(lrcdata['title']))} by {(str(lrcdata['author']))}**", description=f"```yaml\n{chunk}```")
                await ctx.send(embed=embed)

        except discord.HTTPException:
            embe = discord.Embed(title=f"**{(str(lrcdata['title']))} by {(str(lrcdata['author']))}**", description=f"```yaml\n{chunk}```")
            embe.set_footer(text="{0}\nID: {1}\n{2}".format(ctx.message.author.name, ctx.message.author.id, datetime.datetime.utcnow().strftime("%A, %B %d %Y at %I:%M:%S %p UTC")), icon_url=ctx.message.author.avatar_url)
            embe.set_thumbnail(url=lrcdata["thumbnail"]['genius'])
            embe.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embe)

        await lrcsession.close()

    @commands.command()
    async def urlshorten(self,ctx,link):
      shortener=pyshorteners.Shortener()
      shortned_link = shortener.tinyurl.short(link)
      await ctx.send(f"Take Your Shortened URL \n Preview Disabled \n <{shortned_link}>")

    @commands.command()
    async def wiki(self, ctx,*,query):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get(
                        f"https://wiki-api.dhruvnation1.repl.co/wiki/query={query}"
                ) as r:
                    data = await r.json()
                    embed=discord.Embed(title="Wiki Results", description=data["Result"])
                    embed.timestamp = datetime.datetime.utcnow()
                    await ctx.send(embed=embed)


    @commands.command()
    async def admm(self,ctx,name,class_they_study_in,place):
        with open("name.json", "r") as f:
            names = json.load(f)
        # names = {f'{ctx.author.name}':[{'name': f'{name}', 'class': f'{class_they_study_in}', 'from': f'{place}'}]}
        names[str(ctx.author.id)] = [{'name': f'{name}', 'class': f'{class_they_study_in}', 'from': f'{place}'}]
        with open("name.json", "w+") as f:
            json.dump(names, f, indent=4)
            await ctx.send("Done!!")

    @commands.command()
    async def fmm(self,ctx):
        with open("name.json", "r") as f:
            names = json.load(f)
        name = names[f'{ctx.author.id}'][0]['name']
        classs = names[f'{ctx.author.id}'][0]['class']
        places = names[f'{ctx.author.id}'][0]['from']
        await ctx.send(f'Name = {name}\nClass = {classs}\nplace = {places}')

    @commands.command()
    async def upvote(self,ctx):

        await ctx.send(
            "**Thnx For Voting in Advance**",
            components=[[
                Button(style=ButtonStyle.URL, label="UpVote on DBL",url="https://discordbotlist.com/bots/hellothere/upvote"),
                Button(style=ButtonStyle.URL, label="UpVote on Top.gg",url="https://top.gg/bot/790592850588336151/vote"),
            ]])
            

    @commands.command()
    async def simp(self,ctx):

        m = await ctx.send(
            "```glsl\nYou:- Hi\nMe:-\n```",
            components=[[
                Button(style=ButtonStyle.red, label="Do You love Me ??",emoji="💗",disabled=True),
                Button(style=ButtonStyle.green, label="Yes I Do",),
            ]])
        def check(res):
            return ctx.author == res.user and res.channel == ctx.channel

        try:
            await self.bot.wait_for("button_click", check=check,timeout=5)
            await m.edit(
                        "Bahahahahhahah",
            components=[[
                Button(style=ButtonStyle.blue, label="F Off",emoji="🤣", disabled=True),
                Button(style=ButtonStyle.red, label="You simp",emoji="💢", disabled=True),
            ]]
            )
        except asyncio.TimeoutError:
            await m.edit(
            "You Better Reply Faster",
            components=[
                Button(style=ButtonStyle.red, label="I Have Got Standards", disabled=True,emoji="😏"),
            ]
        )

    @commands.command()
    async def f(self,ctx):
        await ctx.send("Done!!",delete_after=3.0)

def setup(bot):
    bot.add_cog(Dump(bot))
