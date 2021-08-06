from google.cloud import texttospeech
import re

def text_to_ssml(txt: str):
    """Str to ssml (beta)
    See ssml reference at  
    https://cloud.google.com/text-to-speech/docs/ssml

     - escape url
     - braek when encounter "\\n"
    """
    url_pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"

def tts()
