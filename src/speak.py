import requests
import json
import time

import status

base_url = "http://localhost:50021"


def synthesis(text: str, filename: str, speaker: int = 3, max_retry: int = 20, debug: bool = False):
    # speaker = 1: ずんだもん（あまあま）
    # speaker = 3: ずんだもん（ノーマル）

    # audio_query
    query_payload = {"text": text, "speaker": speaker}
    for query_i in range(max_retry):
        r = requests.post(base_url + "/audio_query",
                          params=query_payload, timeout=(10.0, 300.0))
        if r.status_code == 200:
            query_data = r.json()
            break
        time.sleep(1)
    else:
        raise ConnectionError(
            "リトライ回数が上限に到達しました。 audio_query : ", filename, "/", text[:30], r.text)

    # synthesis
    synth_payload = {"speaker": speaker}
    for synth_i in range(max_retry):
        r = requests.post(base_url + "/synthesis", params=synth_payload,
                          data=json.dumps(query_data), timeout=(10.0, 300.0))
        if r.status_code == 200:
            with open(filename, "wb") as fp:
                fp.write(r.content)
            if debug:
                print(
                    f"{filename} は query={query_i+1}回, synthesis={synth_i+1}回のリトライで正常に保存されました")
            break
        time.sleep(1)
    else:
        raise ConnectionError("リトライ回数が上限に到達しました。 synthesis : ",
                              filename, "/", text[:30], r, text)


def text_to_speech(text: str, filename: str):
    speaker = status.speaker
    synthesis(text, filename, speaker)


def get_speaker_list():
    r = requests.get(base_url + "/speakers")
    return r.json()