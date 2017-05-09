"""
This script takes as input a list of OTU ids and finds the corresponding rep sequence

"""

import sys, re


# Finding required parameters
def params_open():
    filein = ''
    fileout = ''
    rep_set = ''
    for i, x in enumerate(sys.argv):

        if x == "-i":
            filein = sys.argv[i+1]
        elif x == "-o":
            fileout = sys.argv[i+1]
        elif x == "-r":
            rep_set = sys.argv[i+1]

    return filein, fileout, rep_set

def extract_otu_line(filein):
    otu_ids = []
    with open(filein, 'r') as infile:
        for line in infile:
            line = line.strip()
            otu_ids.append(line)
    return otu_ids

def output_seq(outfile, otu, rep_seq):

    outfile.write(otu + rep_seq)

    return

def find_otu_rep_seq(outfile, otu, rep_set_file):

    with open(rep_set_file, "r") as rep_set:
        for line in rep_set:
            if ">" + otu in line:
                output_seq(outfile, line, next(rep_set))
                break
            else:
                continue

    return

def main():

    infile, outfile, rep_set = params_open()

    with open(outfile, 'w') as fileout:

        otu_ids = extract_otu_line(infile)

        for otu in otu_ids:

            find_otu_rep_seq(fileout, otu, rep_set)
            
    return

main()