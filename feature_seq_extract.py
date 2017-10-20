"""
This script takes as input a list of Feature ids and finds the corresponding rep sequence

"""

import sys, re


# Parameters that need to be passed to the script

def params_open():
    filein = ''
    fileout = ''
    rep_set = ''
    for i, x in enumerate(sys.argv):
        #FeatureID list separated one per line
        if x == "-i":
            filein = sys.argv[i+1]
        #Output fasta name
        elif x == "-o":
            fileout = sys.argv[i+1]
        #name of representative sequence file
        elif x == "-r":
            rep_set = sys.argv[i+1]

    return filein, fileout, rep_set

#Function that creates a list containing feature ids with no newline characters
def extract_feature_id(filein):
    feature_ids = []
    with open(filein, 'r') as infile:
        for line in infile:
            line = line.strip()
            feature_ids.append(line)
    return feature_ids

#Outputs each representative sequence with feature ID to an empty file
def output_seq(outfile, feature_id, rep_seq):

    outfile.write(feature_id + rep_seq)

    return

#Function for searching for corresponding representative sequence to input FeatureID
#Looks for >FEATUREID then passes the >FEATUREID and the next line to the output_seq function

def find_feature_rep_seq(outfile, feature_id, rep_set_file):

    with open(rep_set_file, "r") as rep_set:
        for line in rep_set:
            if ">" + feature_id in line:
                output_seq(outfile, line, next(rep_set))
                break
            else:
                continue

    return

def main():

    infile, outfile, rep_set = params_open()

    with open(outfile, 'w') as fileout:

        feature_ids = extract_feature_id(infile)

        for feature in feature_ids:

            find_feature_rep_seq(fileout, feature, rep_set)

    return

if __name__ == "__main__":
    main()
