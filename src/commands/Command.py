class Command:
    """Super class for each Command
    Please extend this class to make new command
    """
    def __init__(self):
        self.command = []

    def run(self):
        """Content for command
        Override this method
        This is the main content of the command
        """
        print(self.__class__, "run")

    def check(self, string):
        if string in self.command:
            return True
        else:
            return False

    def help_txt(self):
        """Help text
        Get usage of this command
        """
        txt = """
        """
        return txt