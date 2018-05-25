import sys
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from random import *
import asyncio
import time
import json
import urllib.request
from annoyingLists import *
#import chalk
bot = commands.Bot(command_prefix='&')

@bot.event
async def on_ready():
    print ("Ready when you are")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)
    await bot.change_presence(game=discord.Game(name='&help for commands'))
@bot.command(pass_context=True)
async def latestnews():
    with urllib.request.urlopen("https://xivdb.com/assets/lodestone.json"):
        jsonfile=json.loads(url.read().decode())
@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
    """Chooses between multiple choices."""
    x=randint(0,len(choices)-1)
    await bot.say(choices[x])

@bot.command(pass_context=True)
async def yt(ctx, url):
    """Plays Youtube or Twitch link's Audio"""
    author = ctx.message.author
    voice_channel = author.voice_channel
    vc = await bot.join_voice_channel(voice_channel)

    player = await vc.create_ytdl_player(url)
    length=player.duration
    player.start()
    start=time.time()
    elapsed=0
    while(elapsed<length):
        elapsed=time.time()-start
    for x in bot.voice_clients:
        if(x.server == ctx.message.server):
            return await x.disconnect()
@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: ping!!")
    print ("user has pinged")

@bot.command(pass_context = True)
async def leave(ctx):
    """Leaves Voice Channel"""
    for x in bot.voice_clients:
        if(x.server == ctx.message.server):
            return await x.disconnect()
    return await bot.say("I am not connected to any voice channel on this server!")

@bot.command(pass_context=True)
async def dice(ctx,dicetype):
    """Rolls dice from 1 to X"""
    x=randint(1,int(dicetype))
    await bot.say(x)

#@bot.command(pass_context=True)
#async def play(ctx,url):
#    """WIP"""
#    await bot.create_ytdl_player(url)

@bot.command(pass_context=True)
async def flip(ctx):
    """Flip a coin"""
    x=randint(1,100)
    if(x<50):
        await bot.say("HEADS https://mainkhan.files.wordpress.com/2015/02/head4.png")
    if(x>50):
        await bot.say("TAILS https://vignette.wikia.nocookie.net/sonic/images/a/a3/SF_STEAM_MANUAL_EN_LRv5-10.png/revision/latest/scale-to-width-down/324?cb=20171129131208")

@bot.command(pass_context=True, description='chooses random league character')
async def randomChamp(ctx):
    """"chooses random league character"""
    champlist=[]
    champlist=makeChampList()
    x=randint(0,len(champlist))
    await bot.say(champlist[x])

@bot.command(pass_context=True, description='chooses random spot on map for Fortnite')
async def whereto(ctx):
    """chooses random spot on map for Fortnite"""
    locationList=[]
    locationList=makeLocation()
    x=randint(0,len(locationList))
    await bot.say(locationList[x])

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    """Display User Info"""
    await bot.say("The users name is: {}".format(user.name))
    await bot.say("The users ID is: {}".format(user.id))
    await bot.say("The users status is: {}".format(user.status))
    await bot.say("The users highest role is: {}".format(user.top_role))
    await bot.say("The user joined at: {}".format(user.joined_at))

@bot.command(pass_context=True)
async def Hello(ctx):
    """Hello"""
    await bot.say("Fuck you")

@bot.command(pass_context=True)
async def Forest(ctx,user:discord.Member):
    """Did somebody say the forest?"""
    await bot.say(user.mention+" https://store.steampowered.com/app/242760/")

@bot.command(pass_context=True)
async def closeRobinBot(ctx):
    """Used cause im lazy to close terminal and blah blah blah"""
    await bot.logout();
    await sys.exit(0)

bot.run("NDMwNTg2OTk0NjY2NzY2MzM3.DaV6Bg.h9BNfDOrPJGIz8Cz3eMxEuGdes0")
