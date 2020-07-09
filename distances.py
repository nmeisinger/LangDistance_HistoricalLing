#!/usr/bin/env python3

from Levenshtein import distance
import json
import numpy as np
from pandas import DataFrame

def read_file(filename):
    with open(filename, 'rt', encoding="utf-8") as in_f:
        return json.load(in_f)

def save_distance_matrix(distance_matrix, filename="distance_matrix.csv"):

    with open(filename, "w", encoding="utf-8") as out_f:
        DataFrame.to_csv(distance_matrix, out_f)


def calc_distance_matrix(data):
    """Calculate a distance matrix between languages.
    1. Calculates Levensthein distance for every word between two languags (assuming they both have
    the given concept)
    2. Normalizes the Levensthein distance: words_d / longest_word_d
    3. Calculates language distance: word1_d + word2_d + ... + wordn_d / amount of words

    Returns: the distance matrix (Pandas DataFrame)
    """
    d_matrix = np.zeros(shape=(len(data.keys()), len(data.keys())))
    i = 0

    for lang1, lang1_dict in data.items():
        j = 0
        for lang2, lang2_dict in data.items():
            lv_distances = []
            
            for w_concept1, word1_l in lang1_dict.items():
                word2_l = lang2_dict.get(w_concept1, None)

                # if word concept not in list
                if word2_l is None:
                    continue

                dis_list = []

                # some words have more than one translation for a given concept
                # I take the smallest distance as given one
                for w1 in word1_l:
                    for w2 in word2_l:
                        dis_list.append(distance(w1, w2))

                lv_distances.append(np.min(dis_list))

            longest_wd = np.max(lv_distances)

            if longest_wd > 0:
                lv_distances = [x/longest_wd for x in lv_distances]

            lang_dist = np.sum(lv_distances) / len(lv_distances)

            d_matrix[i][j] = lang_dist
            j += 1
        i += 1

    d = DataFrame(d_matrix)
    d.index = data.keys()
    d.columns = data.keys()
    return d
    

if __name__ == "__main__":

    data = read_file("lang2.json")
    d = calc_distance_matrix(data)
    save_distance_matrix(d)