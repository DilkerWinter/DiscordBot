import discord
from discord.ext import commands
from Mensages import handle_message
from Comands import handle_commands
from Bot_Token import token

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    print(f'O usuario: {message.author} chamou o bot')
    await handle_message(bot, message)
    await handle_commands(bot, message)

bot.run(token)
