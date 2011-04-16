#!/bin/sh
##
## translate_figures.sh
## 
## Made by Jean-Noël Avila
## Login   <jna@muscade>
## 
## Started on  Sat Apr 16 08:25:05 2011 Jean-Noël Avila
## Last update Sat Apr 16 08:25:05 2011 Jean-Noël Avila
##

lang=$1
# translate the svg files
for image_file in `ls *.svg`
do 
    xml2po -p ../$lang/figure-sources/figures.po $image_file > ../$lang/figures-source/$image_file
    inkscape -z -d 300 -D -f ../$lang/figures-source/$image_file -e ../$lang/figures/${image_file%%svg}png
done


