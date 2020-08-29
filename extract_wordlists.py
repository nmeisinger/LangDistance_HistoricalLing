#!/usr/bin/env python3

import sys
import csv
import json
import argparse
import re
from lingpy import *

def read_file(filename, lang_filter=None):

    lang_list_dict = {}
    blacklist = ["OldEnglish", "OldFrisian", "OldHighGerman", "OldLowFranconian", "OldNorse", "OldSaxon", "ProtoGermanic", "Danish2",
    "Dutch2", "English2", "Icelandic2", "NorwegianBokmaal2", "Scots2", "StandardGerman2", "Swedish2", "Gothic"]


    if lang_filter is not None:
        with open(lang_filter, "r", encoding="utf-8") as in_f:
            for line in in_f:
                blacklist.append(line.strip())
    print(blacklist)
    with open(filename, "r", encoding="utf-8") as in_f:
        reader = csv.reader(in_f, delimiter=',')
        next(reader)

        for line in reader:
            lang_name = line[15]
            lang_name = lang_name.replace(" ", "")

            print( lang_name in blacklist, lang_name)
            if lang_name in blacklist:
                continue 

            wordlist = line[19]  
            word_dict = _parse_wordlist(wordlist)

            lang_list_dict[lang_name] = word_dict

    return lang_list_dict


def _parse_wordlist(wordlist):

    word_dict = {}
    wordlist = wordlist.split('\n')
    for line in wordlist:
        if line[0].isdigit():
            line.replace(',', '')
            tokens = line.split()
            word_concept = tokens[1]
            word_trans = [tokens[i].replace(',',"") for i in range(2, len(tokens)-1)]
            word_dict[word_concept] = word_trans

    return word_dict      


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert ASJP list of languages into JSON")
    parser.add_argument("-f", "--in_fil", help="Input file", required=True)
    parser.add_argument("-b", "--blacklist", help="Blacklist file", required=False)
    parser.add_argument("-o", "--out_fil", help="output file", required=True)
    args = parser.parse_args()

    filename = args.in_fil
    blacklist = args.blacklist
    output_f = args.out_fil
    
    if blacklist is None:
        lang_dict = read_file_lingpy(filename)
    else:
        lang_dict = read_file_lingpy(filename, blacklist)

    print(lang_dict)
    _create_csv(lang_dict, output_f)
    
