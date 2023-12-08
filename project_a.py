def text_to_list(filename):
    with open(filename) as openfile:
        wordlist = []
        for line in openfile:
            line = line.strip("\n").split()
            for element in line:
                wordlist.append(element)
    return wordlist

def occurence_dictionary(list_argument):
    initialize_dictionary = {}
    for x in list_argument:
        if not x in initialize_dictionary:
            initialize_dictionary[x] = 1
        else: 
            initialize_dictionary[x] += 1 
    return initialize_dictionary

def max_value(dictionary_argument):
    maxvalue_key = None
    for key, value in dictionary_argument.items():
        if maxvalue_key == None or dictionary_argument[maxvalue_key] < value:
            maxvalue_key = key
    return max_key

def capitalized_key_count(word_count_dictionary):
    capitalized_dictionary = {"capitalized": 0, "non_capitalized": 0}
    for key, value in word_count_dictionary.items():
        word_is_upper = False
        for letter in key:
            if letter.isupper():
                capitalized_dictionary["capitalized"] += value
                word_is_upper = True
        if not word_is_upper:
            capitalized_dictionary["non_capitalized"] += value
    return word_count_dictionary

def punctuation_count(word_count_dictionary):
    punctuation_dictionary = {"punctuated": 0, "non_punctuated": 0}
    for key, value in word_count_dictionary:
        word_is_punctuated = False
        for letter in key:
            if 33 <= ord(letter) <= 47:
                punctuation_dictionary["punctuated"] += value
                word_is_punctuated = True
        if not word_is punctuated:
            punctuation_dictionary["non_punctuated"] += value
    return word_count_dictionary

