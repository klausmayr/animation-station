#!/bin/bash

BASE_DIR="$HOME/animation-photos"
PHOTO_DIR="$BASE_DIR/photos"
STATE_FILE="$BASE_DIR/.last_photo_count"
OUTPUT_FILE="$BASE_DIR/video/animation.mp4"

CURRENT_COUNT=$(ls "$PHOTO_DIR"/photo_*.jpg | wc -l)
LAST_COUNT=$(cat "$STATE_FILE")
NEW_PHOTOS=$((CURRENT_COUNT - LAST_COUNT))

if [ "$NEW_PHOTOS" -ge 10 ]; then
    ffmpeg -y -framerate 15 \
        -i "$PHOTO_DIR/photo_%06d.jpg" \
        -c:v libx264 \
        -pix_fmt yuv420p \
        "$OUTPUT_FILE"

    echo "$CURRENT_COUNT" > "$STATE_FILE"
fi

