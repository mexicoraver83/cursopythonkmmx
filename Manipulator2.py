#!/usr/bin/python
#Author: jcastelo - 04/03/2018

# This script will list the files in a directory

import os

path = raw_input("Enter the desire path to evaluate: ")

#Here we are removing the space on path location after drag and drop
path = path.rstrip()
#print path
# Here we are listing the content in the directory

for f in os.listdir(path):
	print 'Here is the content: ', f
