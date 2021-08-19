import discord
import io

import status, command, settings, speek

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
    
    elif msg.content.startswith(status.prefix):
        # if msg starts with prefix
        await command.run(msg)

    elif status.is_connect(msg.guild) and\
        status.is_observing(msg.guild, msg.channel) and\
        not msg.guild.voice_client.is_playing():
        ssml = speek.text_to_ssml(msg.content)
        audio = speek.ssml_to_speech(ssml)
        bs = io.BytesIO(audio)
        msg.guild.voice_client.play(discord.PCMAudio(bs))

client.run(tokens["discord"])