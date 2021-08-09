import asyncio
import discord

import status

async def run(msg: discord.Message):
    #eliminate prefix 
    prefix_len = len(status.prefix)+1
    msg_txt:str = msg.content[prefix_len:]

    if msg_txt.startswith("con"):
        await connect(msg)
    elif msg_txt.startswith(("dc", "dis")):
        await disconnect(msg)

def get_help_txt(self):
    with open("..\help\general.txt", "r") as f:
        return f.read()
    return "help_txt err"

async def connect(msg: discord.Message):
    if msg.author.voice is None:
        await msg.channel.send("あなたはボイスチャンネルに接続していません。")
        return
    # connect to voice channel
    await msg.author.voice.channel.connect()
    await msg.channel.send("接続しました。")
    status.connect(msg.guild, msg.channel)

async def disconnect(msg: discord.Message):
    if msg.guild.voice_client is None:
        await msg.channel.send("接続していません。")
        return

    # disconnect
    await msg.guild.voice_client.disconnect()

    await msg.channel.send("切断しました。")
    status.disconnect(msg.guild)

