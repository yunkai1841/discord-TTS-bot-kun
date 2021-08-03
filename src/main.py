import discord

from status import Status
from command import Command

client = discord.Client()
status = Status()
command = Command()

@client.event
async def on_ready():
    status.set_ready(True)
    print(client.user, "login")

@client.event
async def on_message(msg):
    
    if msg.author.bot:
        return
    
    if msg.content.startswith(status.prefix):
        # if msg has prefix
        command.run(msg)