

files=($(find -E . -type f -regex "^.*$"))
for item in ${files[*]}
do
  printf "   %s\n" $item
done