class Status:
    """class for server Status
    """

    def __init__(self):
        """init
        Set or get server status.
        """

        self.__ready = False
        print(self.__class__, "Ready")

    def is_ready(self):
        """getter for __ready
        Check if server is ready.
        """
        return self.__ready

    def set_ready(self, ready):
        self.__ready = ready

