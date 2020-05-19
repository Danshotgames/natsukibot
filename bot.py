import discord
from discord.ext import commands, tasks
import asyncio
import random
import os
import datetime
from discord import Webhook, RequestsWebhookAdapter
from random import randint
import sys
import traceback
from discord.ext.commands import Bot

client = discord.Client()

client = commands.Bot( command_prefix = '//' )

client.remove_command('help')

@client.command()
async def rct(ctx,id:int,reaction:str):
    await ctx.message.delete()
    message = await ctx.message.channel.fetch_message(id)
    await message.add_reaction(reaction)

@client.event
async def on_raw_reaction_add(payload):
    
    if payload.message_id == 704322752974291004: # ID Сообщения
        guild = client.get_guild(payload.guild_id)
        role = None
        role2 = None
        role3 = None
        role4 = None
        channel = client.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)

        if str(payload.emoji) == '😄': # Emoji для реакций
            role = guild.get_role(704324146569412679)
        
        if str(payload.emoji) == '😐': # Emoji для реакций
            role2 = guild.get_role(704324310143336468)  
        
        if str(payload.emoji) == '😔': # Emoji для реакций
            role3 = guild.get_role(704324450824486972) 
        
        if str(payload.emoji) == '😡': # Emoji для реакций
            role4 = guild.get_role(704324571188428840) 

        if role2:
            member = guild.get_member(payload.user_id)
            if member:
                if(len([i for i in member.roles if i.id not in config.EXCROLES]) <= config.MAX_ROLES_PER_USER):
                    await member.add_roles(role2)
                    print('[SUCCESS] User {0.display_name} has been granted with role {1.name}'.format(member, role))
                else:
                    await message.remove_reaction(payload.emoji, member)
                    print('[ERROR] Too many roles for user {0.display_name}'.format(member))

        if role:
            member = guild.get_member(payload.user_id)
            if member:
                if(len([i for i in member.roles if i.id not in config.EXCROLES]) <= config.MAX_ROLES_PER_USER):
                    await member.add_roles(role)
                    print('[SUCCESS] User {0.display_name} has been granted with role {1.name}'.format(member, role))
                else:
                    await message.remove_reaction(payload.emoji, member)
                    print('[ERROR] Too many roles for user {0.display_name}'.format(member))
        if role3:
            member = guild.get_member(payload.user_id)
            if member:
                if(len([i for i in member.roles if i.id not in config.EXCROLES]) <= config.MAX_ROLES_PER_USER):
                    await member.add_roles(role3)
                    print('[SUCCESS] User {0.display_name} has been granted with role {1.name}'.format(member, role))
                else:
                    await message.remove_reaction(payload.emoji, member)
                    print('[ERROR] Too many roles for user {0.display_name}'.format(member))
        if role4:
            member = guild.get_member(payload.user_id)
            if member:
                if(len([i for i in member.roles if i.id not in config.EXCROLES]) <= config.MAX_ROLES_PER_USER):
                    await member.add_roles(role4)
                    print('[SUCCESS] User {0.display_name} has been granted with role {1.name}'.format(member, role))
                else:
                    await message.remove_reaction(payload.emoji, member)
                    print('[ERROR] Too many roles for user {0.display_name}'.format(member))
    
    if payload.message_id == 704262869713158195: # ID Сообщения
        guild = client.get_guild(payload.guild_id)
        role = None

        if str(payload.emoji) == '✅': # Emoji для реакций
            role = guild.get_role(704206253525696533) # ID Ролей для выдачи
            role2 = guild.get_role(704206642291540028) # ID Ролей для выдачи
        if role2:
            member = guild.get_member(payload.user_id)
            if member:
                await member.remove_roles(role2)

        if role:
            member = guild.get_member(payload.user_id)
            if member:
                await member.add_roles(role)

@client.event
async def on_raw_reaction_remove(payload):
    if payload.message_id == 704322752974291004: # ID Сообщения
        guild = client.get_guild(payload.guild_id)
        role = None
        role2 = None
        role3 = None
        role4 = None

        if str(payload.emoji) == '😄': # Emoji для реакций
            role = guild.get_role(704324146569412679)
        
        if str(payload.emoji) == '😐': # Emoji для реакций
            role2 = guild.get_role(704324310143336468)  
        
        if str(payload.emoji) == '😔': # Emoji для реакций
            role3 = guild.get_role(704324450824486972) 
        
        if str(payload.emoji) == '😡': # Emoji для реакций
            role4 = guild.get_role(704324571188428840) 

        if role2:
            member = guild.get_member(payload.user_id)
            if member:
                await member.remove_roles(role2)

        if role:
            member = guild.get_member(payload.user_id)
            if member:
                await member.remove_roles(role)
        if role3:
            member = guild.get_member(payload.user_id)
            if member:
                await member.remove_roles(role3)
        if role4:
            member = guild.get_member(payload.user_id)
            if member:
                await member.remove_roles(role4)

