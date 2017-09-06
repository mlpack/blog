#!/bin/bash
#
# git pull, then rebuild the docs.
#
# $1: version of mlpack (should be unpacked into /var/www/www.mlpack.org/mlpack-x.y.z/)
# should be in the format "mlpack-2.2.3" or similar.  "mlpack-git" for git
# master.
srcdir=/Volumes/koch/src/blog/
docdir=/Volumes/koch/src/blog/script/$1/
postdir=/Volumes/koch/src/blog/script/doxygen-post/
doxygensrcdir=/Volumes/koch/src/blog/script/doxygen-src

cd $srcdir
cd build

# Adjust each post and add date.
$doxygensrcdir/adjust-meta.py

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
# Create authors page and author pages.
$doxygensrcdir/build-authors.py --path=$srcdir/doc/tutorials/

# Create authors page and author pages.
$doxygensrcdir/build-archive.py --path=$srcdir/doc/tutorials/

$doxygensrcdir/adjust-author.py --path=$docdir/doxygen

$doxygensrcdir/build-index.py --path=$srcdir/doc/tutorials/




