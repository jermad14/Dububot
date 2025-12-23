import discord
from discord.ext import commands, tasks
import asyncio
import datetime
import time
import importlib.util
from configparser import ConfigParser
import logging
from pprint import pprint
import os
import ctypes

# local files
import dubucore
from lib import TwitchClient

# Sets window name of running application if on Windows
if os.name == 'nt':
    ctypes.windll.kernel32.SetConsoleTitleW("Dububot")

dubucore.configureLogging()
dubulog = logging.getLogger(__name__)

custom_commands = ConfigParser()
custom_commands.read('custom_commands.ini')

config = ConfigParser()
try:
    config.read('config.ini')
except FileNotFoundError:
    dubulog.error("'config.ini' not found! Some functions will be disabled.")

owner = config.get('owner', 'owner_id', fallback='0')
comm_pre = config.get('chat', 'command_prefix', fallback='!')
discord_token = config.get('discord', 'token')
twitch_token = config.get('twitch','client_id', fallback=None)


intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix = comm_pre, intents=intents)


@client.event
async def on_ready():
    dubulog.info("Bot is online and connected to Discord!")
    await client.change_presence(activity=discord.Game(name="Dubu Dubu Dubu"))

@client.listen()
async def on_message(message):
    if message.author.bot:
        return

    greeting_list = ["HELLO", "HI"]
    contents = message.content.split(" ")
    for word in contents:
        if word.upper() in greeting_list:
            await message.channel.send(f"{message.author.mention} 안녕 :heartbeat:")
            break

@client.command()
async def ping(ctx):
    await ctx.send(f"{ctx.author.mention} pong!")

@client.command()
@commands.is_owner()
async def status(ctx, *, game: str):
    await client.change_presence(activity=discord.Game(name=game))
    await ctx.send(f"Status has been updated to {game}")

@tasks.loop(seconds=45)
async def twitch_loop():
    if twitch_token is None or twitch_token == '':
        dubulog.warning('Twitch token missing. No monitoring will take place.')
        return
    
    twClient = TwitchClient.TwitchClient(twitch_token)
    announceChannel = client.get_channel(int(config.get('twitch','AnnounceChannelId')))
    usernames = config.get('twitch','MonitorChannels').split(',')

    live = await twClient.update_live_list(usernames)

    for s in live['started'].values():
        embed = twitch_start_embed(s)
        message = twitch_start_message(s)
        dubulog.info("Twitch stream started: {} ({}), {}, {}"\
            .format(s['user']['login'], s['id'], s['game']['name'], s['title']))
        await announceChannel.send(content=message, embed=embed)

    for s in live['stopped'].values():
        message = "{} has ended their stream ({})."\
            .format(s['user']['display_name'], s['id'])
        dubulog.info("Twitch stream stopped: {} ({})"\
            .format(s['user']['login'], s['id']))
        await announceChannel.send(content=message)

    for s in live['updated'].values():
        embed = twitch_start_embed(s)
        message = twitch_start_message(s)
        dubulog.info("Twitch stream updated: {} ({}), {}, {}"\
            .format(s['user']['login'], s['id'], s['game']['name'], s['title']))
        await announceChannel.send(content=message, embed=embed)

@twitch_loop.before_loop
async def before_twitch_loop():
    await client.wait_until_ready()
    dubulog.info('Starting Twitch monitor loop.')
    usernames = config.get('twitch','MonitorChannels').split(',')
    dubulog.info('Monitoring twitch channels: {}'.format(str(usernames)))

def twitch_start_message(stream):
    return "{0} is live playing {1}! https://www.twitch.tv/{2}".format(
        stream['user']['display_name'], 
        stream['game']['name'],
        stream['user']['login'])

def twitch_start_embed(stream):
    user = stream['user']
    game = stream['game']

    embed = discord.Embed(
        description = "https://www.twitch.tv/{}".format(user['login']),
        timestamp = datetime.datetime.strptime(stream['started_at'],"%Y-%m-%dT%H:%M:%SZ")
    )
    embed.set_author(
            name = "{} is live!".format(user['display_name']),
            url = "https://www.twitch.tv/{}".format(user['login']),
            icon_url = "https://cdn.discordapp.com/emojis/287637883022737418.png") \
         .set_thumbnail(url=user['profile_image_url'])                             \
         .set_footer(
            text="All Hail Dubu! | Broadcast started",
            icon_url="https://cdn.discordapp.com/attachments/440690304853737484/443852212326891530/unknown.png") \
         .add_field(name="Now Playing", value=game['name'])                        \
         .add_field(name="Total Views", value=user['view_count'])                  \
         .add_field(name="Stream Title", value=stream['title'])                    \
         .set_image(url=stream['thumbnail_url'].format(width=1024, height=576) + '?t={}'.format(time.time()))
    return embed

def handle_async_exception(loop, context):
    dubulog.warning("discord async exception: {}".format(context['message']))

client.loop.set_exception_handler(handle_async_exception)
twitch_loop.start()
client.run(discord_token)
