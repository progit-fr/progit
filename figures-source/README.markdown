# Localizing figures #

To fully localize the book, you may feel that you need to localize the figures as well.

Some figures in the book were extracted from the source graffle file and transformed into SVG. The transformation was not pixel-exact however. Obviously,the figures which represent screenshots are not transformed into SVG. Some SVG files do not need translation at all, but are included to maintain a uniform style in the figures.

SVG is a vector image format built as a XML-dialect. It is thus totally editable and translatable with a simple text editor. In these files, not only are the text translables, but if you need it, you can change the shapes as well, for instance make them longer to cope with translation lengthenings.

To make the translated SVG files consumable by the pdf and ebook toolchains, you need to convert them to `png` and `pdf`. The tool chosen in the convert.sh script uses [Inkscape](http://www.inkscape.org) for these transtyping.

# How to try localization #

1. Create a new branch experimental on your tree
     git checkout -b my_figures_l10n
2. Add the figure localization repo as a remote
     git remote add figure_l10n git://github.com/jnavila/progit.git; git fetch figure_l10n
3. Merge the figure_l10n branch in your experimental branch
     git merge figure_l10n/figure_l10n
4. Copy this directory to your localization folder
     cp -r figures-source [localization_folder] 
	 git add [localization_folder]/figures-source/*.svg
	 git commit -a 'first figure import'
5. Edit the svg files and localize the text.
6. Run the `convert.sh`; the final files are created in ../figures
7. Run your toolchain with localized figures included!

# Bugs ?

This development is in beta state. It has successfully been used for the french localization.

If you ever encounter issues, please let me know by filing an issue.
