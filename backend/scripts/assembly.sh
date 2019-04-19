#!/bin/bash

get_input () {

    # Function to parse arguments
    # Specifying usage message
    usage="Usage: sh pipeline.bash -a <trimmed_1 reads> -b <trimmed_2 reads> -c <trimmed_UP reads> -o <output directory> -[OPTIONS]
              Bacterial short reads genome assembly software. The options available are:
                        -a : Location of trimmed forward (_1) reads [required]
			-b : Location of trimmed reverse (_2) reads  [required]
			-c : Location of trimmed unpaired (UP) reads [required]
                        -o : Output directory [required]
                        -k : Kmer range for spades (default=71,73,75,79)
                        -h : Print usage instructions"

  #Specifying deafult Arguments
  kmer_length="71,73,75,79"

  #Export kmer length to be used within xargs
  export kmer_length

  #Getopts block, will take in the arguments as inputs and assign them to variables
  while getopts "a:b:c:o:k:h" option; do
          case $option in
                  a) in1=$OPTARG;;
		  b) in2=$OPTARG;;
		  c) in3=$OPTARG;;
                  o) output_directory=$OPTARG;;
                  k) kmer_length=$OPTARG;;
                  h) echo "$usage"
                        exit 0;;
                 \?) echo "Invalid option."
                    "$usage"
                             exit 1;;
          esac
  done

}
get_input "$@"
#echo $in1
mkdir -p  $output_directory
spades.py -k $kmer_length -1 $in1 -2 $in2 -s $in3 --careful --cov-cutoff auto -o $output_directory/assembled
mkdir -p $output_directory/quast
quast.py $output_directory/assembled/contigs.fasta -o $output_directory/quast/

# Copy the Assembled User Sequence to the folder where the script is being executed.
cp $output_directory/assembled/scaffolds.fasta ./UserSeq

# The following script calculates the mash distance between the user sequence and 20 reference sequence.
# It then builds a distance matrix based on those values and outputs a new Newick Tree 
./test.sh

# Copy the Newick Tree to the output directory and remove it from the script directory
cp ./NewickTree $output_directory/UserTree
rm ./NewickTree

# readlink copies the address of the required genomes for comparison into the text file being created.
#readlink -e /projects/VirtualHost/predictc/Listeria_Sequences/LeastIdentity/* > ReferenceList.txt
#readlink -e InputFile >> ReferenceList.txt

# Compares the user input sequence against 20 of the most diverse genome sequences (collected in the previous step) and calculates the nucleotide identity for the input against the 20 genomes.
#fastANI --ql ReferenceList.txt --rl ReferenceList.txt -o $output_directory/fastANI_output.txt
#rm ReferenceList.txt

# annotation commands

mydir=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
if [ -d $output_directory/annotation ]; then rm -r $output_directory/annotation; fi
mkdir -p $output_directory/annotation

# RGI-CARD

if [ -d "$mydir"/localDB ]; then rm -r "$mydir"/localDB; fi


rgi load -i "$mydir"/annotation/card/card.json --card_annotation "$mydir"/annotation/card/nucleotide_fasta_protein_homolog_model.fasta --local
rgi main -i $output_directory/assembled/contigs.fasta -o "$mydir"/card_out.temp --input_type contig --local
python3 "$mydir"/convert_rgi.py -i "$mydir"/card_out.temp.txt -o $output_directory/annotation/card.temp

if [ -d "$mydir"/localDB ]; then rm -r "$mydir"/localDB; fi
rm *.temp*

# VFDB

if [ -d "$mydir"/annotation/vfdb/temp ]; then rm -r "$mydir"/annotation/vfdb/temp; fi

python3 "$mydir"/vfdb_out.py -i $output_directory/assembled/contigs.fasta -o $output_directory/annotation/vfdb.temp

# combine files into GFF format

cat $output_directory/annotation/vfdb.temp $output_directory/annotation/card.temp > $output_directory/annotation/annotation.gff3

rm $output_directory/annotation/*.temp*
