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

Out = open('NewickTree', 'w')
Out.write(FinalOutput)
