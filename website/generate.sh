for f in data/audio_alignment/ramayana/sentence_alignment/Kanda_*.json; do g=$(basename $f); echo $g; echo $g | python3 generate.py; done
