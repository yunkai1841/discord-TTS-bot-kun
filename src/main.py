import discord

import status
import command
import settings

client = discord.Client()

tokens = settings.get_token(True)

@client.event
async def on_ready():
    status.set_ready(True)
    print(client.user, "login")

@client.event
async def on_message(msg: discord.Message):
    
    if msg.author.bot:
        return
    
    if msg.content.startswith(status.prefix):
        # if msg starts with prefix
        await command.run(msg)

client.run(tokens["discord"])