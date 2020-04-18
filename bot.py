import discord
from discord.ext import commands, tasks
import asyncio
import random
import os
import datetime
import json	

client = discord.Client()

client = commands.Bot( command_prefix = '//' )

client.remove_command('help')

#Variables

gift_1 = True
gift_2 = True
gift_3 = True
gift_4 = True
gift_5 = True
gift_6 = True
gift_7 = True
gift_8 = True
gift_9 = True
gift_10 = True
gift_11 = True
gift_12 = True
gift_13 = True
gift_14 = True
gift_15 = True
gift_16 = True
gift_17 = True
gift_18 = True
gift_19 = True
gift_20 = True
gift_21 = True
gift_22 = True
gift_23 = True
gift_24 = True
gift_25 = True
gift_26 = True
gift_27 = True
gift_28 = True
gift_29 = True
gift_30 = True
gift_31 = True
gift_32 = True

#Messages

#Filter

#@client.event
#async def on_message (message):
    #channel = client.get_channel( 625001455182544937 )

    #await client.process_commands(message)

    #msg = message.content.lower()
    #if msg in bad_words:
        #await message.delete()
        #await message.author.send(f'{message.author.name}, нельзя такое писать в этом чате!')

#Commands

#Gifts

@client.command()

async def gift_1897 (ctx, member:discord.Member):
    global gift_1

    if gift_1:
        await ctx.channel.purge(limit=1)
        pup_role = discord.utils.get(ctx.message.guild.roles, name='❄️')
        emb = discord.Embed(title = 'ПОЗДРАВЛЯЕМ!', colour = discord.Color.gold(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Вы получили подарок!')
        await ctx.send(embed = emb)
        await member.add_roles(pup_role)
        gift_1 = False
    else:
        await ctx.channel.purge(limit=1)
        emb = discord.Embed(title = 'ОШИБКА!', colour = discord.Color.red(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Код уже использован!')
        await ctx.send(embed = emb)

@client.command()
async def gift_2315 (ctx, member:discord.Member):
    global gift_2

    if gift_2:
        await ctx.channel.purge(limit=1)
        pup_role = discord.utils.get(ctx.message.guild.roles, name='❄️')
        emb = discord.Embed(title = 'ПОЗДРАВЛЯЕМ!', colour = discord.Color.gold(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Вы получили подарок!')
        await ctx.send(embed = emb)
        await member.add_roles(pup_role)
        gift_2 = False
    else:
        await ctx.channel.purge(limit=1)
        emb = discord.Embed(title = 'ОШИБКА!', colour = discord.Color.red(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Код уже использован!')
        await ctx.send(embed = emb)

@client.command()
async def gift_3412 (ctx, member:discord.Member):
    global gift_3

    if gift_3:
        await ctx.channel.purge(limit=1)
        pup_role = discord.utils.get(ctx.message.guild.roles, name='❄️')
        emb = discord.Embed(title = 'ПОЗДРАВЛЯЕМ!', colour = discord.Color.gold(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Вы получили подарок!')
        await ctx.send(embed = emb)
        await member.add_roles(pup_role)
        gift_3 = False
    else:
        await ctx.channel.purge(limit=1)
        emb = discord.Embed(title = 'ОШИБКА!', colour = discord.Color.red(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Код уже использован!')
        await ctx.send(embed = emb)

@client.command()
async def gift_6753 (ctx, member:discord.Member):
    global gift_4

    if gift_4:
        await ctx.channel.purge(limit=1)
        pup_role = discord.utils.get(ctx.message.guild.roles, name='❄️')
        emb = discord.Embed(title = 'ПОЗДРАВЛЯЕМ!', colour = discord.Color.gold(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Вы получили подарок!')
        await ctx.send(embed = emb)
        await member.add_roles(pup_role)
        gift_4 = False
    else:
        await ctx.channel.purge(limit=1)
        emb = discord.Embed(title = 'ОШИБКА!', colour = discord.Color.red(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Код уже использован!')
        await ctx.send(embed = emb)

@client.command()
async def gift_2345 (ctx, member:discord.Member):
    global gift_5

    if gift_5:
        await ctx.channel.purge(limit=1)
        pup_role = discord.utils.get(ctx.message.guild.roles, name='❄️')
        emb = discord.Embed(title = 'ПОЗДРАВЛЯЕМ!', colour = discord.Color.gold(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Вы получили подарок!')
        await ctx.send(embed = emb)
        await member.add_roles(pup_role)
        gift_5 = False
    else:
        await ctx.channel.purge(limit=1)
        emb = discord.Embed(title = 'ОШИБКА!', colour = discord.Color.red(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Код уже использован!')
        await ctx.send(embed = emb)

@client.command()
async def gift_2341 (ctx, member:discord.Member):
    global gift_6

    if gift_6:
        await ctx.channel.purge(limit=1)
        pup_role = discord.utils.get(ctx.message.guild.roles, name='⭐')
        emb = discord.Embed(title = 'ПОЗДРАВЛЯЕМ!', colour = discord.Color.gold(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Вы получили подарок!')
        await ctx.send(embed = emb)
        await member.add_roles(pup_role)
        gift_6 = False
    else:
        await ctx.channel.purge(limit=1)
        emb = discord.Embed(title = 'ОШИБКА!', colour = discord.Color.red(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Код уже использован!')
        await ctx.send(embed = emb)

@client.command()
async def gift_7857 (ctx, member:discord.Member):
    global gift_7

    if gift_7:
        await ctx.channel.purge(limit=1)
        pup_role = discord.utils.get(ctx.message.guild.roles, name='⭐')
        emb = discord.Embed(title = 'ПОЗДРАВЛЯЕМ!', colour = discord.Color.gold(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Вы получили подарок!')
        await ctx.send(embed = emb)
        await member.add_roles(pup_role)
        gift_7 = False
    else:
        await ctx.channel.purge(limit=1)
        emb = discord.Embed(title = 'ОШИБКА!', colour = discord.Color.red(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Код уже использован!')
        await ctx.send(embed = emb)

@client.command()
async def gift_2432 (ctx, member:discord.Member):
    global gift_8

    if gift_8:
        await ctx.channel.purge(limit=1)
        pup_role = discord.utils.get(ctx.message.guild.roles, name='⭐')
        emb = discord.Embed(title = 'ПОЗДРАВЛЯЕМ!', colour = discord.Color.gold(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Вы получили подарок!')
        await ctx.send(embed = emb)
        await member.add_roles(pup_role)
        gift_8 = False
    else:
        await ctx.channel.purge(limit=1)
        emb = discord.Embed(title = 'ОШИБКА!', colour = discord.Color.red(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Код уже использован!')
        await ctx.send(embed = emb)

@client.command()
async def gift_9578 (ctx, member:discord.Member):
    global gift_9

    if gift_9:
        await ctx.channel.purge(limit=1)
        pup_role = discord.utils.get(ctx.message.guild.roles, name='⭐')
        emb = discord.Embed(title = 'ПОЗДРАВЛЯЕМ!', colour = discord.Color.gold(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Вы получили подарок!')
        await ctx.send(embed = emb)
        await member.add_roles(pup_role)
        gift_9 = False
    else:
        await ctx.channel.purge(limit=1)
        emb = discord.Embed(title = 'ОШИБКА!', colour = discord.Color.red(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Код уже использован!')
        await ctx.send(embed = emb)

@client.command()
async def gift_9869 (ctx, member:discord.Member):
    global gift_10

    if gift_10:
        await ctx.channel.purge(limit=1)
        pup_role = discord.utils.get(ctx.message.guild.roles, name='⭐')
        emb = discord.Embed(title = 'ПОЗДРАВЛЯЕМ!', colour = discord.Color.gold(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Вы получили подарок!')
        await ctx.send(embed = emb)
        await member.add_roles(pup_role)
        gift_10 = False
    else:
        await ctx.channel.purge(limit=1)
        emb = discord.Embed(title = 'ОШИБКА!', colour = discord.Color.red(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Код уже использован!')
        await ctx.send(embed = emb)

@client.command()
async def gift_2344 (ctx, member:discord.Member):
    global gift_11

    if gift_11:
        await ctx.channel.purge(limit=1)
        pup_role = discord.utils.get(ctx.message.guild.roles, name='🔥')
        emb = discord.Embed(title = 'ПОЗДРАВЛЯЕМ!', colour = discord.Color.gold(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Вы получили подарок!')
        await ctx.send(embed = emb)
        await member.add_roles(pup_role)
        gift_11 = False
    else:
        await ctx.channel.purge(limit=1)
        emb = discord.Embed(title = 'ОШИБКА!', colour = discord.Color.red(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Код уже использован!')
        await ctx.send(embed = emb)

@client.command()
async def gift_3452 (ctx, member:discord.Member):
    global gift_12

    if gift_12:
        await ctx.channel.purge(limit=1)
        pup_role = discord.utils.get(ctx.message.guild.roles, name='🔥')
        emb = discord.Embed(title = 'ПОЗДРАВЛЯЕМ!', colour = discord.Color.gold(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Вы получили подарок!')
        await ctx.send(embed = emb)
        await member.add_roles(pup_role)
        gift_12 = False
    else:
        await ctx.channel.purge(limit=1)
        emb = discord.Embed(title = 'ОШИБКА!', colour = discord.Color.red(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Код уже использован!')
        await ctx.send(embed = emb)

@client.command()
async def gift_1321 (ctx, member:discord.Member):
    global gift_13

    if gift_13:
        await ctx.channel.purge(limit=1)
        pup_role = discord.utils.get(ctx.message.guild.roles, name='🔥')
        emb = discord.Embed(title = 'ПОЗДРАВЛЯЕМ!', colour = discord.Color.gold(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Вы получили подарок!')
        await ctx.send(embed = emb)
        await member.add_roles(pup_role)
        gift_13 = False
    else:
        await ctx.channel.purge(limit=1)
        emb = discord.Embed(title = 'ОШИБКА!', colour = discord.Color.red(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Код уже использован!')
        await ctx.send(embed = emb)

@client.command()
async def gift_3424 (ctx, member:discord.Member):
    global gift_14

    if gift_14:
        await ctx.channel.purge(limit=1)
        pup_role = discord.utils.get(ctx.message.guild.roles, name='🔥')
        emb = discord.Embed(title = 'ПОЗДРАВЛЯЕМ!', colour = discord.Color.gold(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Вы получили подарок!')
        await ctx.send(embed = emb)
        await member.add_roles(pup_role)
        gift_14 = False
    else:
        await ctx.channel.purge(limit=1)
        emb = discord.Embed(title = 'ОШИБКА!', colour = discord.Color.red(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Код уже использован!')
        await ctx.send(embed = emb)

@client.command()
async def gift_1233 (ctx, member:discord.Member):
    global gift_15

    if gift_15:
        await ctx.channel.purge(limit=1)
        pup_role = discord.utils.get(ctx.message.guild.roles, name='🔥')
        emb = discord.Embed(title = 'ПОЗДРАВЛЯЕМ!', colour = discord.Color.gold(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Вы получили подарок!')
        await ctx.send(embed = emb)
        await member.add_roles(pup_role)
        gift_15 = False
    else:
        await ctx.channel.purge(limit=1)
        emb = discord.Embed(title = 'ОШИБКА!', colour = discord.Color.red(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Код уже использован!')
        await ctx.send(embed = emb)

@client.command()
async def gift_6788 (ctx, member:discord.Member):
    global gift_16

    if gift_16:
        await ctx.channel.purge(limit=1)
        pup_role = discord.utils.get(ctx.message.guild.roles, name='💀')
        emb = discord.Embed(title = 'ПОЗДРАВЛЯЕМ!', colour = discord.Color.gold(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Вы получили подарок!')
        await ctx.send(embed = emb)
        await member.add_roles(pup_role)
        gift_16 = False
    else:
        await ctx.channel.purge(limit=1)
        emb = discord.Embed(title = 'ОШИБКА!', colour = discord.Color.red(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Код уже использован!')
        await ctx.send(embed = emb)

@client.command()
async def gift_4764 (ctx, member:discord.Member):
    global gift_17

    if gift_17:
        await ctx.channel.purge(limit=1)
        pup_role = discord.utils.get(ctx.message.guild.roles, name='💀')
        emb = discord.Embed(title = 'ПОЗДРАВЛЯЕМ!', colour = discord.Color.gold(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Вы получили подарок!')
        await ctx.send(embed = emb)
        await member.add_roles(pup_role)
        gift_17 = False
    else:
        await ctx.channel.purge(limit=1)
        emb = discord.Embed(title = 'ОШИБКА!', colour = discord.Color.red(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Код уже использован!')
        await ctx.send(embed = emb)

@client.command()
async def gift_9809 (ctx, member:discord.Member):
    global gift_18

    if gift_18:
        await ctx.channel.purge(limit=1)
        pup_role = discord.utils.get(ctx.message.guild.roles, name='💀')
        emb = discord.Embed(title = 'ПОЗДРАВЛЯЕМ!', colour = discord.Color.gold(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Вы получили подарок!')
        await ctx.send(embed = emb)
        await member.add_roles(pup_role)
        gift_18 = False
    else:
        await ctx.channel.purge(limit=1)
        emb = discord.Embed(title = 'ОШИБКА!', colour = discord.Color.red(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Код уже использован!')
        await ctx.send(embed = emb)

@client.command()
async def gift_5678 (ctx, member:discord.Member):
    global gift_19

    if gift_19:
        await ctx.channel.purge(limit=1)
        pup_role = discord.utils.get(ctx.message.guild.roles, name='💀')
        emb = discord.Embed(title = 'ПОЗДРАВЛЯЕМ!', colour = discord.Color.gold(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Вы получили подарок!')
        await ctx.send(embed = emb)
        await member.add_roles(pup_role)
        gift_19 = False
    else:
        await ctx.channel.purge(limit=1)
        emb = discord.Embed(title = 'ОШИБКА!', colour = discord.Color.red(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Код уже использован!')
        await ctx.send(embed = emb)

@client.command()
async def gift_1214 (ctx, member:discord.Member):
    global gift_20

    if gift_20:
        await ctx.channel.purge(limit=1)
        pup_role = discord.utils.get(ctx.message.guild.roles, name='👑')
        emb = discord.Embed(title = 'ПОЗДРАВЛЯЕМ!', colour = discord.Color.gold(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Вы получили подарок!')
        await ctx.send(embed = emb)
        await member.add_roles(pup_role)
        gift_20 = False
    else:
        await ctx.channel.purge(limit=1)
        emb = discord.Embed(title = 'ОШИБКА!', colour = discord.Color.red(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Код уже использован!')
        await ctx.send(embed = emb)

@client.command()
async def gift_2353 (ctx, member:discord.Member):
    global gift_21

    if gift_21:
        await ctx.channel.purge(limit=1)
        pup_role = discord.utils.get(ctx.message.guild.roles, name='👑')
        emb = discord.Embed(title = 'ПОЗДРАВЛЯЕМ!', colour = discord.Color.gold(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Вы получили подарок!')
        await ctx.send(embed = emb)
        await member.add_roles(pup_role)
        gift_21 = False
    else:
        await ctx.channel.purge(limit=1)
        emb = discord.Embed(title = 'ОШИБКА!', colour = discord.Color.red(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Код уже использован!')
        await ctx.send(embed = emb)

@client.command()
async def gift_3463 (ctx, member:discord.Member):
    global gift_22

    if gift_22:
        await ctx.channel.purge(limit=1)
        pup_role = discord.utils.get(ctx.message.guild.roles, name='👑')
        emb = discord.Embed(title = 'ПОЗДРАВЛЯЕМ!', colour = discord.Color.gold(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Вы получили подарок!')
        await ctx.send(embed = emb)
        await member.add_roles(pup_role)
        gift_22 = False
    else:
        await ctx.channel.purge(limit=1)
        emb = discord.Embed(title = 'ОШИБКА!', colour = discord.Color.red(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Код уже использован!')
        await ctx.send(embed = emb)

@client.command()
async def gift_1231 (ctx, member:discord.Member):
    global gift_23

    if gift_23:
        await ctx.channel.purge(limit=1)
        pup_role = discord.utils.get(ctx.message.guild.roles, name='👑')
        emb = discord.Embed(title = 'ПОЗДРАВЛЯЕМ!', colour = discord.Color.gold(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Вы получили подарок!')
        await ctx.send(embed = emb)
        await member.add_roles(pup_role)
        gift_23 = False
    else:
        await ctx.channel.purge(limit=1)
        emb = discord.Embed(title = 'ОШИБКА!', colour = discord.Color.red(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Код уже использован!')
        await ctx.send(embed = emb)

@client.command()
async def gift_7698 (ctx, member:discord.Member):
    global gift_24

    if gift_24:
        await ctx.channel.purge(limit=1)
        pup_role = discord.utils.get(ctx.message.guild.roles, name='👑')
        emb = discord.Embed(title = 'ПОЗДРАВЛЯЕМ!', colour = discord.Color.gold(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Вы получили подарок!')
        await ctx.send(embed = emb)
        await member.add_roles(pup_role)
        gift_24 = False
    else:
        await ctx.channel.purge(limit=1)
        emb = discord.Embed(title = 'ОШИБКА!', colour = discord.Color.red(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Код уже использован!')
        await ctx.send(embed = emb)

@client.command()
async def gift_3453 (ctx, member:discord.Member):
    global gift_25

    if gift_25:
        await ctx.channel.purge(limit=1)
        pup_role = discord.utils.get(ctx.message.guild.roles, name='❤️')
        emb = discord.Embed(title = 'ПОЗДРАВЛЯЕМ!', colour = discord.Color.gold(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Вы получили подарок!')
        await ctx.send(embed = emb)
        await member.add_roles(pup_role)
        gift_25 = False
    else:
        await ctx.channel.purge(limit=1)
        emb = discord.Embed(title = 'ОШИБКА!', colour = discord.Color.red(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Код уже использован!')
        await ctx.send(embed = emb)

@client.command()
async def gift_4574 (ctx, member:discord.Member):
    global gift_26

    if gift_26:
        await ctx.channel.purge(limit=1)
        pup_role = discord.utils.get(ctx.message.guild.roles, name='❤️')
        emb = discord.Embed(title = 'ПОЗДРАВЛЯЕМ!', colour = discord.Color.gold(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Вы получили подарок!')
        await ctx.send(embed = emb)
        await member.add_roles(pup_role)
        gift_26 = False
    else:
        await ctx.channel.purge(limit=1)
        emb = discord.Embed(title = 'ОШИБКА!', colour = discord.Color.red(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Код уже использован!')
        await ctx.send(embed = emb)

@client.command()
async def gift_8796 (ctx, member:discord.Member):
    global gift_27

    if gift_27:
        await ctx.channel.purge(limit=1)
        pup_role = discord.utils.get(ctx.message.guild.roles, name='❤️')
        emb = discord.Embed(title = 'ПОЗДРАВЛЯЕМ!', colour = discord.Color.gold(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Вы получили подарок!')
        await ctx.send(embed = emb)
        await member.add_roles(pup_role)
        gift_27 = False
    else:
        await ctx.channel.purge(limit=1)
        emb = discord.Embed(title = 'ОШИБКА!', colour = discord.Color.red(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Код уже использован!')
        await ctx.send(embed = emb)

@client.command()
async def gift_4576 (ctx, member:discord.Member):
    global gift_28

    if gift_28:
        await ctx.channel.purge(limit=1)
        pup_role = discord.utils.get(ctx.message.guild.roles, name='🐲')
        emb = discord.Embed(title = 'ПОЗДРАВЛЯЕМ!', colour = discord.Color.gold(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Вы получили подарок!')
        await ctx.send(embed = emb)
        await member.add_roles(pup_role)
        gift_28 = False
    else:
        await ctx.channel.purge(limit=1)
        emb = discord.Embed(title = 'ОШИБКА!', colour = discord.Color.red(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Код уже использован!')
        await ctx.send(embed = emb)

@client.command()
async def gift_2467 (ctx, member:discord.Member):
    global gift_29

    if gift_29:
        await ctx.channel.purge(limit=1)
        pup_role = discord.utils.get(ctx.message.guild.roles, name='🐲')
        emb = discord.Embed(title = 'ПОЗДРАВЛЯЕМ!', colour = discord.Color.gold(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Вы получили подарок!')
        await ctx.send(embed = emb)
        await member.add_roles(pup_role)
        gift_29 = False
    else:
        await ctx.channel.purge(limit=1)
        emb = discord.Embed(title = 'ОШИБКА!', colour = discord.Color.red(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Код уже использован!')
        await ctx.send(embed = emb)

@client.command()
async def gift_2452 (ctx, member:discord.Member):
    global gift_30

    if gift_30:
        await ctx.channel.purge(limit=1)
        pup_role = discord.utils.get(ctx.message.guild.roles, name='🐲')
        emb = discord.Embed(title = 'ПОЗДРАВЛЯЕМ!', colour = discord.Color.gold(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Вы получили подарок!')
        await ctx.send(embed = emb)
        await member.add_roles(pup_role)
        gift_30 = False
    else:
        await ctx.channel.purge(limit=1)
        emb = discord.Embed(title = 'ОШИБКА!', colour = discord.Color.red(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Код уже использован!')
        await ctx.send(embed = emb)

@client.command()
async def gift_3947 (ctx, member:discord.Member):
    global gift_31

    if gift_31:
        await ctx.channel.purge(limit=1)
        pup_role = discord.utils.get(ctx.message.guild.roles, name='💎')
        emb = discord.Embed(title = 'ПОЗДРАВЛЯЕМ!', colour = discord.Color.gold(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Вы получили подарок!')
        await ctx.send(embed = emb)
        await member.add_roles(pup_role)
        gift_31 = False
    else:
        await ctx.channel.purge(limit=1)
        emb = discord.Embed(title = 'ОШИБКА!', colour = discord.Color.red(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Код уже использован!')
        await ctx.send(embed = emb)

@client.command()
async def gift_1241 (ctx, member:discord.Member):
    global gift_32

    if gift_32:
        await ctx.channel.purge(limit=1)
        pup_role = discord.utils.get(ctx.message.guild.roles, name='💎')
        emb = discord.Embed(title = 'ПОЗДРАВЛЯЕМ!', colour = discord.Color.gold(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Вы получили подарок!')
        await ctx.send(embed = emb)
        await member.add_roles(pup_role)
        gift_32 = False
    else:
        await ctx.channel.purge(limit=1)
        emb = discord.Embed(title = 'ОШИБКА!', colour = discord.Color.red(), url = None)
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name ='------------', value = 'Код уже использован!')
        await ctx.send(embed = emb)

#Mute

@client.command()
@commands.has_permissions(kick_members=True)

async def mute (ctx, member: discord.Member):
    await ctx.channel.purge(limit=1)

    mrole = discord.utils.get(ctx.message.guild.roles, name='Muted')

    emb = discord.Embed( title = 'ВНИМАНИЕ!',colour = discord.Color.purple(),url = None )

    emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url )
    
    emb.add_field( name ='----------------', value = 'У {} ограничения чата за нарушение прав!'.format(member.mention) )

    await ctx.send(embed = emb)
    await member.add_roles( mrole )

#Time

@client.command(pass_context = True)
#@tasks.loop(seconds=60)
async def time(ctx):
    await ctx.channel.purge(limit=1) 
    offset = datetime.timezone(datetime.timedelta(hours=3))
    moscow_time = datetime.datetime.now(offset)
    #await client.change_presence(status=discord.Status.online, activity=discord.Game(f'{moscow_time.hour} : {moscow_time.minute}'))
    emb = discord.Embed( title = 'ВРЕМЯ!',colour = discord.Color.purple(),url = None )
    emb.add_field( name ='---------', value = f'Время МСК: {moscow_time.hour} : {moscow_time.minute}') 
    await ctx.send(embed = emb)

#Unmute
@client.command()
@commands.has_permissions(kick_members=True)

async def unmute(ctx, member: discord.Member):
    await ctx.channel.purge(limit=1) 

    drole = discord.utils.get(ctx.message.guild.roles, name = 'Muted')
    
    #await ctx.send(f"{} снял ограничения чата у{member.mention}")
    emb = discord.Embed( title = 'ВНИМАНИЕ!',colour = discord.Color.purple(),url = None )

    emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url )
    
    emb.add_field( name ='----------------', value = 'У {} сняли ограничения чата!'.format(member.mention) )

    await ctx.send(embed = emb)
    await member.remove_roles(drole)

#Join
@client.command()
@client.event

async def on_member_join( member ):
    channel = client.get_channel( 698183270466060349 )
    await member.send(f'Поздравляем {member.mention}! теперь Вы часть нашего клана! Добро пожаловать на сервер! ')
    role = discord.utils.get( member.guild.roles, id = 698157175561912543 )

    await member.add_roles( role )
    #emb = discord.Embed( title = 'НОВЫЙ УЧАСТНИК!',colour = discord.Color.purple(),url = None )
    await channel.send( embed = discord.Embed( description = f'Пользователь { member.mention }, присоединился к нам! Добро пожаловать!', colour = discord.Color.purple() ) )

#Clear
    
@client.command( pass_context = True )
@commands.has_permissions( kick_members = True )

async def clear( ctx, amount = 1000 ):
    await ctx.channel.purge(limit = amount+1)

    emb = discord.Embed( title = 'УДАЛЕНИЕ', description = f'Удалено: {amount} сообщений',colour = discord.Color.purple(),url = None )
    await ctx.send(embed = emb)
    
#Help
    
@client.command( pass_context = True )

async def help( ctx ):
    await ctx.channel.purge (limit = 1)

    emb = discord.Embed( title = 'ИНФОРМАЦИЯ', description = 'ГИД по коммандам:',colour = discord.Color.purple(),url = None )

    emb.add_field( name ='//help', value = 'Инструкция по коммандам' )
    emb.add_field( name ='//clear', value = 'Очистка чата')
    emb.add_field( name ='//kick', value = 'Выгнать участника')
    emb.add_field( name ='//ban', value = 'Заблокировать участника')
    emb.add_field( name ='//mute', value = 'Ограничить чат участника')
    emb.add_field( name ='//unmute', value = 'Убрать ограничения чата участника')
    emb.add_field( name ='//time', value = 'Посмотреть текущее время')
    emb.add_field( name ='//donate', value = 'Помочь клану')
    emb.add_field( name ='//gift_(код подарка)', value = 'Получить подарок')
    emb.add_field( name ='@Natsuki_bot', value = 'by @_Rayyy, ver 1.9')
    await ctx.send(embed = emb)
    
#Kick

@client.command( pass_context = True )
@commands.has_permissions( kick_members = True )

async def kick( ctx, member: discord.Member, *, reason = None):

    await ctx.channel.purge (limit = 1)
    emb = discord.Embed( title = 'ВНИМАНИЕ!',colour = discord.Color.purple(),url = None )

    emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url )
    await member.send(f'{member.mention}, Вы были выгнаны из сервера! Причина: {reason}')
    #emb.set_thumbnail( url = '' )
    emb.add_field( name ='Kicked', value = 'ВЫГНАН УЧАСТНИК: {}'.format(member.mention) )
    emb.add_field( name ='Reason', value = f'ПРИЧИНА: {reason} ' )
    await ctx.send(embed = emb)
    #await message.author.send(f'{message.author.name}, вы были выгнаны из сервера! Причина: {reason}')
    await member.kick( reason = reason )
    #await ctx.send( f'АДМИНОМ ОТПИЗЖЕН {member.mention}')
    
 
#Ban

@client.command( pass_context = True )
@commands.has_permissions( ban_members = True )

async def ban( ctx, member: discord.Member, *, reason = None):
    await ctx.channel.purge (limit = 1)
    emb = discord.Embed( title = 'ВНИМАНИЕ!',colour = discord.Color.purple(),url = None )
    await member.send(f'{member.mention}, Вы были заблокированы на сервере! Причина: {reason}')
    emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url )
    #emb.set_footer( text = ctx.author.name, icon_url = ctx.author.avatar_url )
    #emb.set_thumbnail( url = '' )
    emb.add_field( name ='Banned', value = 'ЗАБАНЕН УЧАСТНИК: {}'.format(member.mention) )
    emb.add_field( name ='Reason', value = f'ПРИЧИНА: {reason} ' )
    await ctx.send(embed = emb)
    await member.ban( reason = reason )
     #await ctx.send( f'АДМИНОМ ВЫЕБАН {member.mention}')


#Embed

@client.command( pass_context = True )
@commands.has_permissions( ban_members = True )

async def test( ctx ):
    emb = discord.Embed( title = 'Тестовая хуйня', description = 'КАКАЯ-ТО ПОЕБОТА ОТ АДМИНА',colour = discord.Color.purple(),url = None )

    #emb.set_author( name =  client.user.name, icon_url = client.user.avatar_url )
    #emb.set_footer( text = ctx.author.name, icon_url = ctx.author.avatar_url )
    #emb.set_thumbnail( url = '' )

    await ctx.send(embed = emb)
#Connect

@client.command( pass_context = True )
async def donate( ctx ):
    await ctx.channel.purge (limit = 1)

    emb = discord.Embed( title = 'Донат', description = 'Заплатите 55 руб., либо потратьте золото в благо клана, чтобы открыть роль V.I.P и использовать секретные комманды!',colour = discord.Color.purple(),url = None )

    emb.add_field( name ='-------', value = 'Перейдите по ссылке: https://www.donationalerts.com/r/rayyyyyy' )

    await ctx.send(embed = emb)

@client.command(pass_context=True)
@commands.has_role("V.I.P")
async def flash (ctx, member: discord.Member):
    await ctx.channel.purge(limit=1)

    frole = discord.utils.get(ctx.message.guild.roles, name='Flashed')

    emb = discord.Embed( title = 'ВНИМАНИЕ!',colour = discord.Color.purple(),url = None )

    emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url )
    
    emb.add_field( name ='----------------', value = '{} был ослеплен!'.format(member.mention) )

    await ctx.send(embed = emb)
    await member.add_roles( frole )
    #emb.set_author( name =  client.user.name, icon_url = client.user.avatar_url )
    #emb.set_footer( text = ctx.author.name, icon_url = ctx.author.avatar_url )
    #emb.set_thumbnail( url = '' )

    await ctx.send(embed = emb)
            #await client.change_nickname()

@client.command()
@commands.has_role("V.I.P")

async def unflash(ctx, member: discord.Member):
    await ctx.channel.purge(limit=1) 

    frole = discord.utils.get(ctx.message.guild.roles, name = 'Flashed')
    
    #await ctx.send(f"{} снял ограничения чата у{member.mention}")
    emb = discord.Embed( title = 'ВНИМАНИЕ!',colour = discord.Color.purple(),url = None )

    emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url )
    
    emb.add_field( name ='----------------', value = '{} теперь все видит!'.format(member.mention) )

    await ctx.send(embed = emb)
    await member.remove_roles(frole)
    
token = os.environ.get('TOKEN')

client.run(str(token))
  
