# Task:

Count the number of each letter in a sentence.
The department you work for undertook a project construction that makes word / text analysis. 
You are asked to calculate the number of letters or any chars in the sentences entered under this project.
Write a Python program that;
takes a sentence from the user,
counts the number of each letter/chars of the sentence,
collects the letters/chars as a key and the counted numbers as a value in a dictionary.


def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency('hippo runs to us!'))




str1 = "hippo runs to us"

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

freq_words = word_count(str1)
print(freq_words)
