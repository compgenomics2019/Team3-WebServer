#!/usr/bin/env python3

import sys
import os
import subprocess
import argparse

#get directory path and append to files
DIR = os.path.dirname(__file__)
db_file = os.path.join(DIR,'annotation/vfdb/VFDB_setB_nt.fas')

#get input arguments
parser = argparse.ArgumentParser()
parser.add_argument('-i','--infile',required=True,help='Enter input .fasta file')
parser.add_argument('-o','--outfile',required=True,help='Enter output file')
args = parser.parse_args()

input_file = args.infile
out_file = args.outfile

#Run BLAST
temp_folder = os.path.join(DIR,'annotation/vfdb/temp/')
blast_output = os.path.join(DIR,'annotation/vfdb/temp/inter_output.txt')
subprocess.run(['mkdir {}'.format(temp_folder)], shell=True, check = True)
subprocess.run(['cp {} {}'.format(db_file,temp_folder)], shell=True, check=True)
subprocess.run(['makeblastdb -in {} -dbtype nucl'.format(temp_folder+'VFDB_setB_nt.fas')], shell=True, check = True)
subprocess.run(['blastn -query {} -db {} -out {} -evalue 1e-10 -outfmt "6 qseqid qstart qend qlen length qcovs pident evalue stitle" -max_target_seqs 1 -max_hsps 1'.format(input_file, temp_folder+'VFDB_setB_nt.fas', blast_output)], shell=True,check=True)

# parse and filter blast outputs
bls = open(blast_output,'r')
vls = os.path.join(DIR,'annotation/vfdb/temp/temp_final_out.txt')
out  = open(vls,'w')
in_fl = []
in_fl += bls

for line2 in in_fl:
	bls_split = line2.rstrip().split('\t')
	perc_ident = bls_split[6]
	if float(perc_ident) >= 90:
		out.write(line2)
bls.close()
out.close()

with open(vls,'r')as test:
	data = test.read().strip().split('\n')
	final_output = open(out_file,'w')
	source = "vfdb"
	feature = "virulence factor"
	strand = "."
	frame = "."
	final_output.write("##gff-version3\n")
	for i in range(len(data)):
		temp = data[i].split('\t')
		seqid = temp[0]
		start = temp[1]
		stop = temp[2]
		score = temp[7]
		attribute = "stitle={0};start={1};stop={2};evalue={3};querylength={4};alignlength={5};coverage={6};percentid={7}".format(temp[8],temp[1],temp[2],temp[7],temp[3],temp[4],temp[5],temp[6])
		final_output.write('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\n'.format(seqid,source,feature,start,stop,score,strand,frame,attribute))
	final_output.close()

subprocess.run(['rm -rf {}'.format(temp_folder)], shell=True, check = True)