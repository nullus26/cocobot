import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)
TOKEN = "MTE1MDA4NjUwNTQ4MjY4NjUzNQ.Ght3z4.2n1KLvX4BNeqUj5xcr9o-LSWVjgsFt6ujYEs8E"

emoji = "\U0001F965"

cocotime = False
cococount = 0
record = 0

def read_record():
     try:
          with open('record.txt', 'r') as file:
               return int(file.read())
     except FileNotFoundError:
          return 0
     
def update_record(count):
     current = read_record()
     if count > current:
          with open('record.txt', 'w') as file:
               file.write(str(count))
               print('record actualizado')
          return True
     return False


@bot.event
async def on_ready():
        print("bot is up and running")
        try:
            synced = await bot.tree.sync()
            print(f"synced {len(synced)} command(s)")
        except Exception as e:
             print(e) 


@bot.tree.command(name="coco")
async def say(interaction: discord.Interaction):
      await interaction.response.send_message(emoji)


@bot.tree.command(name="cocotime")
async def cococadena(interaction: discord.Interaction):
     global cocotime, cococount

     if cocotime:
          await interaction.response.send_message("Cocotime ya empezó, cabeza de coco!!")
     else:
          await interaction.response.send_message("Cocotime! Intentemos hacer la cadena de cocos mas larga del server!")
          await interaction.followup.send(emoji)
          cocotime = True
          cococount = 1


@bot.event
async def on_message(message):

    global cocotime, cococount
    
    if message.author == bot.user:
        return
    

    if cocotime and message.content == emoji:
         cococount +=1
    elif cocotime:
         await message.channel.send(f"Cocotime se terminó! llegamos a {cococount}. Pero hubiera sido mucho mas si no hubiera sido por {message.author.mention}")
         
         #sistema de record
         if update_record(cococount):
              await message.channel.send(f"...Pero llegamos a un nuevo record de {cococount}!")
         cocotime = False
         cococount = 0

    await bot.process_commands(message)
        

        

    await bot.process_commands(message)
bot.run(TOKEN)