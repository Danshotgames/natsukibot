import discord
from discord.ext import commands, tasks
import asyncio
import random
import os
import datetime
import json	

client = discord.Client()

client = commands.Bot( command_prefix = '//' )

amounts = {}

@client.event
async def on_ready():
    client.loop.create_task(rainbowrole(rainbowrolename))
    client.loop.create_task(rainbowrole2(rainbowrolename))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('Ready.')
    print('------------')
    print( 'bot connected' )
    await client.change_presence( status = discord.Status.online, activity = discord.Game(' //info'))
    global amounts
    global work
try:
    with open('amounts.json') as f:
        amounts = json.load(f)
    with open('work.json') as f:
        work = json.load(f)
except FileNotFoundError:
    print("Could not load amounts.json")
    amounts = {}
    work = {}


@client.command(pass_context=True)
async def balance(ctx):
    await ctx.channel.purge(limit=1)
    id = ctx.message.author.id
    if id in amounts:
        #await ctx.send("У тебя {} монет в банке".format(amounts[id]))
        emb = discord.Embed( title = 'Баланс',colour = discord.Color.purple(),url = None )
        emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url )
        emb.add_field( name ='--------', value = 'У тебя {}$ в банке'.format(amounts[id]) )
        await ctx.send(embed = emb)
    else:
        #await ctx.send("Ты не имеешь аккаунта! Зарегестрируйся c помощью комманды //register")
        emb = discord.Embed( title = 'Аккаунт',colour = discord.Color.red(),url = None )
        emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url )
        emb.add_field( name ='-----------', value = 'Ты не имеешь аккаунта! Зарегестрируйся c помощью комманды //register' )
        await ctx.send(embed = emb)

@client.command(pass_context=True)
async def register(ctx):
    await ctx.channel.purge(limit=1)
    id = ctx.message.author.id
    if id in amounts:
        #await ctx.send("Ты уже имеешь аккаунт!")
        emb = discord.Embed( title = 'Аккаунт',colour = discord.Color.red(),url = None )
        emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url )
        emb.add_field( name ='-----------', value = 'Ты уже имеешь аккаунт!' )
        await ctx.send(embed = emb)
    if id not in amounts:
        amounts[id] = 100
        #await ctx.send("Ты успешно зарегестрирован!")
        emb = discord.Embed( title = 'Аккаунт',colour = discord.Color.purple(),url = None )
        emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url )
        emb.add_field( name ='------------', value = 'Ты успешно зарегестрирован!' )
        await ctx.send(embed = emb)
        _save()


@client.command(pass_context=True)
async def transfer(ctx, amount: int, other: discord.Member):
    await ctx.channel.purge(limit=1)
    primary_id = ctx.message.author.id
    other_id = other.id
    if primary_id not in amounts:
        #await ctx.send("Ты не имеешь аккаунта! Зарегестрируйся c помощью комманды //register")
        emb = discord.Embed( title = 'Аккаунт',colour = discord.Color.red(),url = None )
        emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url )
        emb.add_field( name ='-----------', value = 'Ты не имеешь аккаунта! Зарегестрируйся c помощью комманды //register' )
        await ctx.send(embed = emb)
    elif other_id not in amounts:
        #await ctx.send("Данный пользователь не имеет аккаунта")
        emb = discord.Embed( title = 'Аккаунт',colour = discord.Color.red(),url = None )
        emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url )
        emb.add_field( name ='-----------', value = 'Пользователь {} не имеет аккаунта'.format(other.mention) )
        await ctx.send(embed = emb)
    elif amounts[primary_id] < amount:
        #await ctx.send("Недостаточно средств")
        emb = discord.Embed( title = 'Баланс',colour = discord.Color.red(),url = None )
        emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url )
        emb.add_field( name ='--------', value = 'Недостаточно средств!' )
        await ctx.send(embed = emb)
    else:
        amounts[primary_id] -= amount
        amounts[other_id] += amount
        #await ctx.send("Успешный перевод!")
        emb = discord.Embed( title = 'Баланс',colour = discord.Color.purple(),url = None )
        emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url )
        emb.add_field( name ='--------', value = 'Успешный перевод {}!'.format(other.mention) )
        await ctx.send(embed = emb)
        await other.send(f'{other.mention}, Вам перечислены {amount} монет!')
    _save()

