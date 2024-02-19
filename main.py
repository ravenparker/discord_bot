import discord
from discord.ext import commands
from discord import Interaction
import os

client = commands.Bot(command_prefix="!", intents= discord.Intents.all())

@client.event
async def on_ready():
    print(f'{client.user.name} is now online')

client.run("MTIwOTI0MTg4OTcxNTI1NzM5NA.Gdm0pe.qQWI9d6wvFu3mxwqhnui_qS1MMZAP_N8HZr4jA")