@client.command()
async def botinfo(ctx):

    embed = discord.Embed(title=f"{ctx.guild.name}", description="Информация о боте **Natsuki**.\n Бот был написан специально для клана AFFERs,\n подробнее о командах - //help", colour = discord.Color.purple())
    embed.add_field(name=f'**Создатель:**', value="_Rayyy", inline=True)  # Создает строку
    embed.add_field(name=f'**Помощь в создании:**', value="_Rayyy", inline=True)  # Создает строку
    embed.add_field(name=f'**Лицензия:**', value="Sv-1G-WD-Ui", inline=True)  # Создает строку
    embed.add_field(name=f'**Написан на:**', value="Discord.py", inline=True)  # Создает строку
    embed.add_field(name=f'**Версия:**', value="2.3", inline=True)  # Создает строку
    embed.add_field(name=f'**Патч:**', value="3.8.2", inline=True)  # Создает строку
    embed.set_thumbnail( url = "https://images-ext-2.discordapp.net/external/F-OHTcCXkzVPRbLkFChv-PbqYyC8RYx2L19dXQITEDQ/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/696677196349177906/18e4922dde1f1cbdd89a8044696415fc.webp?width=475&height=475")
    embed.set_footer(text=f"© Copyright 2020 _Rayyy#6698 | Все права защищены")  # создаение футера
    await ctx.send(embed=embed)

@client.command()
@commands.has_role("👑 VIP 👑")
async def gif(ctx, arg, *, txt = ''):
    await ctx.message.delete()
    guild = ctx.guild
    em = str(discord.utils.get(guild.emojis, name=f'{arg}'))
    w = await ctx.channel.create_webhook(name=ctx.author.name)
    await w.send(f'{txt} {em}', avatar_url=ctx.author.avatar_url)
        
    await w.delete()

#Time

@client.event
async def on_ready():
    print("Bot is ready!")
    while True:
        await client.change_presence(status = discord.Status.online, activity = discord.Game('💛 Standoff 2 | AFF 💛'))
        await asyncio.sleep(4)
        await client.change_presence(status = discord.Status.online, activity = discord.Game('💜 Standoff 2 | AFF 💜'))
        #await client.change_presence(status = discord.Status.online, activity = discord.Activity(type = discord.ActivityType.watching, name="за сервером | AFF "))
        await asyncio.sleep(4)
        await client.change_presence(status = discord.Status.online, activity = discord.Game('💙 Standoff 2 | AFF 💙'))
        #await client.change_presence(status = discord.Status.online, activity = discord.Activity(type = discord.ActivityType.listening, name = "Я робот долбаеб | AFF "))
        await asyncio.sleep(4)

@client.command(pass_context = True)
#@tasks.loop(seconds=60)
async def time(ctx):
    await ctx.channel.purge(limit=1) 
    offset = datetime.timezone(datetime.timedelta(hours=3))
    moscow_time = datetime.datetime.now(offset)
    #await client.change_presence(status=discord.Status.online, activity=discord.Game(f'{moscow_time.hour} : {moscow_time.minute}'))
    emb = discord.Embed( title = f'Время МСК: {moscow_time.hour} : {moscow_time.minute}',colour = discord.Color.purple(),url = None )
    await ctx.send(embed = emb)

#Clear
    
@client.command( pass_context = True )
@commands.has_permissions( kick_members = True )

async def clear( ctx, amount = 1000 ):
    await ctx.channel.purge(limit = amount+1)

    emb = discord.Embed( title = f'Очищено: {amount} сообщений',colour = discord.Color.purple(),url = None )
    emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url )
    await ctx.send(embed = emb)
    
#Help
    
@client.command( pass_context = True )

async def help( ctx ):
    await ctx.channel.purge (limit = 1)

    emb = discord.Embed( title = 'ИНФОРМАЦИЯ', description = 'ГИД по коммандам:',colour = discord.Color.purple(),url = None )

    emb.add_field( name ='//help', value = 'Инструкция по коммандам' )
    emb.add_field( name ='//clear', value = 'Очистка чата')
    
    
   
    emb.add_field( name ='//time', value = 'Посмотреть текущее время')
    emb.add_field( name ='//botinfo', value = 'Информация о боте')
    emb.add_field( name ='//serverinfo', value = 'Информация о сервере')
    emb.add_field( name ='//userinfo', value = 'Информация об участнике')
    emb.add_field( name ='//suggest', value = 'Предложить идею')
    emb.add_field( name ='//gif', value = 'Отправить gif-emoji из сервера')
    emb.add_field( name ='//ball', value = 'Магический шар')
    emb.add_field( name ='//say', value = 'Говорить ботом')
    emb.set_thumbnail(url=ctx.guild.icon_url)
    await ctx.send(embed = emb)
  

