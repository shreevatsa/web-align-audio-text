#!/bin/bash
# Download all Ramayana audio files from archive.org

set -e

STATIC_AUDIO="/Users/shreevatsa/w/web-align-audio-text/website/static/audio"
BASE_URL="https://archive.org/download/Ramayana-recitation-Sriram-harisItArAmamUrti-Ghanapaati-v2"
USER_AGENT="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"

# Extract audio file paths from markdown files (handles both old archive.org URLs and new local paths)
grep -h 'alignmentaudio:' /Users/shreevatsa/w/web-align-audio-text/website/content/sarga/*.md | \
    sed 's/.*alignmentaudio: "//' | \
    sed 's/".*//' | \
    sed 's|https://archive.org/download/Ramayana-recitation-Sriram-harisItArAmamUrti-Ghanapaati-v2/||' | \
    sed 's|^audio/||' | \
    sort -u | while read -r filepath; do

    # Extract Kanda directory (e.g., Kanda_1)
    kanda_dir=$(echo "$filepath" | cut -d'/' -f1)
    filename=$(echo "$filepath" | cut -d'/' -f2)

    dest_file="$STATIC_AUDIO/$kanda_dir/$filename"

    if [ -f "$dest_file" ]; then
        echo "SKIP: $filename (already exists)"
    else
        echo "Downloading: $filepath"
        # URL-encode spaces in the URL
        encoded_url=$(echo "$BASE_URL/$filepath" | sed 's/ /%20/g')
        curl -L -g -A "$USER_AGENT" -o "$dest_file" "$encoded_url"
    fi
done

echo "Done!"
