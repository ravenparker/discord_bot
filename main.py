import discord
from discord.ext import commands
from discord import Interaction
import os

client = commands.Bot(command_prefix="!", intents= discord.Intents.all())

@client.event
async def on_ready():
    await client.wait_until_ready()
    await client.change_presence(activity=discord.activity.Game(name="with Python"), 
                                status=discord.Status.idle)
    print(f'{client.user.name} is now online')

@client.command(name = "hello", description = "Say hi!")
async def hello(ctx):
    await ctx.send("hey there!")


@client.command(name = "ping", description = "Latency check")
async def ping(ctx):
    bot_latency = round(client.latency*1000)
    await ctx.send(f"Pong! {bot_latency}ms")

client.run('MTIwOTI0MTg4OTcxNTI1NzM5NA.GHXewE.ms3dx9UaF7s7PJb6Qj-STs_yCt2qBB6u17M0-o')