#!/usr/bin/env python3

import sys
import re
InputFile = open('outtree', 'r')
Lines = InputFile.readlines()

NoTabs = []
for i in Lines:
    NoTabs.append(re.sub(r"[\t]*", "", i))

FinalOutput = ''
for i in NoTabs:
    FinalOutput = FinalOutput + i

ncbi_to_strain_mapping = {
        "ASM118865": "LM850658",
        "ASM145488": "WSLC 1020",
        "ASM19539": "J1-220",
        "ASM202516": "LI0521",
        "ASM2118": "HCC23",
        "ASM220821": "FDA00006907",
        "ASM228583" : "FDA00011238",
        "ASM303191": "PIR00546",
        "ASM30706": "SLCC2376 4c",
        "ASM381256": "FDAARGOS_554",
        "ASM145486": "WSLC 1019",
        "ASM154858": "CFSAN023459",
        "ASM199904": "10-092876-1155 LM6",
        "ASM20975": "L99",
        "ASM21830": "M7",
        "ASM228565": "FDA00006905",
        "ASM303040": "CFSAN054108",
        "ASM303205": "PIR00544",
        "ASM343341": "CIIMS-PH-1",
        "ASM43868": "N1-011A",
    }


# Converting NCBI codes in NewickTree to Strain Names , since that is what we care about
for ncbi_code, strain_name in ncbi_to_strain_mapping.items():
    FinalOutput = FinalOutput.replace(ncbi_code, strain_name)

Out = open('NewickTree', 'w')
Out.write(FinalOutput)
