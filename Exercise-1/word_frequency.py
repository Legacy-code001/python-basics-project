# import string
from functools import reduce

def word_frequency(word):
    word_dic = {}
    word_list = word.split(" ")
    punctuation = "!?.,:;()\"'"
    for val in word_list:
        clean_val = val.strip(punctuation).lower()
        if not clean_val:
            continue
        if clean_val in word_dic:
            word_dic[clean_val] += 1
        else:
            word_dic[clean_val] = 1
    
    return word_dic


print(word_frequency("python is fun and python! is powerfull"))


""""""
the_word_dict = word_frequency("python is fun and python! is powerfull")
most_occcur = reduce(lambda x,y: x if x > y else y, the_word_dict.values())
print(most_occcur)