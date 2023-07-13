# GLaDOS Voice Pack for Dreame Vacuum Robots

Uses voice generation by [UberDuck](https://uberduck.ai).

Requires an UberDuck API Key! Set in `main.py`

Works at least with Dreame `L10 Pro`, `Z10 Pro`, `W10`, and `D9`.

See [release page](https://github.com/Nold360/voice_pack_dreame/releases) for pregenerated voice packs.

## Installation

1. In Valetudo go to "Robot Settings" -> "Misc Settings"
1. Enter the information from the [release page](https://github.com/Nold360/voice_pack_dreame/releases) in the "Voice packs" section. e.g.:
    - URL: `https://github.com/Nold360/voice_pack_dreame/releases/download/glados-p2/voice_pack.tar.gz`
    - Language Code: `GLADOS`
    - Hash: `9303cf5d8df75ad74c12ce9b6d773705`
1. Click "Set Voice Pack"

## Creating own Package

0. Install uberduck: `pip3 install uberduck`
1. Set API-Credentials/voice in `main.py`
2. Run `python3 main.py`
3. Run `bash package.sh`
4. Upload tar.gz to Robot

-----
Thanks to https://github.com/ccoors/dreame_voice_packs for the inspiration and the list of sounds and 15.ai for the voice generation.
