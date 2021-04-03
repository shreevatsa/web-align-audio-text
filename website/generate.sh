set -euo pipefail
for f in data/audio_alignment/ramayana/sentence_alignment/Kanda_*.json; do
    echo $f
    echo $f | python3 generate.py
done
