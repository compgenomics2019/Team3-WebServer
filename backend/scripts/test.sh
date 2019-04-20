#!/bin/bash

readlink -e /projects/VirtualHost/predictc/Listeria_Sequences/MostDistance/* > Trial.txt

#cp /projects/VirtualHost/predictc/scripts/out/assembled/scaffolds.fasta ./UserSeq

readlink -e ./UserSeq >> Trial.txt
mash sketch -o TrialSketch -l Trial.txt
mash dist TrialSketch.msh TrialSketch.msh > Out.txt
sort -k1,1 -k2,2 Out.txt > Sorted.txt

python ./scripts/DM.py Sorted.txt
#python /projects/home/ssharma435/Team3-WebServer/backend/scripts/DM.py Sorted.txt

#neighbor < Y
fitch < Y

python ./scripts/FinalEdits.py
#python /projects/home/ssharma435/Team3-WebServer/backend/scripts/FinalEdits.py

rm TrialSketch.msh
rm Trial.txt
rm Out.txt
rm Sorted.txt
rm infile
rm outfile
rm outtree
rm Y
rm UserSeq
