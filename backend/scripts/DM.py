#!/usr/bin/env python3

import sys

InputFile = sys.argv[1]
#print(InputFile)
InputData = open(InputFile, 'r')
InputValues = InputData.readlines()
List_1 = []
List_2 = []
List_3 = []
List_Distance = []
for i in range(len(InputValues)):
    List_1.append((InputValues[i].split('\t')[0]).split('/')[-1])
    List_2.append(str(round(float(InputValues[i].split('\t')[2]),4)))

for i in List_1:
    if i not in List_3:
        List_3.append(i)

for i in List_2:
    a1 = float(i)
    a2 = (a1 - 100)
    if a2 < 0:
        a3 = a2 * -1
    else:
        a3 = a2
    a4 = str(round(a3, 4))
    List_Distance.append(a4)

#print(List_Distance)
List_Main = []

for i in range(len(List_3)):
    List_Main.append([])

for i in range(len(List_3)):
    for j in range(len(List_1)):
        if List_3[i] == List_1[j]:
            List_Main[i].append(List_2[j])

FinalOutput = '\t' + str(len(List_Main)) + '\n'
for x in List_Main:
    FinalOutput = FinalOutput + List_3[List_Main.index(x)].ljust(10) + '\t' + " ".join(x) + '\n'

FinalFile = open('infile', 'w')
FinalFile.write(FinalOutput)

Y_Though = open('Y', 'w')
Y_Though.write('Y')
