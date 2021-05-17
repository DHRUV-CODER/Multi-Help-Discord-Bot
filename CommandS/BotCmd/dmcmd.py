# # import discord
# # from discord.ext import commands


# # class DmCmd(commands.Cog):
# #     def __init__(self, bot):
# #         self.bot = bot

#     # @commands.command()
#     # @commands.has_role("anonydmallowed")
#     # async def send_anonymous_dm(self,ctx, member: discord.Member, *, content):
#     #     channel = await member.create_dm(
#     #     )  # creates a DM channel for mentioned user
#     #     await channel.send(
#     #         f'**Somebody Sent Anonymous Message Saying:** ||  {content}  ||'
#     #     )  # send whatever in the content to the mentioned user.
#     #     await ctx.message.add_reaction('📫')


# #     @send_anonymous_dm.error
# #     async def anonyerror(self,ctx, error):
# #         if isinstance(error, commands.errors.MissingRole):
# #           embed=discord.Embed(title="Steps To Allow Sending Dm's", color=0xf7fb04)
# #           embed.add_field(name="Step 1", value="Make a Role Named (**dmallowed**)", inline=True)
# #           embed.add_field(name="For sending anonymous Dm's", value="Role named (**anonydmallowed**)", inline=False)
# #           embed.add_field(name="Step 2", value="Assign it to anyone whom you want this To use ", inline=True)
# #           embed.add_field(name="Precaution ", value="(**dmallowed**) is some what safe as it gives id to user \n but  using(**anonydmallowed**) can cause problem , leaving no information to sender \n So assign at your own risk", inline=False)
# #           embed.set_footer(text="Hope you understand, Thanks")
# #           await ctx.send(embed=embed)


# #     # THIS FUNCTION WILL SEND A DM WITH THE AUTHORS NAME.
#     @commands.command()
#     @commands.has_role("dmallowed")
#     async def sendDM(self,ctx, member: discord.Member, *, content):
#         channel = await member.create_dm(
#         )  # creates a DM channel for mentioned user
#         await channel.send(
#             f"**{ctx.message.author} said:** {content}"
#         )
#         await ctx.message.add_reaction('📫')
        




# #     @sendDM.error
# #     async def dmerror(self,ctx, error):
# #         if isinstance(error, commands.errors.MissingRole):
# #           embed=discord.Embed(title="Steps To Allow Sending Dm's", color=0xf7fb04)
# #           embed.add_field(name="Step 1", value="Make a Role Named (**dmallowed**)", inline=True)
# #           embed.add_field(name="For sending anonymous Dm's", value="Role named (**anonydmallowed**)", inline=False)
# #           embed.add_field(name="Step 2", value="Assign it to anyone whom you want this To use ", inline=True)
# #           embed.add_field(name="Precaution ", value="(**dmallowed**) is some what safe as it gives id to user \n but  using(**anonydmallowed**) can cause problem , leaving no information to sender \n So assign at your own risk", inline=False)
# #           embed.set_footer(text="Hope you understand, Thanks")
# #           await ctx.send(embed=embed)

# # def setup(bot):
# #     bot.add_cog(DmCmd(bot))
