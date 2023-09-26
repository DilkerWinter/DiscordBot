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

    elif content == 'pete':
        await message.channel.send(f'repete')

    elif message.content.startswith('/repete'):
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

    elif message.content.startswith('/soma'):

        palavras = message.content.split()

        if len(palavras) == 3:
            try:
                num1 = int(palavras[1])
                num2 = int(palavras[2])

                soma = num1 + num2

                #await message.channel.send(f'A soma de {num1} e {num2} é igual a {soma}')
                await message.channel.send(f'{num1} + {num2} = {soma}')
            except ValueError:
                await message.channel.send('Certifique-se de fornecer dois números válidos após o comando.')
        else:
            await message.channel.send('Uso correto: /soma [número1] [número2]')

    elif message.content.startswith('/sub'):

        palavras = message.content.split()

        if len(palavras) == 3:
            try:
                num1 = int(palavras[1])
                num2 = int(palavras[2])

                sub = num1 - num2

                # await message.channel.send(f'A subtração de {num1} e {num2} é igual a {sub}')
                await message.channel.send(f'{num1} + {num2} = {sub}')
            except ValueError:
                await message.channel.send('Certifique-se de fornecer dois números válidos após o comando.')
        else:
            await message.channel.send('Uso correto: /sub [número1] [número2]')

    elif message.content.startswith('/vezes'):

        palavras = message.content.split()

        if len(palavras) == 3:
            try:
                num1 = int(palavras[1])
                num2 = int(palavras[2])

                vezes = num1 * num2

                # await message.channel.send(f'A multiplicação de {num1} e {num2} é igual a {vezes}')
                await message.channel.send(f'{num1} * {num2} = {vezes}')
            except ValueError:
                await message.channel.send('Certifique-se de fornecer dois números válidos após o comando.')
        else:
            await message.channel.send('Uso correto: /vezes [número1] [número2]')

    elif message.content.startswith('/div'):

        palavras = message.content.split()

        if len(palavras) == 3:
            try:
                num1 = float(palavras[1])
                num2 = float(palavras[2])

                div = num1 / num2

                # await message.channel.send(f'A divisão de {num1} e {num2} é igual a {div}')
                await message.channel.send(f'{num1} / {num2} = {div}')
            except ValueError:
                await message.channel.send('Certifique-se de fornecer dois números válidos após o comando.')
        else:
            await message.channel.send('Uso correto: /div [número1] [número2]')
    elif content.startswith('/clear'):
        if message.author.guild_permissions.administrator:
            await message.delete()
            await message.channel.purge()
            await message.channel.send("# Mensagens limpas com sucesso!  :saluting_face:")
        else:
            await message.channel.send("Você não tem permissão para usar este comando.")

    elif content == '/ajuda':
        ajuda_message = """
        # Laziness Bot :sloth: 
        ```
        Olá sou o Laziness Bot, o bot mais vagabundo e preguiçoso do mundo
        feito pelo Bruno Winter pois ele esta desempregado e quer aprender a programar. ```       
        ## Textos Disponíveis: 
        ```
        - "oi": Cumprimenta o usuário.
        - "tudo bem?": Pergunta como o usuário está.
        - "quem é um gostoso": Diz quem é um gostoso.
        - "vem na sincera": Desafia alguém para uma briga.
        - "bot burro": O bot assume que é inútil (O que é um fato).
        - "nerdola": Mostra um emoji nerd.
        - "boa noite": Deseja boa noite ao usuário.
        - "pete": Repete a mensagem "repete". 
        - "barato": Mostra o gif da barata. ```       
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
        - "/clear": Limpa as mensagens do canal (somente para administradores). ```
        > _Para mais informações acesse:_ [Laziness.bot/support](https://giphy.com/gifs/disneyzootopia-l2JHVUriDGEtWOx0c)
        """
        await message.channel.send(ajuda_message)

