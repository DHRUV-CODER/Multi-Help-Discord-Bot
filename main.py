import os
import discord
import keep_alive
import DiscordUtils
import os
import json
import asyncio
from discord.ext import commands
import urllib
import traceback
import sys
import random
import time
from discord.ext.commands import when_mentioned_or
from prsaw import RandomStuff
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType
import asyncio 
rs = RandomStuff(async_mode=True)
intents = discord.Intents(messages=True,
                          guilds=True,
                          reactions=True,
                          members=True,
                          presences=True)
token = os.environ.get('DISCORD_BOT_SECREAT')
client = discord.Client(intents=discord.Intents.all())


def get_prefix(client, message):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    try:
        x = prefixes.get(str(message.guild.id), "?")
        client.prefix = x
        return when_mentioned_or(x)(client, message)
    except:
        pass


client = commands.Bot(command_prefix=get_prefix, intents=intents)
from discord_slash import SlashCommand  # Importing the newly installed library.
from discord_slash.utils import manage_commands
slash = SlashCommand(
    client, sync_commands=True)  # Declares slash commands through the client.
guild_ids = [790595270438027295,
             825342420928954399]  # Put your server ID in this array.


# Gets The Prefix
@client.event
async def on_guild_join(guild):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    prefixes[str(guild.id)] = "?"
    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)


# Set your own preifx
@client.command(aliases=['setprefix', 'newprefix'])
@commands.has_permissions(administrator=True)
async def set_prefix(ctx, prefix):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    prefixes[str(ctx.guild.id)] = prefix
    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)
    # await ctx.send(f"Server prefix changed to: `{prefix}`")
    embed = discord.Embed(title=f"Prefix Changed {prefix}",
                          description="  ",
                          color=0x28fdfd)
    embed.add_field(name="Changed By:",
                    value=ctx.message.author.mention,
                    inline=True)
    embed.add_field(name="New Prefix:", value=f"**{prefix}**", inline=False)
    await ctx.send(embed=embed)
    client.prefix = prefix


@client.command()
async def prefix(ctx):
    try:
        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)
        prefix = prefixes[str(ctx.guild.id)]
        await ctx.send(f"My Prefix In __{str(ctx.guild.name)}__ Is **{prefix}**")
    except:
        await ctx.send(f"My Prefix In __{str(ctx.guild.name)}__ Is **?**")




@client.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            embed = discord.Embed(title='*Here To your Help*')
            embed.set_footer(text='⭐Credits Go To: Dhruv⭐')
            # embed.set_author(name='?Help')
            embed.add_field(name='`moderation`',
                            value='All The Moderation Command',
                            inline=True)
            embed.add_field(name='`server`',
                            value='Commands Regarding Server',
                            inline=True)
            embed.add_field(name='`dm`',
                            value="Dm commands via bot",
                            inline=True)
            embed.add_field(name='`fun`', value='Get some Fun', inline=True)
            embed.add_field(name='`image`',
                            value='Get some cute images and more',
                            inline=False)
            embed.add_field(
                name='`notfound`',
                value=
                'commands wich are not distributed to there respective help cmd',
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
            await channel.send(embed=embed)
        break


@client.event
async def on_ready():
    # for guild in client.guilds:
    #     guild_id = str(guild.id)
    #     guild_name = str(guild.name)
    #     nos = len(guild.members)
    #     owner = str(guild.owner)
    #     print(f"Id = {guild_id} , Name = {guild_name}, Nos = {nos} , Owner {owner}")
    DiscordComponents(client)
    print("On Ready Function Working")
    await client.change_presence(activity=discord.Activity(
        status=discord.Status.idle,
        type=discord.ActivityType.watching,
        name=f"{len(set(client.users))} Members & {len(client.guilds)} Servers"
    ))
    print('Guild Function Working')



@slash.slash(name="ping", description="🎾 Pong")
async def _ping(ctx):  # Defines a new "context" (ctx) command called "ping."
    await ctx.send(f"Pong! **{round(client.latency * 1000)} ms**")


@slash.slash(name="UpVote", description="💹 Stonks")
async def _upvote(ctx):  # Defines a new "context" (ctx) command called "ping."
    await ctx.send(
        "Thnx in Advance\n\n**https://discordbotlist.com/bots/hellothere/upvote**\n\n**https://top.gg/bot/790592850588336151/vote**"
    )




initial_extensions = [
    'PilImages.imposter', 'PilImages.pewds', "PilImages.shoot",
    "PilImages.wanted", "CommandS.GameCmds.fortnite",
    "CommandS.GameCmds.pokemon", "ApiWork.animals", "ApiWork.CoolCmds",
    "ApiWork.covid", "ApiWork.joke", "ApiWork.meme", "ApiWork.animequote",
    "CommandS.GameCmds.8ball", "CommandS.BotCmd.common_cmd",
    "CommandS.BotCmd.moderation", "CommandS.BotCmd.servercmd",
    "CommandS.BotCmd.dump", "CommandS.BotCmd.Helpcommands",
    "CommandS.BotCmd._my_Bot_error_handler", "RedditMeme.rmeme",
    'PilImages.rip', 'PilImages.imran', 'PilImages.comment', 'PilImages.slap',
    "ApiWork.encoder", "CommandS.BotCmd.emojify",
    "CommandS.BotCmd.support_Service", "ApiWork.imageswitheffects",
    "ApiWork.github", "CommandS.BotCmd.pagtime", "CommandS.BotCmd.try_eval"
]

if __name__ == "__main__":
    for extensions in initial_extensions:
        try:
            client.load_extension(extensions)
        except Exception as e:
            print(f"Failed To Load Extension {extensions}", file=sys.stderr)
            traceback.print_exc()

@client.command()
async def die(ctx):
    await ctx.guild.leave()

keep_alive.keep_alive()

client.run(token)
from replit import db


