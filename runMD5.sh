# PE32/MD5-script-o-matic
# By Sketchymoose
# verion 1.0
# This script takes 3 arguments:
# $1 -> directory of extracted_files
# $2 -> directory of where you want the VT Results to 
# $3 -> path of MD5.txt file 

cd $1
for i in `file * | grep PE32 | cut -d ":" -f 1`; do md5sum $i >> $3; done
cd $2
python SubmitMD5VT.py $2 $3

