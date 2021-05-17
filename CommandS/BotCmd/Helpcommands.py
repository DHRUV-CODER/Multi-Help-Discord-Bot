import discord 
from discord.ext import commands


class HelpCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # @help.command()
    @commands.command(aliases=['mod', 'Moderation'])
    async def moderation(self, ctx):
        embed = discord.Embed(title='Made Moderation Easier!!',
                              description='',
                              colour=discord.Colour.gold())
        embed.set_footer(text='⭐Credits Go To: Dhruv⭐')
        embed.set_author(name='?moderation')
        embed.add_field(name='`ban <memeber>`',
                        value='Bans the User\n',
                        inline=True)
        embed.add_field(name='`unban <user#1234>`',
                        value='Unbans The Memeber',
                        inline=True)
        embed.add_field(name='`kick <memeber>`',
                        value='kicks The Memeber',
                        inline=False)
        embed.add_field(name='`warn <member>` ',
                        value='warns The Person',
                        inline=False)
        embed.add_field(name='`userinfo <member>` ',
                        value='Shows Detail About The User',
                        inline=False)
        embed.add_field(name='`serverinfo` ',
                        value='Shows Detail About Your Server',
                        inline=False)                              
        embed.add_field(name='`gr <member> <role>` ',
                        value='gives the role to user',
                        inline=False)
        embed.add_field(name='`av <member>` ',
                        value='Brings the Users Avatar',
                        inline=False)

        embed.set_thumbnail(
            url=
            'https://media.discordapp.net/attachments/796817762885304340/814807577438322698/mod.png?width=500&height=593'
        )

        await ctx.send(embed=embed)

    # @commands.command(aliases=['Help_special'])
    # async def dm(self, ctx):
    #     embed = discord.Embed(
    #         title='*Dm Command*',
    #         colour=discord.Colour.lighter_gray())
    #     embed.set_footer(text='⭐Credits Go To: Dhruv⭐')
    #     embed.add_field(name='`sendDM  <user.mention> <message>`',
    #                     value="Send's DM via bot Mentioning your name.",
    #                     inline=False)
    #     embed.add_field(name='`send_anonymous_dm  <user.mention>  <message>`',
    #                     value="Send's DM via bot NOT Mentioning your name.",
    #                     inline=False)
    #     embed.set_thumbnail(
    #         url=
    #         'https://www.vippng.com/png/detail/506-5067726_png-niceping-discord-ping-angry-emote.png'
    #     )

    #     await ctx.send(embed=embed)

    @commands.command(aliases=['Fun'])
    async def fun(self, ctx):
        embed = discord.Embed(
            title="*Let's Have Some Fun*",
            colour=discord.Colour.lighter_gray())
        embed.set_footer(text='⭐Credits Go To: Dhruv⭐')
        embed.add_field(name='`8ball <question>`',
                        value="Classic 8ball Game with Predection",
                        inline=False)
        embed.add_field(name='`meme`',
                        value="memes what else",
                        inline=False)
        embed.add_field(name='`rmeme <subreddit>`',
                        value="stuff some redditpost",
                        inline=False)
        embed.set_thumbnail(
            url=
            'https://c8.alamy.com/comp/BH2G63/young-boy-happy-smiling-angry-shouting-screaming-sad-scared-terrified-BH2G63.jpg'
        )

        await ctx.send(embed=embed)

    @commands.command(aliases=['Help'])
    async def help(self, ctx):
        embed = discord.Embed(
            title='*Here To your Help*',color=ctx.author.color)
        embed.set_footer(text='⭐Credits Go To: Dhruv⭐')
        # embed.set_author(name='?Help')
        embed.add_field(name='`moderation`',
                        value='All The Moderation Command',
                        inline=True)
        embed.add_field(name='`server`',
                        value='Commands Regarding Server',
                        inline=True)
        # embed.add_field(name='`dm`',
        #                 value="Dm commands via bot",
        #                 inline=True)
        embed.add_field(name='`fun`', value='Get some Fun', inline=True)
        embed.add_field(name='`animal`',
                        value='Get some cute images and more',
                        inline=False)
        embed.add_field(name='`notfound`',
                        value='commands wich are not distributed to there respective help cmd',
                        inline=False)
        embed.add_field(name='`filter`',
                        value='Get some cool filter on your avatar',
                        inline=False)
        embed.add_field(name='`img`',
                        value='Cool Overlay To Your avatar',
                        inline=False)
        embed.add_field(name='`set_prefix`',
                        value='Customizes The Prefix For The Server',
                        inline=True)
        embed.set_thumbnail(
            url=
            'https://i.insider.com/5cdd82ae021b4c02ec5edfa7?width=1136&format=jpeg'
        )
        embed.add_field(name='`infobot`',
                        value='```info and stuff```',
                        inline=False)
        embed.set_footer(text='Type ?support For Support, ezz')

        await ctx.send(embed=embed)

    @commands.command(aliases=['social media'])
    async def sm(self, ctx):
        embed = discord.Embed(
            title='Social media',
            description=
            '**[Dhruv Nation ~~ YTB ](https://www.youtube.com/channel/UCb9kY0I01P23eOxbs3kNH0g)\n[Audio Nation ~~ YTB](https://www.youtube.com/channel/UC9KPOrSqEI1O4pPD0waDsaQ)\n[GitHub](https://github.com/DHRUV-CODER)**',
            colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @commands.command(aliases=['vbucks'])
    async def vb(self, ctx):
        embed = discord.Embed(
            title="free vbucks",
            url="https://www.youtube.com/watch?v=BLeOcCeqsfI",
            description="my man xaiver is giving some vbucks ",
            color=0xff0000)
        embed.set_author(
            name="Mr Xavier",
            icon_url=
            "https://images-ext-2.discordapp.net/external/RQ1hLYGEF-gxzvmw2H_UjWqrsRiXfw9yPbyJjkpF-fM/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/701146789348376607/eb2b6e18558ff135e8ef5867e8adf7e8.webp"
        )
        embed.set_thumbnail(
            url=
            "https://cnet4.cbsistatic.com/img/aTLKqWz80LEDLhuX74RcgdKiXMM=/1200x675/2020/02/14/676146ec-f899-4c73-a132-99f7bff87827/vbucks.png"
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=[])
    async def infobot(self, ctx):

        embed = discord.Embed(
            title='HelloThere || Creator - Dhruv ',
            description=
            "```fix\nLicenced Under - MIT LICENCE```\n[LICENCE](https://github.com/DHRUV-CODER/Bot/blob/main/LICENSE)\n\n**Bot Created By** **[Dhruv](https://discord.gg/j2NeBaCWYy)** \n **You can always Send us Bug Report on Our** **[Github](https://github.com/DHRUV-CODER/Hello-There-Discord-Bot)** **& Send FeedBack/ Suggestion On Our** **[Server](https://discord.gg/j2NeBaCWYy)** **or via our cmd ?support** \n\n **[Invite](https://discord.com/api/oauth2/authorize?client_id=790592850588336151&permissions=8&scope=bot%20applications.commands)**\n\n**[Bot Support Server](https://discord.gg/j2NeBaCWYy)**\n\n **[Bot's Source Code](https://github.com/DHRUV-CODER/Multi-Help-Discord-Bot)**\n\n **Btw I was Created On *21/12/2020***",
            colour=discord.Colour.gold())
        embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/Tre-DTEsCA4SPxzckreGS-Y4KzYnPSy-ZkcFyc5d6QU/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/790592850588336151/c20460f6812070b89bad577e3a77142a.webp?width=592&height=592")
        await ctx.send(embed=embed)

    @commands.command(aliases=['apihelp'])
    async def animal(self, ctx):
        embed = discord.Embed(title="Cute Animals",
                              description="```fix\nfox\ncat\npanda\ndog\nrp\nbird\nkoala\nkangaroo\nracoon\nwhale\n```",
                              color=0xccb044)
        # embed.set_thumbnail(
        #     url=
        #     "https://www.pngfind.com/pngs/m/456-4569373_view-noice-emotes-pokemon-discord-png-transparent-png.png"
        # )        
        embed.set_footer(text="\n\n ⭐Credits To Dhruv⭐\n\n")
        await ctx.send(embed=embed)

    @commands.command()
    async def server(self, ctx):
        icon = str(ctx.guild.icon_url)
        embed = discord.Embed(title="Server  Command")
        embed.add_field(name="`serverinfo`",
                        value="Information About The server",
                        inline=False)
        embed.add_field(name="`owner`",
                        value="Know Who Is The Owner",
                        inline=False)
        embed.add_field(name="`servericon`",
                        value="Get your beautiful Server Icon",
                        inline=False)
        embed.add_field(name="`servermember`",
                        value="Memebers You Have Got",
                        inline=False)
        embed.add_field(name="`serverregion`",
                        value="Region Of your Server",
                        inline=False)
        embed.set_thumbnail(url=f"{icon}")
        await ctx.send(embed=embed)

    @commands.command()
    async def support(self, ctx):
        embed = discord.Embed(
            title="Support",
            url="https://discord.gg/j2NeBaCWYy",
            description=
            "i (dev of bot) will respond fast to ur suggestion or any kind of concern",
            color=0x14f51b)
        embed.add_field(
            name="?message",
            value=
            "Will Send a Message To Developer \n You can Suggest , Complaint etc.",
            inline=True)
        await ctx.send(embed=embed)

    @commands.command()
    async def notfound(self, ctx):
        embed = discord.Embed(
            title="`These are some commands which will soon be shown in there respective help command`",
            color=ctx.author.color)
        embed.add_field(
            name="__each cmd is seperated by a comma(`,`)__",
            value="```fix\ncovid,encode,decode,ytb,fort,pm,trigger,\nstatus,ping,emojify,\nimposter,shoot,rip,slap,\npewds,wanted,comment,\nquote,wink,hug,\npat,joke,say ```",
            inline=True)
        await ctx.send(embed=embed)

    @commands.command(aliases=['imagefilter'])
    async def filter(self, ctx):
      embed=discord.Embed(title="Filters For Your Amazing Avatar")
      embed.add_field(name="`wasted`", value="remember the gta wasted overlay", inline=False)
      embed.add_field(name="`gay`", value="all rainbow 🌈", inline=False)
      embed.add_field(name="`trigger`", value="why so pissed", inline=False)
      embed.add_field(name="`glass`", value="that looks good on u", inline=False)
      embed.add_field(name="`sepia`", value="boomer look", inline=False)
      embed.set_thumbnail(
          url=
          "https://www.pngfind.com/pngs/m/456-4569373_view-noice-emotes-pokemon-discord-png-transparent-png.png"
      )  
      await ctx.send(embed=embed)
      
    @commands.command(aliases=['img'])
    async def image(self, ctx):
      embed=discord.Embed(title="Custom Made Overlays For You")
      embed.add_field(name="`imposter`", value="red sus", inline=False)
      embed.add_field(name="`shoot`", value="aim the noob", inline=False)
      embed.add_field(name="`rip`", value="we wont miss u", inline=False)
      embed.add_field(name="`slap`", value="test of his own medicine", inline=False)
      embed.add_field(name="`pewdme`", value="pewds av looks cool on u", inline=False)
      embed.add_field(name="`wanted`", value="will find u soon", inline=False)
      embed.add_field(name="`comment`", value="hmm", inline=False)

      await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(HelpCommands(bot))
