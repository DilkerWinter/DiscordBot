import random

async def handle_message(bot, message):
    if message.author.id == bot.user.id:
        return

    content = message.content.lower()

    if content == 'oi':
        await message.channel.send(f'Oi, {message.author.mention}!')

    elif content == 'tudo bem?':
        await message.channel.send(f'Tudo e ctng lindo {message.author.mention}?')

    elif content == 'quem é um gostoso?':
        await message.channel.send(f'Obviamente {message.author.mention}!')

    elif content == 'vem na sincera':
        await message.channel.send(f'Vem então seu fudido, bo cair no soco :rage:')

    elif content == 'bot burro':
        await message.channel.send(f'# Sou inútil e compreendo :sob:')

    elif content == 'nerdola':
        await message.channel.send(f'# :nerd: :point_up_2:')

    elif content == 'boa noite':
        await message.channel.send(f'Boa noite {message.author.mention}!')

    elif message.content == 'barato':
        escolha = random.choice([
            'https://media.tenor.com/eBeeVvRmguwAAAAC/dancing-cockroach.gif',
            'https://media.tenor.com/ABkotNXYWwcAAAAC/cockroach-dancing.gif',
        ])
        await message.channel.send(f':cockroach: [O Barato]({escolha}) :cockroach:')

    elif message.content == 'au au':
        escolha = random.choice([
            'https://media.tenor.com/plWuEbyFX2gAAAAd/dog-theoretical.gif',
            'https://media.tenor.com/dqH6ZBgOvMUAAAAi/dog-dance.gif',
            'https://media.tenor.com/Qw1v0F2MN3sAAAAd/dog-dogs.gif',
            'https://media.tenor.com/enzZ8AfPV2gAAAAC/screaming-scream.gif',
            'https://media.tenor.com/1Y4tqPWQkQMAAAAd/pat-patting.gif',
            'https://media.tenor.com/eTx10HL_01cAAAAC/dog-side-eye.gif',
            'https://media.tenor.com/f8gixYnl5dMAAAAC/excited-dogs.gif'
        ])
        await message.channel.send(f':dog: [Au Au]({escolha}) :dog:')

    elif content == 'pete':
        await message.channel.send(f'repete')

