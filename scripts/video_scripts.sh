# This breaks things down into frames for 

filename=$1

echo $filename
filename_short=${filename/%.*/}
filename_short_dir=${filename_short}_frames/
mkdir -p ${filename_short}_frames/

mkdir -p ${filename_short}_frames/test
mkdir -p ${filename_short}_frames/train
wait

ffmpeg -i $filename -r 24/1 ${filename_short_dir}/out%03d.png

