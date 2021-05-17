import discord
from discord.ext import commands
import datetime
from PIL import Image, ImageFont, ImageDraw
import asyncio
import random
from PIL import Image
from io import BytesIO


class ded(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dedcmddddddd(self,ctx,*,comment="My g where is your comment??"):
        
        commenter = ctx.author
        
        commented_img = Image.open("./images/comment.png")

        asset = commenter.avatar_url_as(size = 128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)

        pfp = pfp.resize((74,65))
        commented_img.paste(pfp, (59,29))
        
        commenter_im = commented_img.convert("RGB")
        commenter_im.save("./finalimages/1comment.png")
        
        image = Image.open('./finalimages/1comment.png')
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("./fonts/arial.ttf",40)
        points = 161,25
        text = f"{comment}"
        warn = ";/ less than 43 char only"
        
        if len(text) > 43:
            # await ctx.send(";/ less than 43 char only")
            draw.text(points, warn,"white",font=font)
            image.save('./finalimages/commented.png')
            
            await ctx.send(file= discord.File("./finalimages/commented.png"))

        else:
            draw.text(points, text,"white",font=font)
            image.save('./finalimages/commented.png')
            
            await ctx.send(file= discord.File("./finalimages/commented.png"))

    # async def comment(self,ctx,*,comment="My g where is your comment??"):
    #     image = Image.open('./images/comment.png')
    #     draw = ImageDraw.Draw(image)
    #     font = ImageFont.truetype("./fonts/arial.ttf",40)
    #     points = 161,25
    #     text = f"{comment}"
    #     warn = ";/ less than 43 char only"

    #     if len(text) > 43:
    #         # await ctx.send(";/ less than 43 char only")
    #         draw.text(points, warn,"white",font=font)
    #         image.save('./finalimages/commented.png')

    #         await ctx.send(file= discord.File("./finalimages/commented.png"))

    #     else:
    #         draw.text(points, text,"white",font=font)
    #         image.save('./finalimages/commented.png')

    #         await ctx.send(file= discord.File("./finalimages/commented.png"))


def setup(bot):
    bot.add_cog(ded(bot))
