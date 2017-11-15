#!/usr/bin/python

from sorter import sort_dict

def frequency_analysis(filename):
    """frequency_analysis: filename -> file analyzing word frequency
    Purpose: Open and read a text file and count the frequency
    at which each word appears. Then print the words and their
    frequency in descending order in a new text file.
    Example: frequency_analysis('breakfast.txt') -> myAnalysis.txt
    where "the 1523; a  578..."
    """

    """We open the file and for every line in the file, we
    split the words into separate strings and add them to a list"""
    file = open(filename)
    list = []
    for line in file:
        words = line.split()
        for i in words:
            list.append(i)
    file.close();

    """We iterate over the list and if it's the first time that we
    encounter the word, we store it as a new key in our dictionary
    called freqCount and set its count to 1. If the string already
    has a key in freqCount, we simply add one to the count."""
    freqCount = {}
    for n in list:
        if freqCount.has_key(n):
            freqCount[n] = freqCount[n] + 1
        else:
            freqCount[n] = 1

    # Sorting freqCount in descending order; converts dictionary to list
    freqCount = sort_dict(freqCount)

    """We create and open a new file and for each 'key' in the list,
    we print out the key and the frequency separated by a space on their
    own line in the file"""
    file = open('myAnalysis.txt', 'w')
    for i in range(len(freqCount)):
        file.write(freqCount[i][0] + " " + str(freqCount[i][1]) + '\n')
    file.close

if __name__ == '__main__' :
    frequency_analysis('breakfast.txt')
