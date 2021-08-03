class Status:
    """class for server Status
    """

    prefix = "yun"

    def __init__(self):
        """init
        Set or get server status.
        """

        self.__ready = False
        self.con_channel = []
        print(self.__class__, "Ready")

    def is_ready(self):
        """getter for __ready
        Check if server is ready.
        """
        return self.__ready

    def set_ready(self, ready):
        """setter for __ready
        Set if server is ready
        """
        self.__ready = ready
        
    def connect(self, channel):
        self.con_channel += channel

    def disconnect(self, channel):
        self.con_channel.remove(channel)

    def is_connect(self, channel):
        return channel in self.con_channel