#Userinfo

@client.command()
async def userinfo(ctx, Member: discord.Member = None ):
    await ctx.channel.purge (limit = 1)
    if not Member:
        Member = ctx.author
    roles = (role for role in Member.roles )
    emb = discord.Embed(title='Информация о пользователе.'.format(Member.name), description=f"Участник зашёл на сервер: {Member.joined_at.strftime('%b %#d, %Y')}\n\n "
                                                                                      f"Имя: {Member.name}\n\n"
                                                                                      f"Никнейм: {Member.nick}\n\n"
                                                                                      f"Статус: {Member.status}\n\n"
                                                                                      f"ID: {Member.id}\n\n"
                                                                                      f"Высшая роль: {Member.top_role}\n\n"
                                                                                      f"Аккаунт создан: {Member.created_at.strftime('%b %#d, %Y')}", 
                                                                                      colour = discord.Color.purple(), timestamp=ctx.message.created_at)

    emb.set_thumbnail(url= Member.avatar_url)
    emb.set_footer(icon_url= Member.avatar_url)
    emb.set_footer(text='Команда вызвана: {}'.format(ctx.author.name), icon_url=ctx.author.avatar_url)
    await ctx.send(embed=emb)

#Serverinfo

@client.command()
async def serverinfo(ctx, member: discord.Member = None):
    await ctx.channel.purge (limit = 1)
    if not member:
        member = ctx.author

    guild = ctx.guild
    embed = discord.Embed(title=f"{guild.name}", description=f"Сервер создан: {guild.created_at.strftime('%b %#d, %Y')}\n\n"
                                                             f"Регион: {guild.region}\n\nГлава сервера: {guild.owner}\n\n"
                                                             f"Людей на сервере: {guild.member_count}\n\n",  colour = discord.Color.purple(),timestamp=ctx.message.created_at)

    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.set_footer(text=f"ID: {guild.id}")

    embed.set_footer(text=f"ID Пользователя: {ctx.author.id}")
    await ctx.send(embed=embed)

#None_commands

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound ):
        await ctx.send(embed = discord.Embed(description = f'**{ctx.author.name}, данной команды не существует.**', colour = discord.Color.red())) 

#Logs

@client.event
async def on_message_edit(before, after):
    channel = client.get_channel(703223484574334976)
    if before.author == client.user:
        return
    if before.content is None:
        return
    elif after.content is None:
        return
    message_edit = discord.Embed(colour=0xff0000,
                                 description=f"**{before.author} Изменил сообщение в канале {before.channel}** "
                                             f"\nСтарое сообщение: {before.content}"
                                             f"\n\nНовое сообщение: {after.content}",timestamp=before.created_at)

    message_edit.set_author(name=f"{before.author}",icon_url=f"{before.author.avatar_url}")
    message_edit.set_footer(text=f"ID Пользователя: {before.author.id} | ID Сообщения: {before.id}")
    await channel.send(embed=message_edit)
    return

@client.event
async def on_message_delete(message):
    channel = client.get_channel(703223484574334976)
    if message.content is None:
        return
    embed = discord.Embed(colour=0xff0000, description=f"**{message.author} Удалил сообщение в канале {message.channel}** \n{message.content}",timestamp=message.created_at)

    embed.set_author(name=f"{message.author}", icon_url=f'{message.author.avatar_url}')
    embed.set_footer(text=f'ID Пользователя: {message.author.id} | ID Сообщения: {message.id}')
    await channel.send(embed=embed)
    return

@client.command()
@commands.has_permissions( ban_members = True)
async def say(ctx, *, arg):

    await ctx.message.delete()
    await ctx.send(embed = discord.Embed(description = f'{arg}', colour = discord.Color.purple()))

@client.command()
async def ball(ctx, *, arg):

    message = ['Нет','Да','Возможно','Опредленно нет'] 
    s = random.choice( message )
    await ctx.send(embed = discord.Embed(description = f'**:crystal_ball: Знаки говорят: ** {s}', colour = discord.Color.purple()))
    return

@client.command( pass_context = True)

async def suggest( ctx , * , agr ):
    await ctx.channel.purge (limit = 1)
    suggest_chanell = client.get_channel( 698168631758028840 ) #Айди канала предложки
    embed = discord.Embed(title=f"{ctx.author.name} Предложил :", description= f" {agr} \n\n")

    embed.set_thumbnail(url=ctx.guild.icon_url)

    message = await suggest_chanell.send(embed=embed)
    await message.add_reaction('✅')
    await message.add_reaction('❎')

    
token = os.environ.get('TOKEN')

client.run(str(token))
  
