import discord


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
