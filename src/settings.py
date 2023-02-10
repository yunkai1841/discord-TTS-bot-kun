import json


def get_discord_token(debug=False):
    with open(file=r"settings/config.json") as f:
        tokens = json.load(f)

        if debug:
            print(tokens["discord"])

        return tokens["discord"]


def get_voicevox_url(debug=False):
    with open(file=r"settings/config.json") as f:
        tokens = json.load(f)

        if debug:
            print(tokens["voicevox_url"])

        return tokens["voicevox_url"]


def get_text_max_length(debug=False):
    with open(file=r"settings/config.json") as f:
        tokens = json.load(f)

        if debug:
            print(tokens["text_max_length"])

        return tokens["text_max_length"]
