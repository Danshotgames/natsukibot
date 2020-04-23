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

@client.event
async def on_ready():
    activity = discord.Game(name="Standoff 2 | AFF", type=3)
    await client.change_presence(status=discord.Status.online, activity=activity)
    print("Bot is ready!")

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
    await member.send(f'Поздравляем {member.mention}! теперь Вы часть нашего клана AFFERs! Добро пожаловать на сервер! Введите //help для помощи')
    role = discord.utils.get( member.guild.roles, id = 698157175561912543 )
    role2 = discord.utils.get( member.guild.roles, id = 690258154512318525 )

    await member.add_roles( role )
    await member.add_roles( role2 )
    #emb = discord.Embed( title = 'НОВЫЙ УЧАСТНИК!',colour = discord.Color.purple(),url = None )
    await channel.send( embed = discord.Embed( description = f'Пользователь { member.mention } присоединился к нам! Добро пожаловать!', colour = discord.Color.purple() ) )

#Clear
    
@client.command( pass_context = True )
@commands.has_permissions( kick_members = True )

async def clear( ctx, amount = 1000 ):
    await ctx.channel.purge(limit = amount+1)

    emb = discord.Embed( title = 'ОЧИСТКА', description = f'Очищено: {amount} сообщений',colour = discord.Color.purple(),url = None )
    emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url )
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
    emb.add_field( name ='//flash(VIP)', value = 'Ограничить доступ к каналу')
    emb.add_field( name ='//unflash(VIP)', value = 'Убрать ограничения доступа к каналу')
    emb.add_field( name ='//vanish(VIP)', value = 'Скрыть участника')
    emb.add_field( name ='//unvanish(VIP)', value = 'Раскрыть участника')
    emb.add_field( name ='NATSUKI-BOT', value = 'Owner: _Rayyy, ver 2.0')
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
@commands.has_permissions( kick_members = True )

async def secret( ctx ):
    emb = discord.Embed( title = 'Ебать секретно!!', description = 'ПИЗДЕЦ ТУТ ТАКОЙ СЕКРЕТ ПРОСТО АХУЕТЬ Я КОГДА УЗНАЛ ЧТО ЭТО БЫЛО А Х У Е Л НУ и ЧТОБ ПОСМОТРЕТЬ СЕКРЕТ ВВЕДИ //yoba!',colour = discord.Color.red(),url = None )

    #emb.set_author( name =  client.user.name, icon_url = client.user.avatar_url )
    #emb.set_footer( text = ctx.author.name, icon_url = ctx.author.avatar_url )
    #emb.set_thumbnail( url = '' )

    await ctx.send(embed = emb)

@client.command( pass_context = True )
@commands.has_permissions( kick_members = True )

async def yoba( ctx ):
    emb = discord.Embed( title = 'Секрет!!', description = 'Я вас наебал, никокого секрета нету гыг',colour = discord.Color.red(),url = None )

    #emb.set_author( name =  client.user.name, icon_url = client.user.avatar_url )
    #emb.set_footer( text = ctx.author.name, icon_url = ctx.author.avatar_url )
    #emb.set_thumbnail( url = '' )

    await ctx.send(embed = emb)

@client.command( pass_context = True )
@commands.has_permissions( ban_members = True )

async def test( ctx ):
    emb = discord.Embed( title = 'Ебать, тест нахуй!', description = 'Ну так то тут должен быть текст, но его как бы нету...',colour = discord.Color.purple(),url = None )

    #emb.set_author( name =  client.user.name, icon_url = client.user.avatar_url )
    #emb.set_footer( text = ctx.author.name, icon_url = ctx.author.avatar_url )
    #emb.set_thumbnail( url = '' )

    await ctx.send(embed = emb)
#Connect

@client.command( pass_context = True )
async def donate( ctx ):
    await ctx.channel.purge (limit = 1)

    emb = discord.Embed( title = 'Донат', description = 'Заплатите 55 руб., либо потратьте золото в благо клана, чтобы открыть роль V.I.P и использовать секретные комманды!',colour = discord.Color.gold(),url = None )

    emb.add_field( name ='-------', value = 'Перейдите по ссылке: https://www.donationalerts.com/r/rayyyyyy' )

    await ctx.send(embed = emb)


@client.command(pass_context=True)
@commands.has_role("👑 VIP 👑")
async def flash (ctx, member: discord.Member):
    await ctx.channel.purge(limit=1)

    frole = discord.utils.get(ctx.message.guild.roles, name='Flashed')
    emb = discord.Embed( title = 'ВНИМАНИЕ!',colour = discord.Color.gold(),url = None )
    emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url )
    emb.add_field( name ='----------------', value = '{} был ослеплен!'.format(member.mention) )
    await ctx.send(embed = emb)
    await member.add_roles( frole )
    #emb.set_author( name =  client.user.name, icon_url = client.user.avatar_url )
    #emb.set_footer( text = ctx.author.name, icon_url = ctx.author.avatar_url )
    #emb.set_thumbnail( url = '' )s

@client.command(pass_context=True)
@commands.has_role("👑 VIP 👑")
async def vanish (ctx, member: discord.Member):
    await ctx.channel.purge(limit=1)

    vrole = discord.utils.get(ctx.message.guild.roles, name='Vanished')
    emb = discord.Embed( title = 'СКРЫТИЕ',colour = discord.Color.gold(),url = None )
    emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url )
    emb.add_field( name ='----------------', value = '{} стал невидим!'.format(member.mention) )
    await ctx.send(embed = emb)
    await member.add_roles( vrole )
    #emb.set_author( name =  client.user.name, icon_url = client.user.avatar_url )
    #emb.set_footer( text = ctx.author.name, icon_url = ctx.author.avatar_url )
    #emb.set_thumbnail( url = '' )s

@client.command(pass_context=True)
@commands.has_role("👑 VIP 👑")
async def unvanish (ctx, member: discord.Member):
    await ctx.channel.purge(limit=1)

    vrole = discord.utils.get(ctx.message.guild.roles, name='Vanished')
    emb = discord.Embed( title = 'РАСКРЫТИЕ',colour = discord.Color.gold(),url = None )
    emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url )
    emb.add_field( name ='----------------', value = '{} стал видим!'.format(member.mention) )
    await ctx.send(embed = emb)
    await member.remove_roles( vrole )
    #emb.set_author( name =  client.user.name, icon_url = client.user.avatar_url )
    #emb.set_footer( text = ctx.author.name, icon_url = ctx.author.avatar_url )
    #emb.set_thumbnail( url = '' )s


@client.command()
@commands.has_role("👑 VIP 👑")

async def unflash(ctx, member: discord.Member):
    await ctx.channel.purge(limit=1) 

    frole = discord.utils.get(ctx.message.guild.roles, name = 'Flashed')
    
    #await ctx.send(f"{} снял ограничения чата у{member.mention}")
    emb = discord.Embed( title = 'ВНИМАНИЕ!',colour = discord.Color.gold(),url = None )

    emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url )
    
    emb.add_field( name ='----------------', value = '{} теперь все видит!'.format(member.mention) )
    await member.remove_roles(frole)
    await ctx.send(embed = emb)
    
    
token = os.environ.get('TOKEN')

client.run(str(token))
  
