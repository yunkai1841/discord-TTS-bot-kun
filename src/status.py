import discord

prefix = "yun"
max_length = 20
ready = False
con_server = []
observe_channel = {}
speaker = 3

def is_ready():
    return ready

def set_ready(newstatus):
    global ready
    ready = newstatus
    
def connect(guild: discord.Guild, channel: discord.TextChannel):
    con_server.append(guild)
    observe_channel[guild] = channel

def disconnect(guild: discord.Guild):
    global con_server
    con_server.remove(guild)
    observe_channel.pop(guild)

def is_connect(guild: discord.Guild):
    return guild in con_server

def observing_channel(guild: discord.TextChannel):
    # if not is_connect(guild):
        # raise Exception
    return observe_channel.get(guild)

def is_observing(guild: discord.Guild, channel: discord.TextChannel):
    return observe_channel.get(guild) == channel

def set_speaker(new_speaker):
    global speaker
    speaker = new_speaker