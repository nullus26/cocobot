import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)
TOKEN = "MTE1MDA4NjUwNTQ4MjY4NjUzNQ.G4cfn-.arsDxVeW4B_tRydiz8AvBBXL9l3Y9MINL9GlJk"

emoji = "\U0001F965"

cocotime = False
cococount = 0
record = 3

@bot.event
async def on_ready():
        print("bot is up and running")
        try:
            synced = await bot.tree.sync()
            print(f"synced {len(synced)} command(s)")
        except Exception as e:
             print(e) 

@bot.tree.command(name="hello")
async def hello(interaction: discord.Interaction):
      await interaction.response.send_message(f"hello {interaction.user.mention}, this is a slash command :))", ephemeral=True)

@bot.tree.command(name="say")
@app_commands.describe(arg = "What should i say?")
async def say(interaction: discord.Interaction, arg: str):
      await interaction.response.send_message(f"{interaction.user.name} said:`{arg}`")


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
         await message.channel.send(f"Cocotime se terminó! llegamos a {cococount}. NT muchachos... NT...")
         
         #sistema de record
         if cococount > record:
              await message.channel.send(f"...Pero llegamos a un nuevo record de {cococount}!")
         cocotime = False
         cococount = 0

    await bot.process_commands(message)
        

        

    await bot.process_commands(message)
bot.run(TOKEN)