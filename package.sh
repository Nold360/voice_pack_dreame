#!/bin/bash
set -e
set -u

echo "Converting WAV to OGG"
for file in data/*.wav ; do
  name=$(basename $file | awk -F. '{print $1}')
  oggenc --resample=16000 -o "output/${name}.ogg" --downmix "$file"
done

echo "Packaging Voice Pack..."
tar -C output/ -czf voice_pack.tar.gz .
md5sum voice_pack.tar.gz
