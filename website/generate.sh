set -euo pipefail

for pm in Pm01-10 Pm11-20 Pm21-30 Pm31-40 Pm41-50 Pm51-63; do
    echo $pm
    cat >content/meghaduta/$pm.md <<EOF
---
kind: "page"
layout: "ramepage"
alignmentjson: "meghaduta/word_alignment/$pm.json"
alignmentaudio: "https://archive.org/download/meghadUta-mUlam-vedabhoomi.org/$pm.mp3"
---
EOF
done

for f in data/audio_alignment/ramayana/word_alignment/Kanda_*.json; do
    echo $f
    echo $f | python3 generate.py
done
