import random
from Embed_Text import ajuda_texto
from Embed_Text import ajuda_comandos
import discord
from Bot_Keys import ID_ADM
async def handle_commands(bot, message):
    content = message.content.lower()

    if content.startswith('/repete'):
        frase = message.content[8:].strip()
        await message.channel.send(frase)

    elif content.startswith('/random'):
        await message.channel.send(f'{random.randint(1, 100)}')

    elif content.startswith('/soun'):
        choices = ["Sim!", "Não!", "Talvez"]
        choice = random.choice(choices)
        await message.channel.send(choice)

    elif content.startswith('/moeda'):
        escolha = random.choice(["Cara", "Coroa"])
        await message.channel.send(f'O resultado é: {escolha}')

    elif content.startswith('/soma'):
        palavras = message.content.split()
        if len(palavras) == 3:
            try:
                num1 = int(palavras[1])
                num2 = int(palavras[2])
                soma = num1 + num2
                await message.channel.send(f'A soma de {num1} e {num2} é igual a {soma}')
            except ValueError:
                await message.channel.send('Certifique-se de fornecer dois números válidos após o comando.')
        else:
            await message.channel.send('Uso correto: /soma [número1] [número2]')

    elif content.startswith('/sub'):
        palavras = message.content.split()
        if len(palavras) == 3:
            try:
                num1 = int(palavras[1])
                num2 = int(palavras[2])
                sub = num1 - num2
                await message.channel.send(f'A subtração de {num1} e {num2} é igual a {sub}')
            except ValueError:
                await message.channel.send('Certifique-se de fornecer dois números válidos após o comando.')
        else:
            await message.channel.send('Uso correto: /sub [número1] [número2]')

    elif content.startswith('/vezes'):
        palavras = message.content.split()
        if len(palavras) == 3:
            try:
                num1 = int(palavras[1])
                num2 = int(palavras[2])
                vezes = num1 * num2
                await message.channel.send(f'A multiplicação de {num1} e {num2} é igual a {vezes}')
            except ValueError:
                await message.channel.send('Certifique-se de fornecer dois números válidos após o comando.')
        else:
            await message.channel.send('Uso correto: /vezes [número1] [número2]')

    elif content.startswith('/div'):
        palavras = message.content.split()
        if len(palavras) == 3:
            try:
                num1 = float(palavras[1])
                num2 = float(palavras[2])
                div = num1 / num2
                await message.channel.send(f'A divisão de {num1} e {num2} é igual a {div}')
            except ValueError:
                await message.channel.send('Certifique-se de fornecer dois números válidos após o comando.')
        else:
            await message.channel.send('Uso correto: /div [número1] [número2]')

    elif content.startswith('/clear'):
        if message.author.guild_permissions.administrator:
            await message.delete()
            await message.channel.purge()
            await message.channel.send("# Mensagens limpas com sucesso! :saluting_face:")
        else:
            await message.channel.send("Você não tem permissão para usar este comando.")

    elif content == '/ajuda':
        ajuda_message = """
        # Laziness Bot :sloth:
        ```
        Olá sou o Laziness Bot, o bot mais vagabundo e preguiçoso do mundo
        feito pelo Bruno Winter pois ele esta desempregado e quer aprender a programar. ```
        ## Textos Disponíveis:
        
    ``` - "oi": Cumprimenta o usuário.
        - "tudo bem?": Pergunta como o usuário está.
        - "quem é um gostoso": Diz quem é um gostoso.
        - "vem na sincera": Desafia alguém para uma briga.
        - "bot burro": O bot assume que é inútil (O que é um fato).
        - "nerdola": Mostra um emoji nerd.
        - "boa noite": Deseja boa noite ao usuário.
        - "pete": Repete a mensagem "repete".
        - "barato": Mostra gif do barato.
        - "au au": Mostra gif de cachorros. ```
        ## Comandos Disponíveis:
        ```
        - "/random": Gera um número aleatório entre 1 e 100.
        - "/soun": Responde "Sim!" ou "Não!" aleatoriamente.
        - "/repete: [mensagem]": Repete a mensagem pedida.
        - "/moeda": Para Decidir no Cara ou Coroa.
        - "/soma": Para executar a soma de 2 números.
        - "/sub": Para executar a subtração de 2 números.
        - "/vezes": Para executar a multiplicação de 2 números.
        - "/div": Para executar a divisão de 2 números.
        - "/ping": Mostra o ping atual do bot.
        - "/clear": Limpa as mensagens do canal (somente para administradores).
        - "/desligar": Desliga o Bot (Apenas pessoas autorizadas pelo criador podem usar este comando) ```
        > _Para mais informações acesse:_ [Laziness.bot/support](https://giphy.com/gifs/disneyzootopia-l2JHVUriDGEtWOx0c)
        """
        await message.channel.send(ajuda_message)

    elif content == '/desligar':
        if  message.author.id in ID_ADM:
            await message.channel.send('Desligando o Bot')
            await bot.close()
        else:
            await message.channel.send('Você não tem permissão para desligar o Bot.')

    elif content == '/ping':
        latency = bot.latency * 1000
        await message.channel.send(f'Pong: {latency:.2f}ms')

    elif content == '/help':
        embed = discord.Embed(
            title = '*Tutorial do Laziness*',
            description = 'Olá sou o Laziness Bot criado pelo Bruno Winter.' ,
            colour= 4175359
        )
        embed.add_field(name='Textos Disponíveis:', value=(ajuda_texto))
        embed.add_field(name='Comandos Disponíveis:', value=(ajuda_comandos),inline=False)
        embed.set_author(name='Laziness Bot', icon_url='https://cdn-icons-png.flaticon.com/512/3819/3819144.png')
        embed.set_thumbnail(url='https://cdn-icons-png.flaticon.com/512/7631/7631040.png')
        embed.set_footer(text='Alguns comandos so podem ser utilizado por usuários autorizados')
        await message.channel.send(embed = embed)

