import discord
import serial
import time
from discord.ext import commands

# Configuração da porta serial para o Arduino (verifique a porta correta do seu Arduino)
ser = serial.Serial('COM3', 9600)  # Substitua 'COM3' pelo caminho da sua porta (ex: '/dev/ttyACM0' no Linux)

# Habilitando intents e criando o bot com o prefixo de comando
intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="$", intents=intents)

# Evento disparado quando o bot se conecta
@client.event
async def on_ready():
    print(f"Bot conectado como {client.user}")

# Comando para ligar o LED
@client.command()
async def led_on(ctx):
    ser.write(b'1')  # Envia '1' para o Arduino
    await ctx.send("LED ligado!")

# Comando para desligar o LED
@client.command()
async def led_off(ctx):
    ser.write(b'0')  # Envia '0' para o Arduino
    await ctx.send("LED desligado!")

# Rodando o bot
client.run("SEU_TOKEN_DO_BOT_DISCORD")
