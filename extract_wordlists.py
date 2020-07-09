#!/usr/bin/env python3

import sys
import csv
import json
import argparse
import re

def read_file(filename):

    lang_list_dict = {}

    with open(filename, "r", encoding="utf-8") as in_f:
        reader = csv.reader(in_f, delimiter=',')
        next(reader)

        for line in reader:
            print(line)
            lang_name = line[15]
            wordlist = line[19]  
            word_dict = _parse_wordlist(wordlist)

            lang_list_dict[lang_name] = word_dict
            print("___________________-")

    return lang_list_dict


def _parse_wordlist(wordlist):

    #import code
    #code.interact(local=locals())

    word_dict = {}
    wordlist = wordlist.split('\n')
    for line in wordlist:
        if line[0].isdigit():
            line.replace(',', '')
            tokens = line.split()
            word_concept = tokens[1]
            word_trans = [tokens[i] for i in range(2, len(tokens)-1)]
            word_dict[word_concept] = word_trans

    return word_dict
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert ASJP list of languages into JSON")
    parser.add_argument("-f", "--in_fil", help="Input file")
    parser.add_argument("-o", "--out_fil", help="output file")
    args = parser.parse_args()

    filename = args.in_fil
    output_f = args.out_fil
    
    lang_dict = read_file(filename)
    with open(output_f, 'w', encoding="utf-8") as out_f:
        json.dump(lang_dict, out_f)
