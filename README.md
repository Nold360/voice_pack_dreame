# GLaDOS Voice Pack for Dreame Vacuum Robots

using voice generation by [15.ai](https://15.ai/)

md5 sum of the prepackaged `voice_pack.tar.gz`: `c34109f9012b855a42096d7987dd9bd5`


## Installation

1. In Valetudo go to "Robot Settings" -> "Misc Settings"
1. Enter the following information in the "Voice packs" section:
    - URL: `https://github.com/Findus23/voice_pack_dreame/raw/main/voice_pack.tar.gz`
    - Language `Code: GLADOS`
    - Hash: `c34109f9012b855a42096d7987dd9bd5`
1. Click "Set Voice Pack"

Interestingly on my L10 Pro running `Valetudo 2022.03.0` the .tar.gz doesn't seem to work and the newly created folder `/data/personalized_voice/GLADOS` stays empty.
However, the language code is set correctly in Valetudo and manually copying the files into the right directory works:

```
git clone https://github.com/Findus23/voice_pack_dreame
scp voice_pack_dreame/output/* root@<YOUR_ROBOT_ADDRESS>:/data/personalized_voice/GLADOS
```

-----
Thanks to https://github.com/ccoors/dreame_voice_packs for the inspiration and the list of sounds and 15.ai for the voice generation.
