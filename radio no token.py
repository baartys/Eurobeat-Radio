import discord
from discord import FFmpegPCMAudio
from discord.ext import commands
client= commands.Bot(command_prefix="er!", intents=discord.Intents.all())

@client.event
async def on_ready():
    print('Bot is running!')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="er!play / er!join"))


@client.command(aliases=['p', 'pla', 'join', 'j'])
async def play(ctx, url: str = 'http://stream.eurobeat.xyz'):
    channel = ctx.message.author.voice.channel
    global player
    try:
        player = await channel.connect()
    except:
        pass
    player.play(FFmpegPCMAudio('http://stream.eurobeat.xyz'))
    await ctx.send("**Started playing!**")


@client.command(aliases=['s', 'sto'])
async def stop(ctx):
    channel = ctx.message.author.voice.channel
    player.stop()
    channel.disconnect()
    await ctx.send("**Stopped playing!**")

@client.command(aliases=['i'])
async def info(ctx):
    await ctx.send("**Info about the Eurobeat FM**\nhttp://stream.laut.fm/eurobeat")
client.run("TOKEN")
