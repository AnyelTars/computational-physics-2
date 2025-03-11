#!/usr/bin/env python

import sys

inputfolder  = sys.argv[1]
outputfolder = sys.argv[2]

print('Input folder is: ' + inputfolder, 'Output folder is: ' + outputfolder)

print('Now provide number please:')

inputnumber = input()
print('Now provide an integer please:')
inputint = input()


print('Thanks, the number provided is: ' + inputnumber)
print(int(inputint)//2)
