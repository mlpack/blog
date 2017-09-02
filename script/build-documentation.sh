#!/bin/bash
#
# build the blog.

srcdir=../
docdir=../script/$1/
postdir=../script/doxygen-post/
doxygensrcdir=../script/doxygen-src

# Change into working directory.
cd $srcdir
cd build

# Do we need to update the Doxygen stylesheet?
modified_lines=`cat $srcdir/Doxyfile | grep 'doxygen-src/header.html' | wc -l`;
# Remove spaces from output.
modified_lines="${modified_lines// /}"

# Adjust each post and add date.
$doxygensrcdir/adjust-dates.py

# We have to build everything for the sake of the man pages.
# This probably precipitates cleaning the environment.
make clean
rm -rf doc/html/*
# Rebuild the man pages and the documentation.
make doc
# We need to invert all the images.
cd doc/html/
#mogrify -negate *.png
# Move the extra CSS.
cp $doxygensrcdir/tabs.css .
cp $doxygensrcdir/dynamic_tables.js .

# Now postprocess all of the HTML.
for i in *.html; do
  echo $i
  $doxygensrcdir/label_html_templates.py $i > tmp.html;
  mv tmp.html $i;
done
cd ../../

# Create blog directory.
mkdir -p $docdir

# Now move the HTML to the right place.
mv $docdir/doxygen $docdir/doxygen-old;
mv $srcdir/build/doc/html $docdir/doxygen;
rm -rf $docdir/doxygen-old;

# Remove doxygen markdown artifacts.
sed -n '/md_doc_/!p' $docdir/doxygen/pages.html > $docdir/doxygen/pages.tmp
mv $docdir/doxygen/pages.tmp $docdir/doxygen/pages.html

# Copy images to the right place.
cp -r $srcdir/doc/images $docdir/doxygen/images

# Copy menudata file to the right directory.
cp $doxygensrcdir/menudata.js $docdir/doxygen/

cp $docdir/doxygen/index.html $docdir/doxygen/authors.html
cp $docdir/doxygen/index.html $docdir/doxygen/pages.html
cp $docdir/doxygen/index.html $docdir/doxygen/author.html

# Create index html file.
cd ../script
$doxygensrcdir/build-index.py --path=$srcdir/doc/tutorials/

# Create authors page and author pages.
$doxygensrcdir/build-authors.py --path=$srcdir/doc/tutorials/

# Create authors page and author pages.
$doxygensrcdir/build-archive.py --path=$srcdir/doc/tutorials/
