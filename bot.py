import discord

TOKEN = "."
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

cocotime = False
cococount = 0

@client.event
async def on_ready():
    print('bot is ready')

@client.event
async def on_message(msg):
    global cocotime, cococount
    
    if msg.author == client.user:
        return
    
    if msg.content == "/coco":
        await msg.channel.send(':coconut:')
    
    if msg.content == "/cocotime":
        #pretty message goes here
        await msg.channel.send("cocotime! let's start a chain of :coconut: !")
        cocotime = True
        #if message not coco
            #get cococount and check for record
        #else
            #cococount++
    
    if cocotime:
        if msg.author == client.user:
            pass

        if msg.content != ":coconut:" and msg.author != client.user:
            await msg.channel.send(f"YOU BLEW IT!!!! max record is {cococount}")
            print(cococount)
            cococount = 0
            return
        
        cococount += 1

client.run(TOKEN)