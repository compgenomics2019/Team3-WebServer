#!/bin/bash

readlink -e /projects/VirtualHost/predictc/Listeria_Sequences/AllGenomes/* > QueryList.txt

mash sketch -o Trial -l QueryList.txt
mash dist Trial.msh Trial.msh > FinalOutput.txt

awk 'NR>1{
arr[$1] += $3
count[$1] += 1
}
END{
for (a in arr) {
print a","arr[a] / count [a]
}
}
' FinalOutput.txt > AverageIdentity.txt

sort -k2 -n -t ',' AverageIdentity.txt > SortedIdentity.txt

head -20 SortedIdentity.txt | cut -d',' -f1 | cut -d'/' -f7 > LeastDistance.txt
tail -20 SortedIdentity.txt | cut -d',' -f1 | cut -d'/' -f7 > MostDistance.txt

cd /projects/VirtualHost/predictc/Listeria_Sequences/AllGenomes

mkdir ../MostDistance
mkdir ../LeastDistance

cp $(cat /projects/VirtualHost/predictc/scripts/MostDistance.txt) ../MostDistance
cp $(cat /projects/VirtualHost/predictc/scripts/LeastDistance.txt) ../LeastDistance

mv /projects/VirtualHost/predictc/scripts/QueryList.txt ../
mv /projects/VirtualHost/predictc/scripts/FinalOutput.txt ../
mv /projects/VirtualHost/predictc/scripts/Trial.msh ../
mv /projects/VirtualHost/predictc/scripts/AverageIdentity.txt ../
mv /projects/VirtualHost/predictc/scripts/SortedIdentity.txt ../
mv /projects/VirtualHost/predictc/scripts/LeastDistance.txt ../
mv /projects/VirtualHost/predictc/scripts/MostDistance.txt ../

#rm QueryList.txt
#rm FinalOutput.txt
#rm Trial.msh
#rm AverageIdentity.txt
#rm SortedIdentity.txt
#rm LeastDistance.txt
#rm MostDistance.txt
