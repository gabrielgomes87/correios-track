import requests
import discord
import random
import asyncio
from discord.ext import commands
from bs4 import BeautifulSoup
from discord.ext.commands import Bot
from discord.ext import commands



intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix="!c", intents=intents)

@client.event
async def on_ready():
    print("==BOT ONLINE==")
    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)
    activity = discord.Game(name="Temos nosso própio tempo >.<", type=3)
    await client.change_presence(status=discord.Status.idle, activity=activity)



@client.tree.command(name="ver")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"ver1.1")

@client.event
async def get_status(codigo):
        try:
            global resposta
            global texto
            req = requests.post(url= f"https://www.linkcorreios.com.br/?id={codigo}", headers={'Content-Type': 'text/html; charset=utf-8'})
            soup = BeautifulSoup(req.text,'html.parser')
            texto = soup.find('ul', {'class': 'linha_status m-0'}).text.replace("Local" , "**:round_pushpin: Local**").replace('Data  :', ':calendar_spiral: **Data:**').replace('Origem', ':airplane_departure: **Origem**').replace('Destino', ':airplane_arriving: **Destino**').replace('Data :', ':calendar_spiral: **Data:**').replace('Status', ':page_with_curl: **Status**').replace('Objeto entregue ao destinatário', 'Objeto entregue ao destinatário :white_check_mark:').replace('| Hora:', ':clock1: **Hora:**').replace('Objeto em trânsito - por favor aguarde', 'Objeto em trânsito  :truck:  por favor aguarde').replace('Objeto saiu para entrega ao destinatário', 'Objeto saiu para entrega ao destinatário :outbox_tray: ')
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
        


client.run("TOKEN AQUI")
