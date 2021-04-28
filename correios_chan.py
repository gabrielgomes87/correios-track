import requests
import discord
import random
import asyncio
from discord.ext import commands
from bs4 import BeautifulSoup
from discord.ext.commands import Bot
from discord.ext import commands



prefix = "$"
bot = commands.Bot(command_prefix=prefix)


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
            req = requests.post(url="https://www2.correios.com.br/sistemas/rastreamento/ctrl/ctrlRastreamento.cfm?", data={"objetos" : codigo})
            soup = BeautifulSoup(req.text,'html.parser')
            texto = soup.find(id='UltimoEvento').strong.text
            data = soup.find(id='UltimoEvento').text.split()[-1]
            resposta = f' :ballot_box_with_check:  **{texto}** - Data - **{data}** Código n°: **{codigo}**'
            print(resposta) 
            channel = client.get_channel(ID DO CANAL)
            await channel.send(resposta)
        except Exception as e:
            channel = client.get_channel(ID DO CANAL)
            await channel.send(" :x: **Pacote não encontrado, certifique de que o código esteja correto. (Compras internacionais podem demorar para serem registradas).**")






@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!c'):
        channel = message.channel
        await channel.send(' :mag: **Procurando o seu pacote... >.<**')    
    if message.content.startswith('!c'):
        codigo = message.content.replace("!c ", "")
        await get_status(codigo)









client.run('APIKEY')