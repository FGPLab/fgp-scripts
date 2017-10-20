#!/usr/bin/env python

import sys


# Finding required parameters
def params_open():
    filein = ''
    fileout = ''

    for i, x in enumerate(sys.argv):

        if x == "-i":
            filein = sys.argv[i+1]
        elif x == "-o":
            fileout = sys.argv[i+1]

    return filein, fileout

def rename_silva(line):

    acs_list = []
    acs_num = ""
    org_name = ""
    header_list = []
    newheader = ""

    header_list = line.split(";")
    acs_list = header_list[0].split(" ")
    acs_num = acs_list[0]
    acs_num = acs_num.rstrip()
    acs_num = acs_num.strip(">")
    acs_num = acs_num.lstrip()
    acs_num = acs_num.split(".")
    acs_num = acs_num[0]

    org_name = header_list[6]
    org_name = org_name.rstrip()
    org_name = org_name.replace(" ", "_").replace("=", "_").replace("-", "_").replace(".", "_").replace("\'", "_").replace("\"", "_")

    newheader = ">" + org_name + "_" + acs_num + "\n"

    return newheader

def main():

    filein, fileout = params_open()

    with open(fileout, "w") as outfile:

        with open(filein, "r") as infile:
            for line in infile:
                if line[0] == ">":
                    newheader = rename_silva(line)
                    outfile.write(newheader)

                else:
                    outfile.write(line)

    return

main()
