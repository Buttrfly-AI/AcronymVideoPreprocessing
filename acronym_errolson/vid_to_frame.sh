
foldername=$1

i=0
for entry in "$foldername"/*
do
  ffmpeg -i $entry -r 120/1 _frames/${i}out%03d.png
  
  wait
  ((i=i+1))

done