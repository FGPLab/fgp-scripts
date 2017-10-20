#!/usr/bin/env python

#Script written by Daniel Roush 10.17.2017
#For formatting sequence files in current directory from SAMPLEID_R1.fastq.gz to
# CASVA1.8 Format: SAMPLEID_00_L001_R1_001.fastq.gz

#Import os so we do things to directories and files
import os

#Funtion that takes the filename input and modifies to casava 1.8 format.
#This function assumes files ares in SAMPLEID_R1.fastq.gz format. Code can be modified for files
#formatted differently.
def renamed(filename):
    filename_split =filename.split("_")

    cas18filename = filename_split[0] + "_00" + "_L001_" + filename_split[1].split(".")[0] + "_001.fastq.gz"

    return cas18filename

#Main function that goes through each file in the current directory one by one, checks to see if the file is a
#sequence file, and then renames it according to the rename function.
def main():
    for f in os.listdir():
        if f.split(".")[1] == "fastq":
            new_f = renamed(f)

            os.rename(f, new_f)

    return


#Execute script
if __name__ == "__main__":
    main()
