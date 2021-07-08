import discord

import Status

client = discord.Client()
status = Status()
command_list = []

@client.event
async def on_ready():
    print(client.user, "login")

@client.event
async def on_message(msg):
    for c in command_list:
        if c.check(msg):
            c.run()
