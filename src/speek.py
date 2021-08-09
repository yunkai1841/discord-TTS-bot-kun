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

def ssml_to_speech(
    ssml: str, 
    language = "ja_JP", 
    voice_name = "ja-JP-Standard-A", 
    gender = None,
    outputfile = None):
    """Pass text to gcloud
    see reference
    https://cloud.google.com/text-to-speech/docs/reference/rpc/google.cloud.texttospeech.v1

    Return:
        audio content(binary)
    """
    input_text = texttospeech.SynthesisInput(ssml=ssml)

    voice = texttospeech.VoiceSelectionParams(
        language_code = language,
        name=voice_name,
        # ssml_gender=texttospeech.SsmlVoiceGender.SSML_VOICE_GENDER_UNSPECIFIED,
    )
    #TODO speaking_rate, pitch, valume_gain_db
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16,
        sample_rate_hertz=48000
    )
    response = tts_client.synthesize_speech(
        input=input_text, voice=voice, audio_config=audio_config
    )

    if outputfile != None:
        with open(outputfile, "wb") as out:
            out.write(response.audio_content)
            print('Audio content written to file "output.mp3"')

    return response.audio_content

def list_voices(language: str = None, debug: bool = False) -> list:
    """Get list of availiable voices
    see reference
    https://cloud.google.com/text-to-speech/docs/reference/rpc/google.cloud.texttospeech.v1

    Param:
        language: language_code (default=None)
        see website
        http://www.lingoes.net/en/translator/langcode.htm

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