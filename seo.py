import re
import math
import sys
import operator

histogram_all = {}

def add_to_histogram(filename, histogram, key):
    if key in histogram:
        histogram[key]['nb_occurrences'] += 1
        if filename not in histogram[key]['pages']:
            histogram[key]['pages'].append(filename)
    else:
        histogram[key] = {'nb_occurrences' : 1, 'pages' : [filename]}

def extract_grams_from_words(words):
    res = []
    # index of k-gram
    for k in range(2, 8):
        # parse each gram
        for i in range(0, len(words) - k + 1):
            gram = ""
            # append gram
            for j in range(i, i + k):
                gram += words[j] + " "
            res.append(gram)
    return res

def analyse_file(filename):
    with open(filename) as f:
        words = re.findall(r"[\w']+", f.read())
        grams = extract_grams_from_words(words)
        for gram in grams:
            add_to_histogram(filename, histogram_all, gram)

def get_max_occurrences():
    res = 0
    for key, value in histogram_all.items():
        if value['nb_occurrences'] > res:
            res = value['nb_occurrences']
    return res

def analyse_data(argc):
    all_w = []
    max_occurrences = get_max_occurrences()
    for key, value in histogram_all.items():
        tf = float(value['nb_occurrences']) / (float)(max_occurrences)
        idf = math.log((float)(argc) / (float)(len(value['pages']))) + 1
        w = tf * idf

        all_w.append({"key" : key, "value" : w})

    return sorted(all_w, key=lambda e: e["value"], reverse=True)

def print_n_results(all_w, n):
    for i in range(0, n):
        print((i + 1), all_w[i]["key"], "=>", all_w[i]["value"])

if (len(sys.argv) > 1):
    for i in range(0, len(sys.argv) - 1):
        analyse_file(sys.argv[i + 1])
    print_n_results(analyse_data(len(sys.argv) - 1), 10)
else:
    print("Please enter at least one file.")
