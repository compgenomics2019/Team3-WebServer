#!/usr/bin/env bash
#inDir="/mnt/c/Users/miles_000/Downloads/BIOL_7210/ncbi-genomes-2019-04-08"
inDir="/mnt/c/Users/miles_000/Downloads/BIOL_7210/LeastIdentity"
outDir="/mnt/c/Users/miles_000/Downloads/BIOL_7210/Team3-WebServer/frontend/jbrowse/data/"

#Make the reference file
echo "Making the references"
for file in $inDir/*.fna; do
	base=$(basename $file .fna) # extract the basename of a file (remove path and extension)
	base=${base/./_} # replace the period with an underscore
	echo $base
	trackDir="$outDir""$base"
	echo $trackDir
	mkdir $trackDir
	/mnt/c/Users/miles_000/Downloads/BIOL_7210/Team3-WebServer/frontend/jbrowse/bin/prepare-refseqs.pl --fasta $file --out $trackDir
done

#Make the gff track
echo "Making the gff tracks"
for file in $inDir/*.gff; do
	base=$(basename $file .gff) # extract the basename of a file (remove path and extension)
	base=${base/./_} # replace the period with an underscore
	label="GFF_""$base"
	trackDir="$outDir""$base"
	echo $trackDir
	/mnt/c/Users/miles_000/Downloads/BIOL_7210/Team3-WebServer/frontend/jbrowse/bin/flatfile-to-json.pl --gff $file --out $trackDir --trackLabel $label
done

#Edit the JBrowse configuration file so that the new genomes appear in the dropdown menu of Genomes
echo "Editing the configuration file"
for file in $inDir/*.gff; do
	base=$(basename $file .gff) # extract the basename of a file (remove path and extension)
	base=${base/./_} # replace the period with an underscore
	trackDir="$outDir""$base"
	echo $trackDir
	echo "[general]
dataset_id = $base
[datasets.$base]
url  = ?data=data/$base
name = $base
" >> /mnt/c/Users/miles_000/Downloads/BIOL_7210/Team3-WebServer/frontend/jbrowse/jbrowse.conf
done
