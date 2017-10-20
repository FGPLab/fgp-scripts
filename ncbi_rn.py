#!/usr/bin/env python

import sys

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

    return filein, fileout

def rename_genbank(line):
    org_name_holder = ""
    acs_num = ""
    org_name = ""
    header_list = []
    newheader = ""
    ncbi_header = ""
    ncbi_header_list = []
    acs_num_hold_list = []
    #example header
    header_list = line.split("|")

    if header_list[0] == ">gi":

        ncbi_header = header_list[1]
        ncbi_header_list = ncbi_header.split(" ")
        acs_num_hold = ncbi_header_list[0]
        acs_num_hold_list = acs_num_hold.split(":")
        acs_num = acs_num_hold_list[0]
        acs_num = acs_num.rstrip()
        acs_num = acs_num.strip(">")
        acs_num = acs_num.lstrip()
        acs_num = acs_num.split(".")
        acs_num = acs_num[0]

        org_name = ncbi_header_list[1] + "_" + ncbi_header_list[2] + "_" + ncbi_header_list[3] + "_" + ncbi_header_list[4] + "_"
        org_name = org_name.rstrip()
        org_name = org_name.replace(" ", "_")
        org_name = org_name.replace(".", "_")
        org_name = org_name.replace(";", "_")
        org_name = org_name.replace("'", "_")
        org_name = org_name.replace("\"", "_")
        org_name = org_name.replace(",", "_")
        org_name = org_name.replace("/", "_")
        org_name = org_name.replace("-", "_")
        org_name = org_name.replace(":", " ")


        newheader = ">" + org_name.lstrip("_") + "_" + acs_num + "\n"

    else:
        newheader = line

    return newheader

def main():

    filein, fileout = params_open()

    with open(fileout, "w") as outfile:

        with open(filein, "r") as infile:
            for line in infile:
                if line[0] == ">":
                    newheader = rename_genbank(line)
                    outfile.write(newheader)

                else:
                    outfile.write(line)

    return

main()
