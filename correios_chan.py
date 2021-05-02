import requests
import discord
import random
import asyncio
from discord.ext import commands
from bs4 import BeautifulSoup
from discord.ext.commands import Bot
from discord.ext import commands

client = discord.Client()

@client.event
async def on_ready():
    print("==BOT ONLINE==")
    activity = discord.Game(name="Temos nosso própio tempo >.<", type=3)
    await client.change_presence(status=discord.Status.idle, activity=activity)


@client.event
async def get_status(codigo):
        try:
            global resposta
            global texto
            req = requests.post(url= f"https://www.linkcorreios.com.br/?id={codigo}")
            soup = BeautifulSoup(req.text,'html.parser')
            texto = soup.find('ul', {'class': 'linha_status m-0'}).text.replace('trÃ¢nsito', "trânsito").replace('LogÃ­stica', 'Logística').replace('  ', ' ').replace('destinatÃ¡rio', 'destinatário').replace('DistribuiÃ§Ã£o', '**Distribuição**').replace("exportaÃ§Ã£o", "exportação").replace("paÃ­s", "país").replace("PaÃ­s", 'País').replace("Local" , "**:round_pushpin: Local**").replace('Origem', ':airplane_departure: **Origem**').replace('Destino', ':airplane_arriving: **Destino**').replace('Data', ':clock1: **Data**').replace('Status', ':page_with_curl: **Status**')
            resposta = f' {texto}'
            await channel.send(" **:package: Pacote encontrado:** " + resposta)
            print(resposta) 
        except Exception as e:
            await channel.send(" :x: **Pacote não encontrado, certifique de que o código esteja correto. (Compras internacionais podem demorar para serem registradas).**")
        

@client.event
async def on_message(message):
    global channel
    if message.author == client.user:
        return
    if message.content.startswith('!c'):
        channel = message.channel
        await channel.send(' :mag: **Procurando o seu pacote... >.<**')    
    if message.content.startswith('!c'):
        codigo = message.content.replace("!c ", "")
        await get_status(codigo)

client.run('DISCORD API KEY AQUI')