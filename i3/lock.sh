#!/bin/sh -e

# Take a screenshot
scrot /tmp/screen_locked.png

# Pixellate it 10x
mogrify -blur 0x10 /tmp/screen_locked.png

# Lock screen displaying this image.
i3lock -i /tmp/screen_locked.png
