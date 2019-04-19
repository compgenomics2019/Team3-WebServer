#!/bin/bash


# Script written to find out 20 of the most diverse sequences from the 173 Listeria Sequences extracted from NCBI
# Script not involved in the final pipeline.
# Script was run just once to extract the 20 most diverse sequences.

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

#cd /projects/VirtualHost/predictc/Listeria_Sequences/AllGenomes

mkdir /projects/VirtualHost/predictc/Listeria_Sequences/MostDistance
mkdir /projects/VirtualHost/predictc/Listeria_Sequences/LeastDistance

#Transfer files listed in the two text files from the directory containing all the genomes to the required Directory.

rsync --files-from=MostDistance.txt /projects/VirtualHost/predictc/Listeria_Sequences/AllGenomes/ /projects/VirtualHost/predictc/Listeria_Sequences/MostDistance/
rsync --files-from=LeastDistance.txt /projects/VirtualHost/predictc/Listeria_Sequences/AllGenomes/ /projects/VirtualHost/predictc/Listeria_Sequences/LeastDistance/

#cp $(cat /projects/VirtualHost/predictc/scripts/MostDistance.txt) ../MostDistance
#cp $(cat /projects/VirtualHost/predictc/scripts/LeastDistance.txt) ../LeastDistance

mv QueryList.txt /projects/VirtualHost/predictc/Listeria_Sequences
mv FinalOutput.txt /projects/VirtualHost/predictc/Listeria_Sequences
mv Trial.msh /projects/VirtualHost/predictc/Listeria_Sequences
mv AverageIdentity.txt /projects/VirtualHost/predictc/Listeria_Sequences
mv SortedIdentity.txt /projects/VirtualHost/predictc/Listeria_Sequences
mv LeastDistance.txt /projects/VirtualHost/predictc/Listeria_Sequences
mv MostDistance.txt /projects/VirtualHost/predictc/Listeria_Sequences

#rm QueryList.txt
#rm FinalOutput.txt
#rm Trial.msh
#rm AverageIdentity.txt
#rm SortedIdentity.txt
#rm LeastDistance.txt
#rm MostDistance.txt
