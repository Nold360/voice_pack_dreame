from pathlib import Path
from typing import TypedDict, List, Union

import requests
from requests import Session
from uberduck import UberDuck

class UberAPI(UberDuck):
    max_text_len = 255

    def __init__(self, api_key, api_secret, voice):
        self.voice = voice
        self.s = Session()
        super(UberAPI, self).__init__(api_key, api_secret)
        self.num = 0

    def set_progress(self, num: int, of: int) -> None:
        self.num = num
        self.s.headers.update({"User-Agent": f"VacuumVoicePack ({num}/{of})"})

    def get_tts(self, text: str):
        assert len(text) <= self.max_text_len
        
        print("Synthezing: " + text)
        url = self.speak(text, voice=self.voice, play_sound=False, return_bytes=False)
        return url

    def tts_to_wavs(self, dir: Path, text: str) -> None:
        url = self.get_tts(text)
        dir.mkdir(exist_ok=True)

        print("fetching wav file: " + url)
        r = requests.get(url)
        with open(dir / f"{self.num}.wav", "wb") as f:
            f.write(r.content)
