import discord
from discord.ext import commands
import datetime

class ServerCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def serverinfo(self, ctx):
      embed = discord.Embed(title="Server information",
              colour=ctx.guild.owner.colour,
              timestamp=datetime.datetime.utcnow())

      embed.set_thumbnail(url=ctx.guild.icon_url)

      statuses = [len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
            len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
            len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
            len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))]

      fields = [("ID", ctx.guild.id, True),
            ("Owner", ctx.guild.owner.mention, True),
            ("Region", ctx.guild.region, True),
            ("Created at", ctx.guild.created_at.strftime("%d/%m/%Y %H:%M:%S"), True),
            ("Members", len(ctx.guild.members), True),
            ("Humans", len(list(filter(lambda m: not m.bot, ctx.guild.members))), True),
            ("Bots", len(list(filter(lambda m: m.bot, ctx.guild.members))), True),
            ("Banned members", len(await ctx.guild.bans()), True),
            ("Statuses", f"🟢 {statuses[0]} 🟠 {statuses[1]} 🔴 {statuses[2]} ⚪ {statuses[3]}", True),
            ("Text channels", len(ctx.guild.text_channels), True),
            ("Voice channels", len(ctx.guild.voice_channels), True),
            ("Categories", len(ctx.guild.categories), True),
            ("Roles", len(ctx.guild.roles), True),
            ("Invites", len(await ctx.guild.invites()), True),
            ("\u200b", "\u200b", True)]

      for name, value, inline in fields:
        embed.add_field(name=name, value=value, inline=inline)

      await ctx.send(embed=embed)

    @commands.command(aliases=['owner'])
    async def serverOwner(self,ctx):
        await ctx.send(f'Here At {ctx.guild.name} , The Server Owner Is **{ctx.guild.owner}** \n\n\n **To Know More About Server , Use ** \n ```fix\n ?server```')



    @commands.command(aliases=['icon'])
    async def serverIcon(self,ctx):
        await ctx.send(ctx.guild.icon_url)


    @commands.command(aliases=['totalmember'])
    async def serverMember(self,ctx):
        # memberCount = str(ctx.guild.member_count)
        member_count = len(ctx.guild.members)
        true_member_count=len([m for m in ctx.guild.members if not m.bot])
        bots = member_count - true_member_count
        await ctx.send(f'Here At **{ctx.guild.name}** , We Got Here  **{true_member_count}** Members To appreciate & **{bots}** bots \n\n\n **To Know More About Server , Use ** \n ```fix\n ?server```')


    @commands.command(aliases=['serverarea', 'serverregion', 'region'])
    async def serverRegion(self,ctx):
      embed=discord.Embed(title=f"Region {ctx.guild.region}")
      embed.timestamp = datetime.datetime.utcnow()
      await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(ServerCmd(bot))
