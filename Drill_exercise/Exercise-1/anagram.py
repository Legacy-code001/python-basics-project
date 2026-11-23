def anagram_status(word1, word2):

    clean_string1 = "".join(word1.lower().split())
    clean_string2 = "".join(word2.lower().split())


    if len(clean_string1) != len(clean_string2):
        return False

    string_count1 = {}
    string_count2 = {}

    for char in clean_string1:
        string_count1[char] = string_count1.get(char, 0) + 1

    for char in clean_string2:
        string_count2[char] = string_count2.get(char, 0) + 1

    return string_count1 == string_count2

print(anagram_status('silent', 'ways'))
        