@commands.has_permissions( ban_members = True )
@client.command(pass_context=True)
async def give(ctx, amount: int, other: discord.Member):
    await ctx.channel.purge(limit=1)
    primary_id = ctx.message.author.id
    other_id = other.id
    if primary_id not in amounts:
        #await ctx.send("Ты не имеешь аккаунта! Зарегестрируйся c помощью комманды //register")
        emb = discord.Embed( title = 'Аккаунт',colour = discord.Color.red(),url = None )
        emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url )
        emb.add_field( name ='-----------', value = 'Ты не имеешь аккаунта! Зарегестрируйся c помощью комманды //register' )
        await ctx.send(embed = emb)
    elif other_id not in amounts:
        #await ctx.send("Данный пользователь не имеет аккаунта")
        emb = discord.Embed( title = 'Аккаунт',colour = discord.Color.red(),url = None )
        emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url )
        emb.add_field( name ='-----------', value = 'Пользователь {} не имеет аккаунта'.format(other.mention) )
        await ctx.send(embed = emb)
    else:
        amounts[other_id] += amount
        #await ctx.send("Успешный перевод!")
        emb = discord.Embed( title = 'Баланс',colour = discord.Color.purple(),url = None )
        emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url )
        emb.add_field( name ='--------', value = 'Успешное зачисление {}!'.format(other.mention) )
        await ctx.send(embed = emb)
        await other.send(f'{other.mention}, Вам зачислены {amount} монет!')
    _save()

def _save():
    with open('amounts.json', 'w+') as f:
        json.dump(amounts, f)

def _save_work():
    with open('work.json', 'w+') as f:
        json.dump(work, f)

@client.command(pass_context=True)
async def work_filter(ctx):
    await ctx.channel.purge(limit=1)
    id = ctx.message.author.id
    if id in work:
        if id in amounts:
            #await ctx.send("Ты уже имеешь аккаунт!")
            emb = discord.Embed( title = 'Работа',colour = discord.Color.red(),url = None )
            emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url )
            emb.add_field( name ='-----------', value = 'Ты уже работаешь!' )
            await ctx.send(embed = emb)
    if id not in work:
        if id in amounts:
            work[id] = 1
            #await ctx.send("Ты успешно зарегестрирован!")
            emb = discord.Embed( title = 'Работа',colour = discord.Color.purple(),url = None )
            emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url )
            emb.add_field( name ='------------', value = 'Ты успешно устроился на работу!' )
            await ctx.send(embed = emb)
            _save_work()


@client.command()
async def save():
    _save()

@client.command()
async def save_work():
    _save()


#Variables

serverid = 625001454666776586
rainbowrolename = "АДМИН"
delay = 1
link = 'https://youtu.be/81MglUZp5-I'
serverid2 = 698843967403327530


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

#Rainbow

colours = [discord.Color.dark_orange(),discord.Color.orange(),discord.Color.dark_gold(),discord.Color.gold(),discord.Color.dark_magenta(),discord.Color.magenta(),discord.Color.red(),discord.Color.dark_red(),discord.Color.blue(),discord.Color.dark_blue(),discord.Color.teal(),discord.Color.dark_teal(),discord.Color.green(),discord.Color.dark_green(),discord.Color.purple(),discord.Color.dark_purple()]

async def rainbowrole(role):
    for role in client.get_guild(serverid).roles:
        if str(role) == str(rainbowrolename):
            print("detected role")
            while not client.is_closed():
                try:
                    await role.edit(color=random.choice(colours))
                except Exception:
                    print("can't edit role, make sure the bot role is above the rainbow role and that is have the perms to edit roles")
                    pass
                await asyncio.sleep(delay)
    print('role with the name "' + rainbowrolename +'" not found')
    print("creating the role...")
    try:
        await client.get_guild(serverid).create_role(reason="Created rainbow role", name=rainbowrolename)
        print("role created!")
        await asyncio.sleep(2)
        client.loop.create_task(rainbowrole(rainbowrolename))
    except Exception as e:
        print("couldn't create the role. Make sure the bot have the perms to edit roles")
        print(e)
        pass
        await asyncio.sleep(10)
        client.loop.create_task(rainbowrole(rainbowrolename))

