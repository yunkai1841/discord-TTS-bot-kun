import discord

import status, command, settings, speak

client = discord.Client(intents = discord.Intents.all())

tokens = settings.get_token()

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

        speak.text_to_speech(msg.content, "out.wav")
        msg.guild.voice_client.play(discord.FFmpegPCMAudio("out.wav"))

@client.event
async def on_voice_state_update(member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
    if status.is_connect(member.guild):
        # disconnect if bot is alone
        if before.channel is not None and\
            len(before.channel.members) == 1 and\
            before.channel.members[0].id == client.user.id:
            await member.guild.voice_client.disconnect()

client.run(tokens["discord"])