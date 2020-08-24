#!/usr/bin/env python3

import argparse
import extract_wordlists as ew
import distances
import json


if __name__ == "__main__":
    """
    Command Line interface to get distance matrix + Tree in one line
    Example usage: $python3 kwic.py -f Germanic_Lang_ASJP.csv -o Test
    Produces: Test.csv (distance matrix) and Test.png (Tree of distance matrix)
    For network, R script is necessary (using the distance matrix produced here)
    """
    
    parser = argparse.ArgumentParser(description="Convert ASJP list of languages into JSON")
    parser.add_argument("-f", "--in_fil", help="Input file", required=True)
    parser.add_argument("-b", "--blacklist", help="Blacklist file", required=False)
    parser.add_argument("-o", "--out_fil", help="output file (file ending appended automatically)", required=True)
    args = parser.parse_args()

    filename = args.in_fil
    blacklist = args.blacklist
    output_f = args.out_fil
    
    # get concept dictionary
    if blacklist is None:
        lang_dict = ew.read_file(filename)
    else:
        lang_dict = ew.read_file(filename, blacklist)

    distance_matrix = distances.calc_distance_matrix(lang_dict)
    distances.save_distance_matrix(distance_matrix, (output_f + ".csv"))

    distances.lingpy_tree(distance_matrix, filename=("tree_" + output_f + ".png"))