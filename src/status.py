import discord

prefix = "yun"
ready = False
con_server = []

def is_ready():
    return ready

def set_ready(newstatus):
    ready = newstatus
    
def connect(guild: discord.Guild):
    global con_server
    con_server.append(guild)

def disconnect(guild: discord.Guild):
    global con_server
    con_server.remove(guild)

def is_connect(guild: discord.Guild):
    return guild in con_server
