import discord
from Mensages import handle_message
from Bot_Token import token

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}!')

@bot.event
async def on_message(message):
    await handle_message(bot, message)

bot.run(token)
