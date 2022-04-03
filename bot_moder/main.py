from asyncio import events
from pydoc import cli
from click import pass_context
from webserver import keep_alive
from discord.ext import commands

import time
import discord
import os
import config


if __name__ == '__main__':
    client  = discord.Client()

client = commands.Bot(command_prefix='/')
@client.command(pass_context = True)
async def z(ctx, amount = 100):
    await ctx.channel.purge(limit = amount)


@client.event
async def on_message(message):
    await client.process_commands( message )

    if(message.author.id == 282859044593598464 and message.channel.id==874647785461411903 ):
        await message.channel.purge(limit = 1 )
        await message.channel.send('Пошли нахуй отсюда')

    msg = set(message.content.lower().split())
    
    if oleg_good_day(msg):
        await message.channel.send('А я ясные дни оставляю себе!')

def oleg_good_day(text):
    good = {'ясный','ясные','ясными','ясным'}
    days = {'дни','день','днями','дням'}
    oleg = {'олег','олежа'}
    doing = {'делаешь','делать','поступать','там'}
    what = {'че','что','как'}

    int_good = len(set.intersection(text,good)) >  0
    int_days = len(set.intersection(text,days)) > 0
    int_oleg = len(set.intersection(text,oleg)) > 0
    int_doing = len(set.intersection(text,doing)) > 0
    int_what = len(set.intersection(text,what)) > 0

    sum_of = int_good + int_days + int_oleg + int_doing + int_what

    if  sum_of >= 3 and int_oleg :
        return True
    else:
        return False

#keep_alive()
client.run(config.BOT_TOKEN)


