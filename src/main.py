import discord
import json

import status
from command import Command

client = discord.Client()
command = Command(status)

setting = json.load(open("setting\\token.json", "r"))
print(setting["discord"])

@client.event
async def on_ready():
    status.set_ready(True)
    print(client.user, "login")

@client.event
async def on_message(msg: discord.Message):
    
    if msg.author.bot:
        return
    
    if msg.content.startswith(status.prefix):
        # if msg has prefix
        command.run(msg)

client.run(setting["discord"])
print("ok")