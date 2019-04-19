#!/usr/bin/env python3

import sys
import os
import subprocess
import argparse

#DIR = os.path.dirname(__file__)

parser = argparse.ArgumentParser()
parser.add_argument('-i','--infile',required=True,help='Enter input .fasta file')
parser.add_argument('-o','--outfile',required=True,help='Enter output file')
args = parser.parse_args()

vls = args.infile
out_file = args.outfile

with open(vls,'r')as test:
    data = test.readlines()
    del data[0]
    final_output = open(out_file,'w')
    source = "card"
    feature = "AMR"
    strand = "."
    frame = "."
    for i in range(len(data)):
        temp = data[i].split('\t')
        seqid = temp[1]
        start = temp[2]
        stop = temp[3]
        score = "."
        attribute = "drug class={0};resistance mechanism={1};AMR gene family={2};Orientation={3};Best hit ARO={4}".format(temp[14],temp[15],temp[16],temp[4], temp[8])
        final_output.write('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\n'.format(seqid,source,feature,start,stop,score,strand,frame,attribute))
    final_output.close()