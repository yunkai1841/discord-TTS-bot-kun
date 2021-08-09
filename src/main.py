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
    
    if msg.content.startswith(status.prefix):
        # if msg starts with prefix
        await command.run(msg)

    if status.is_connect(msg.guild) and\
        status.is_observing(msg.guild, msg.channel):
        ssml = speek.text_to_ssml(msg.content)
        audio = speek.ssml_to_speech(ssml, outputfile="out.wav")
        bs = io.BytesIO(audio)
        msg.guild.voice_client.play(discord.PCMAudio(bs))

client.run(tokens["discord"])