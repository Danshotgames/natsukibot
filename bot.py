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

global sex_v 
sex_v = False

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

@client.command()
async def kill(  ctx, member: discord.Member ):
    await ctx.send( f"{ctx.author.mention} Достает дробовик... \n https://tenor.com/view/eyebrow-raise-smile-prepared-ready-loaded-gif-15793001" )
    await asyncio.sleep( 3 )
    await ctx.send( f"{ctx.author.mention} Направляет дробовик на {member.mention}... \n https://tenor.com/view/aim-point-gun-prepared-locked-and-loaded-gif-15793489" )
    await asyncio.sleep( 2 )
    await ctx.send( f"{ctx.author.mention} Стреляет в {member.mention}... \n https://media.discordapp.net/attachments/690222948283580435/701494203607416943/tenor_3.gif" )
    await asyncio.sleep( 2 )
    await ctx.send( f"{member.mention} истекает кровью..." )
    await asyncio.sleep( 3 )
    await ctx.send( f"{member.mention} погиб..." )

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

@client.command()
async def emoji(ctx, arg):
    await ctx.message.delete()
    guild = ctx.guild
    em = str(discord.utils.get(guild.emojis, name=f'{arg}'))
    await ctx.send(f'{em}')

@client.command()
async def e(ctx, arg):
    await ctx.message.delete()
    guild = ctx.guild
    em = str(discord.utils.get(guild.emojis, name=f'{arg}'))
    await ctx.send(f'{em}')

@emoji.error
async def emoji_error( ctx, error ):
  if isinstance( error, commands.MissingRequiredArgument ):
    await ctx.author.send(embed = discord.Embed(description = f'{ ctx.author.mention }, Вы забыли указать эмодзик!' ))

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
    await member.send(f'Приветствую тебя, я Natsuki, мой создатель - _Rayyy. Мы поздравляем тебя, {member.mention}! теперь ты часть нашего клана AFFERs! Добро пожаловать! Введи //help для помощи')
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
    emb.add_field( name ='//serverinfo', value = 'Информация о сервере')
    emb.add_field( name ='//userinfo', value = 'Информация об участнике')
    emb.add_field( name ='//suggest', value = 'Предложить идею')
    emb.add_field( name ='//tempmute', value = 'Ограничить чат участника на время')
    emb.add_field( name ='//avatar', value = 'Посмотреть аватарку')
    emb.add_field( name ='//math', value = 'Калькулятор')
    emb.add_field( name ='//emoji', value = 'Отправить gif-emoji из сервера')
    emb.add_field( name ='//ball', value = 'Магический шар')
    emb.add_field( name ='//say', value = 'Говорить ботом')
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

#Ava

@client.command()
async def avatar(ctx, member : discord.Member = None):
    await ctx.channel.purge (limit = 1)

    user = ctx.message.author if (member == None) else member

    embed = discord.Embed(title=f'Аватар пользователя {user}', colour = discord.Color.purple())

    embed.set_image(url=user.avatar_url)

    await ctx.send(embed=embed)

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

#Ban

@client.command( pass_context = True )
@commands.has_permissions( ban_members = True )

async def softban( ctx, member: discord.Member, *, reason = None):
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


#Tempmute

@client.command()
@commands.has_permissions( kick_members = True )
async def tempmute(ctx,amount : int,member: discord.Member = None, reason = None):
    await ctx.channel.purge (limit = 1)
    mute_role = discord.utils.get(member.guild.roles, id = 698457341019816016) #Айди роли
    channel_log = client.get_channel(703223484574334976) #Айди канала логов

    await member.add_roles( mute_role )
    await ctx.send(embed = discord.Embed(description = f'**Пользователю {member.mention} был ограничен доступ к чатам на {amount} секунд. По причине: {reason}**', colour = discord.Color.red())) 
    await channel_log.send(embed = discord.Embed(description = f'**Пользователю {member.mention} был ограничен доступ к чатам на {amount} секунд. По причине: {reason}**', colour = discord.Color.red()))
    await asyncio.sleep(amount)
    await ctx.send(embed = discord.Embed(description = f'**Пользователю {member.mention} сняли ограничения чата.**', colour = discord.Color.purple())) 
    await member.remove_roles( mute_role )   

@tempmute.error 
async def tempmute_error(ctx, error):

    if isinstance( error, commands.MissingPermissions ):
        await ctx.send(embed = discord.Embed(description = f'** {ctx.author.name}, у вас нет прав для использования данной команды.**', colour = discord.Color.red()))

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

# Работа с ошибками шара

@ball.error 
async def ball_error(ctx, error):

    if isinstance( error, commands.MissingRequiredArgument ): 
        await ctx.send(embed = discord.Embed(description = f'Пожалуйста, укажите сообщение.', colour = discord.Color.red()))

@client.command()
async def math(ctx, *, args = None):
    await ctx.channel.purge (limit = 1)
    text = ctx.message.content

    if args == None:
        await ctx.send(embed = discord.Embed(description = 'Пожалуйста, укажите выражение', colour = discord.Color.red()))
    else:
        result = eval(args)
        await ctx.send(embed = discord.Embed(description = f'Вычислить `{args}` = \n`{result}`', colour = discord.Color.purple()))


@client.command( pass_context = True)

async def suggest( ctx , * , agr ):
    await ctx.channel.purge (limit = 1)
    suggest_chanell = client.get_channel( 698168631758028840 ) #Айди канала предложки
    embed = discord.Embed(title=f"{ctx.author.name} Предложил :", description= f" {agr} \n\n")

    embed.set_thumbnail(url=ctx.guild.icon_url)

    message = await suggest_chanell.send(embed=embed)
    await message.add_reaction('✅')
    await message.add_reaction('❎')


@commands.command()
#@commands.bot_has_permissions(manage_webhooks=True)
async def mebot(self, ctx, *, msg: commands.clean_content):
    await ctx.message.delete()
    w = await ctx.channel.create_webhook(name=ctx.author.name)
    await w.send(msg, avatar_url=ctx.author.avatar_url)
        
    await w.delete()

@client.command( pass_context = True )
@commands.has_permissions( ban_members = True )

async def test( ctx ):
    emb = discord.Embed( title = 'иди нахуй', description = 'даун',colour = discord.Color.purple(),url = None )

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
  
