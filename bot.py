import discord
from discord.ext import commands

TOKEN = "."
intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='/', intents=intents)


@client.event
async def on_ready():
    print('bot is ready')

@client.event
async def on_message(message):
    print(message.author, message.content, message.channel.id)

@client.command()
async def hello(ctx):
    await client.send_message("hello")


client.run(TOKEN)