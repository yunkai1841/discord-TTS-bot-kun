from google.cloud import texttospeech
import re

tts_client = texttospeech.TextToSpeechClient()

def text_to_ssml(txt: str) -> str:
    """Str to ssml (beta)
    See ssml reference at  
    https://cloud.google.com/text-to-speech/docs/ssml
    https://www.w3.org/TR/speech-synthesis/

     - escape url
     - braek when encounter "\\n"
    """

    #replace URL(spell-out)
    url_pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"
    txt = re.sub(url_pattern, "<say-as interpret-as=\"verbatim\">URL</say-as>", txt)

    #replace \n to break time
    txt.replace("\n", "\n<break time=\"1s\"/>")

    return txt

def tts(txt: str, language, gender):
    """Pass text to gcloud
    """
    pass

def list_voices(language: str = None, debug: bool = False) -> list:
    """Get list of availiable voices

    example:
        list_voices("ja_JP")
    """
    voices = tts_client.list_voices(language_code=language)

    voice_names = []
    for voice in voices.voices:
        voice_names.append(voice.name)

    if debug:
        for voice in voices.voices:
            print(f"Name: {voice.name}")
            gender = texttospeech.SsmlVoiceGender(voice.ssml_gender)
            print(f"Gender: {gender.name}")

    return voice_names

list_voices("ja-JP", True)