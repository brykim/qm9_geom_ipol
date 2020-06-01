#############
## MODULES ##
#############

import os, sys

###############
## FUNCTIONS ##
###############

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
            fh.write("[%i][%i]%s\t" % (i,j,array[i][j]))
        fh.write("\n")

############
## INPUTS ##
############

path = '../1_data'
nconfig = 1333885

################
## MAIN BLOCK ##
################

with open("qm9_geom_ipol.txt", "w") as f:
    ind1=0
    for i in range(nconfig):
        ind1 = i+1
        print(ind1)
        filename = ("%s/dsgdb9nsd_%s.xyz" % (path,str(ind1).zfill(6)))
        xyz,nrow = read_file(filename)
        gdb9_id = int(xyz[1][1])
        ipol = float(xyz[1][6])
        natm = int(xyz[0][0])
        f.write("%d\t%f\t%d\t" % (gdb9_id,ipol,natm))
        ind2=0
        for j in range(natm):
            ind2 = j+2
            atm_id = xyz[ind2][0]
            x = float(xyz[ind2][1].replace('*^','E',1))
            y = float(xyz[ind2][2].replace('*^','E',1))
            z = float(xyz[ind2][3].replace('*^','E',1))

            if (j < natm-1):
                f.write("%s\t%f\t%f\t%f\t" % (atm_id,x,y,z))
            else:
                f.write("%s\t%f\t%f\t%f\n" % (atm_id,x,y,z))

##############
## END MAIN ##
##############

