import discord
import time

TOKEN = 'NTk5NjA4NTU4OTY2ODAwMzk1.XSnrWA.OOFKXJFGYrwu-x0BHgcM8Kv3DqI'

#https://discordapp.com/oauth2/authorize?client_id=599608558966800395&scope=bot&permissions=8

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!owner'):
        msg = 'Zen Hap for Earth'
        await client.send_message(message.channel, msg)
    if message.content.startswith('!cleanup'):
        if message.author.id == '375338480521445396':
            userid = message.content.split(' ', 1)[1]
            print (userid)

            count = 1
            
            async for m in client.logs_from(message.channel, limit=500):
                if (str('<@' + str(m.author.id)+'>') == str(userid)):
                    print ('match')
                    await client.delete_message(m)

            time.sleep(5)
            
            async for m in client.logs_from(message.channel, limit=count):
                if m.author == client.user:
                    await client.delete_message(m)
                    time.sleep(0.2)
            print("action completed")
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
