# GLaDOS Voice Pack for Dreame Vacuum Robots

Uses voice generation by [UberDuck](https://uberduck.ai).
Requires an UberDuck API Key! Set in `main.py`

MD5 sum of the prepackaged `voice_pack.tar.gz`:  `9303cf5d8df75ad74c12ce9b6d773705`

Works at least with Dreame `L10 Pro`, `Z10 Pro`, `W10`, and `D9`.

## Installation

1. In Valetudo go to "Robot Settings" -> "Misc Settings"
1. Enter the following information in the "Voice packs" section:
    - URL: `https://github.com/nold360/voice_pack_dreame/raw/main/voice_pack.tar.gz`
    - Language Code: `GLADOS`
    - Hash: `9303cf5d8df75ad74c12ce9b6d773705`
1. Click "Set Voice Pack"

## Creating own Package

0. Install uberduck: `pip3 install uberduck`
1. Modify `main.py`
2. Run `main.py`
3. Run `package.sh`
4. Upload to Robot

-----
Thanks to https://github.com/ccoors/dreame_voice_packs for the inspiration and the list of sounds and 15.ai for the voice generation.
