#!/usr/bin/env python3

import sys
import csv
import json
import argparse

def read_file(filename):

    lang_list_dict = {}

    with open(filename, "r", encoding="utf-8") as in_f:
        reader = csv.reader(in_f, delimiter=',')
        next(reader)

        for line in reader:
            lang_name = line[15]
            wordlist = line[19]  
            word_dict = _parse_wordlist(wordlist)

            lang_list_dict[lang_name] = word_dict

    return lang_list_dict


def _parse_wordlist(wordlist):

    wordlist = wordlist.split()[5:]
    eng_word = ""
    next_eng = False
    word_dict = {}

    for elem in wordlist:
        if elem.isdigit():
            next_eng = True
            continue
        elif next_eng:
            eng_word = elem
            word_dict[elem] = []
            next_eng = False
            continue
        elif elem != "//" and eng_word != "":
            if elem[-1] == ',':
                elem = elem[:-1]
            word_dict[eng_word].append(elem)

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
