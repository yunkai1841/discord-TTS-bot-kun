prefix = "yun"
ready = False
con_server = []

def is_ready():
    return ready

def set_ready(newstatus):
    ready = newstatus
    
def connect(server):
    global con_server
    con_server += server

def disconnect(server):
    global con_server
    con_server.remove(server)

def is_connect(server):
    return server in con_server