class Status:

    def __init__(self):
        self.__ready = False
        print(self.__class__, "Ready")

    # check server status
    def is_ready(self):
        return self.__ready

    def set_ready(self, ready):
        self.__ready = ready

