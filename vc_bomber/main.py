from discord.ext import commands

def vc_bomber():

    tokens = open('tokens.txt'.strip()).readlines()
    channel_id = input(f'VCID > ')
    amount = 1

    with open('start.bat', 'w') as startall:
        startall.write(f'cd zombies\n')

    for token in tokens:
        content = f'''
from discord.ext import commands

selfbot = commands.Bot(command_prefix='>>', help_command=None, self_bot=True)
selfbot.remove_command('help')

@selfbot.event
async def on_ready():            
    channel = selfbot.get_channel(int({channel_id}))
    if channel is None:
        print(f'Channel not found')
    
    else:
        await channel.connect()

selfbot.run('{token.strip()}')
'''
        with open(f'zombies/client{amount}.py', 'w') as client:
            client.write(content)

        with open('start.bat', 'a') as startall:
            startall.write(f'start python client{amount}.py\n')

        with open('kill.bat', 'w') as killall:
            killall.write('taskkill /im python.exe')

        amount+=1


    
vc_bomber()