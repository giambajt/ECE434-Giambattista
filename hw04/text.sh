# Here's how to use imagemagick to display text
# Make a blank image
SIZE=320x240
TMP_FILE=/tmp/frame.png

# From: http://www.imagemagick.org/Usage/text/
convert -background red -fill blue -font Times-Roman -pointsize 24 \
      -size $SIZE \
      label:'ImageMagick\nJoshua Giambattista says Hi\n' \
      -draw "text 0,200 'Bottom of Display'" \
      $TMP_FILE

sudo fbi -noverbose -T 1 -a $TMP_FILE

# convert -list font
