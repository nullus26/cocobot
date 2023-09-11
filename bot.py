import discord

TOKEN = "MTE1MDA4NjUwNTQ4MjY4NjUzNQ.GGRnv4.DrkOv8c97zqqvP9LbTq-MycOU3LwI3DHjorNKY"
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('bot is ready')

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    
    if msg.content == "/coco":
        await msg.channel.send(':coconut:')
    
    #if cocotime
        #if message not coco
            #get cococount and check for record
        #else
            #cococount++

client.run(TOKEN)