async def rainbowrole2(role):
    for role in client.get_guild(serverid2).roles:
        if str(role) == str(rainbowrolename):
            print("detected role")
            while not client.is_closed():
                try:
                    await role.edit(color=random.choice(colours))
                except Exception:
                    print("can't edit role, make sure the bot role is above the rainbow role and that is have the perms to edit roles")
                    pass
                await asyncio.sleep(delay)
    print('role with the name "' + rainbowrolename +'" not found')
    print("creating the role...")
    try:
        await client.get_guild(serverid2).create_role(reason="Created rainbow role", name=rainbowrolename)
        print("role created!")
        await asyncio.sleep(2)
        client.loop.create_task(rainbowrole2(rainbowrolename))
    except Exception as e:
        print("couldn't create the role. Make sure the bot have the perms to edit roles")
        print(e)
        pass
        await asyncio.sleep(10)
        client.loop.create_task(rainbowrole2(rainbowrolename))


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

#offkick

@client.command( pass_context = True )
@commands.has_permissions( kick_members = True )

async def warn_off( ctx, member: discord.Member):
    await ctx.channel.purge (limit = 1)
    
    await member.send(f'{member.mention}, Предупреждение! Вы не были онлайн 3 дня! 3 таких предупреждения - автоматический кик!')

@client.command( pass_context = True )
@commands.has_permissions( kick_members = True )

async def warn_kick( ctx, member: discord.Member, reason):
    await ctx.channel.purge (limit = 1)
    
    await member.send(f'{member.mention}, Вы были выгнаны из сервера по причине большого не актива!')
    await member.kick( reason = reason )

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

#links
@client.command()
@client.event
async def new( ctx):
    
    await ctx.channel.purge (limit = 1)
    
    emb = discord.Embed( title = 'РАССЫЛКА!',colour = discord.Color.purple(),url = None )

    emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url )
    
    emb.add_field( name ='---------------', value = '@everyone У Ская вышло новое видео!!! Бегом смотреть! Ссылка: https://youtu.be/81MglUZp5-I' )

    await ctx.send(embed = emb)

#Clear
    
@client.command( pass_context = True )
@commands.has_permissions( kick_members = True )

async def clear( ctx, amount = 1000 ):
    await ctx.channel.purge(limit = amount+1)

    emb = discord.Embed( title = 'УДАЛЕНИЕ', description = f'Удалено: {amount} сообщений',colour = discord.Color.purple(),url = None )
    await ctx.send(embed = emb)
    
#Help
    
@client.command( pass_context = True )

async def info( ctx ):
    await ctx.channel.purge (limit = 1)

    emb = discord.Embed( title = 'ИНФОРМАЦИЯ', description = 'ГИД по коммандам:',colour = discord.Color.purple(),url = None )

    emb.add_field( name ='//info', value = 'Инструкция по коммандам' )
    emb.add_field( name ='//clear', value = 'Очистка чата')
    emb.add_field( name ='//kick', value = 'Выгнать участника')
    emb.add_field( name ='//ban', value = 'Заблокировать участника')
    emb.add_field( name ='//mute', value = 'Ограничить чат участника')
    emb.add_field( name ='//unmute', value = 'Убрать ограничения чата участника')
    emb.add_field( name ='//time', value = 'Посмотреть текущее время')
    emb.add_field( name ='//register', value = 'Зарегистрировать счет в банке')
    emb.add_field( name ='//balance', value = 'Посмотреть свой баланс')
    emb.add_field( name ='//transfer', value = 'Перекинуть деньги')
    emb.add_field( name ='@Natsuki_bot', value = 'by @Rayyy, ver 1.7')
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

token = os.environ.get('TOKEN')

client.run(str(token))
  
