import itertools
import math


def all_possibilities(n):
    possibilities = list(map(list, itertools.product([0, 1], repeat=n)))
    beg = ""
    string_possibilities = []
    for possibility in possibilities:
        string_possibility = [str(i) for i in possibility]
        string_possibilities.append(beg.join(string_possibility))

    return string_possibilities


def create_counts_all(counts, n):
    list_of_possibilities = all_possibilities(n)

    list_of_keys = list(counts.keys())
    for possibility in list_of_possibilities:
        if possibility not in list_of_keys:
            counts[possibility] = 0

    return counts


def probabilities(number_of_occurrences, number_of_shots):
    for key, value in number_of_occurrences.items():
        number_of_occurrences[key] = value / number_of_shots

    return number_of_occurrences


def min_entropy(probabilities_values):
    filtered_probabilities_values = [value for value in probabilities_values if value != 0.0]
    new_list = [-(math.log(x)) for x in filtered_probabilities_values]

    return min(new_list)


def porter_thomas_distribution(p, number_of_sequences):
    return number_of_sequences * math.exp(-number_of_sequences * p)


def middle_of_bins(bins):
    middle_of_bin_list = []
    for i in range(len(bins) - 1):
        middle_of_bin_list.append((bins[i + 1] + bins[i]) / 2)

    return middle_of_bin_list
