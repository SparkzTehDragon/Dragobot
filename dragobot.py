# SECTION 1.0.0: Imported Modules

import discord
from discord.ext import commands
import typing
import discord.ext
import logging
import random
import time
import asyncio
import sys

logger = open("discord.txt", "w")
logger=logging.getLogger('discord').setLevel(logging.DEBUG)
logging.basicConfig(level=logging.INFO)
logging.StreamHandler(logger)

handler=logging.FileHandler(filename='discord.txt', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(Levelname)s:%(name)s: %(message)s'))

log = logging.getLogger(__name__)
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    async def on_message_event(message):
        return all
async def on_typing():
    return()
       
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("who"):
       await message.channel.send("I am Drago#3438")

@client.event
async def request_offline_members(self, guilds):
    logger.setLevel()
    await self._connection.request_offline_members(guilds)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('ur gay' or 'your gay'):
        await message.channel.send("love you too")
    if message.content.startswith('hello'):
        await message.channel.send('Hello!\n')
        
    if message.content.startswith('idk'):
        await message.channel.send("what's wrong?\n")
        
    if message.content.startswith("you suck"):
        await message.channel.send(random.choice(["That wasn't very nice...","You should apologize now.","You shouldn't be saying that here.","You don't have to be rude.","Please refrain from insulting myself or other users within this guild.","I can literally mute you, ban you, or even cause you to be stuck within one channel and never escape ever again."]))
        
    if message.content.startswith("i am sad"):
        await message.channel.send(random.choice(["Can I hug you?","*Drago gives the one who needs it a hug and lots of smiles. Especially, cookies!*","*Curls around trying to make the one who needs the comfort feel secure.*","[ERROR] Command not found with directory.","[ERROR] Command not found within Dragobot.py"]))
        
    if message.content.startswith("cmd_list\n"):
        await message.channel.send("""```Command List for Dragobot.py```
        
        

`game` - ***DISABLED*** *Starts up a combat game between the bot and the user (Still in progress it is being converted)*

`i am sad` - *Responds to the User to help comfort them/support them through an IN-CHARACTER format*

`you suck` - *Responds to the User with random.choice responses that are positive, never negative feedback from the bot itself.*
`idk` - *Asks the User what the situation is.*

`hello` - *Responds to the User with "Hello!"*
        """)
        

        

client.run('')
