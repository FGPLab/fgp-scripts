#!/usr/bin/env python
#DWR FGPLAB 4.7.2017

import sys, re, hashlib


# Finding required parameters
# Requires input of a rep-set file from DADA2, an output file for the modified rep set, and then a second output file for the list of MD5 sums
def params_open():
    filein = ''
    fileout = ''
    md5_list = ''
    for i, x in enumerate(sys.argv):

        if x == "-i":
            filein = sys.argv[i+1]
        elif x == "-o":
            fileout = sys.argv[i+1]
        elif x == "-m":
            md5_list = sys.argv[i + 1]


    return filein, fileout, md5_list

def main():

    md5_line = ""

    filein, fileout, md5_list = params_open()

    with open(fileout, "w") as outfile:

        with open(md5_list, "w") as md5_name_list:
            #Loops read in sequence, convert to MD5 sum, and then rename sequence header with MD5 sum. Also writes a 1 name per line MD5 sum file
            with open(filein, "r") as infile:
                for line in infile:
                    if line[0] == ">":
                        continue

                    else:
                        md5_line = hashlib.md5(line.strip().encode())
                        outfile.write(">" + md5_line.hexdigest() + "\n" + line)
                        md5_name_list.write(md5_line.hexdigest() + "\n")

    return

main()
