import main

status = main.status

class Command:
    """Super class for each Command
    extend this class to make new command
    """
    def run(self, msg):
        #eliminate prefix
        prefix_len = len(status.prefix)+1
        msg_txt = msg.content[prefix_len:]

        if msg_txt.startswith("con"):
            self.connect(msg)

    def check(self, string):
        if string in self.command:
            return True
        else:
            return False

    def help_txt(self):
        with open("..\help\general.txt", "r") as f:
            return f.read()
        return "help_txt err"

    def connect(self, msg):
        if msg.author.voice is None:
            await msg.channel.send("あなたはボイスチャンネルに接続していません。")
            return
        # ボイスチャンネルに接続する
        await msg.author.voice.channel.connect()
        await msg.channel.send("接続しました。")
        status.connect(msg.channel)