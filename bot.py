import os
import discord
from discord import FFmpegPCMAudio
from discord.ext.commands import Bot
from dotenv import load_dotenv

load_dotenv()
#TOKEN = os.getenv('DISCORD_TOKEN')

client = Bot(command_prefix='!',intents=discord.Intents.all())


@client.event
async def on_ready():
    print('Music Bot Ready')


@client.command(aliases=['p', 'pla'])
async def play(ctx, url: str = 'https://streams.ilovemusic.de/iloveradio109.mp3'):  #http://stream.radioparadise.com/rock-128
    channel = ctx.message.author.voice.channel
    global player
    try:
        player = await channel.connect()
    except:
        pass
    player.play(FFmpegPCMAudio(executable='ffmpeg/bin/ffmpeg.exe',source='http://stream.radioparadise.com/rock-128'))


@client.command(aliases=['s', 'sto'])
async def stop(ctx):
    player.stop()
  


client.run('OTg1MTc2OTg1OTUxMTY2NDk1.Gk5k6K._Oaaj8DmXVp8hfUc0EP-YfLIQvLAU1ybsExhN0')