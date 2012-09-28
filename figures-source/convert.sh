#!/bin/bash
mkdir -p ../figures
for image_file in `ls *.svg`; do 
    inkscape -z -d 100 -D -f $image_file -e ../figures/${image_file%%svg}png
    inkscape -z -D -f $image_file -A ../figures/${image_file%%svg}pdf
done