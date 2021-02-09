import discord, typing, os, asyncio
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure, ArgumentParsingError, MissingRequiredArgument, BadArgument
from datetime import datetime
from time import strftime
import random

client  = commands.Bot(command_prefix = "d!") 

client.remove_command('help')

@client.event
async def on_ready():
    print('Welcome to the dreams!')
    await client.change_presence(status = discord.Status.online, activity = discord.Game("Welcome to the Dreams"))


client.run(' ODA4NzA0NTAxMjQ5ODY3ODA2.YCKawg.n8Ti2Vk8hQCdPFxCbvWc_SVHCQo')
