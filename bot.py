
import discord
from discord import FFmpegPCMAudio
from discord.ext.commands import Bot
from dotenv import load_dotenv

load_dotenv()
#TOKEN = os.getenv('DISCORD_TOKEN')
#PREFIX = os.getenv('DISCORD_PREFIX')
intents=discord.Intents.all()
client = Bot(command_prefix='>>',intents=intents)


@client.event
async def on_ready():
    print('Music Bot Ready')


@client.command(aliases=['p', 'pla'])
async def play(ctx, url: str = 'http://stream.radioparadise.com/rock-128'):
    channel = ctx.message.author.voice.channel
    global player
    try:
        player = await channel.connect()
    except:
        pass
    player.play(FFmpegPCMAudio('http://stream.radioparadise.com/rock-128',executable='ffmpeg/bin/ffmpeg.exe'))


@client.command(aliases=['s', 'sto'])
async def stop(ctx):
    player.stop()


client.run('OTg1MTc2OTg1OTUxMTY2NDk1.Gg1ao9.Y2LSW8zOcRCwUNFurway8okgj3vPA-cM6DFvvo')