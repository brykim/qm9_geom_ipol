fh = open("help.txt", "w")
log = False
log = True

#############
## MODULES ##
#############

import os, sys, math

'''
import numpy as np
import numpy.linalg as linalg
from numpy import mean
import copy
'''

###############
## FUNCTIONS ##
###############

def get_datetime():
    from datetime import datetime
    lt = datetime.now()
    timestamp = lt.strftime("%Y-%m-%d, %I:%M %p")
    return timestamp
    
def get_newdir(name):
    try:
        os.rmdir(name)
    except IOError:
        pass
    os.mkdir(name)

def read_list(comment_list):
    fdf = open("df_tmp", "w")
    fdf.write(comment_list)
    fdf.close()
    file = open("df_tmp", "r")
    array,nrow = read_file("df_tmp")
    file.close()
    os.remove("df_tmp")
    return array,nrow

def read_file(file_name):
    try:
        file = open(file_name, "r")
    except IOError:
        print('Error: file (%s) not found!\n' % (file_name))
        sys.exit()
    lines = file.readlines()
    file.close()
    array = []
    for line in lines:
        array.append(line.split())
    nrow = len(array)
    return array,nrow

def print_out(out):
    fh.write(out)

def print_read(array,x):
    for i in range(x):
        for j in range(len(array[i])):
            fh.write("[%i,%i]%s\t" % (i,j,array[i][j]))
        fh.write("\n")

def print_1d(x,var,array):
    for i in range(x):
        ii = i+1
        fh.write("%s[%d] = %6.3f\n" % (var,ii,array[i]))

def print_2d(x,y,array):
    for i in range(x):
        for j in range(y):
            fh.write("%6.3f " % array[i][j])
        fh.write("\n")

#######################
## DEFAULT VARIABLES ##
#######################

wrkdir = os.getcwd()
print(wrkdir)

############
## INPUTS ##
############

################
## MAIN BLOCK ##
################

"""
tmp_list = '''\
'''
tmp,ntmp = read_list(tmp_list)
"""

filenum = 33459

for i in range(filenum-1,filenum):
    filename = ("dsgdb9nsd_033459.xyz")
    tmp,ntmp = read_file("dsgdb9nsd_033459.xyz")

##############
## END MAIN ##
##############

if log == True:
    print_read(tmp,ntmp)

#https://stackoverflow.com/questions/10985603/multi-line-string-with-arguments-how-to-declare
out = """\
line %d
line %d
line %d
""" % (
1,
2,
3)
