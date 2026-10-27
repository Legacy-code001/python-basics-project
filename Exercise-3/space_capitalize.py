def spaceAndCapitalize(word):
    word_arr = word.split(" ")

    for i in range(len(word_arr)):
        current_word = word_arr[i]
        if current_word:
            first_char = current_word[0]
        if ord(first_char) >= 97 and ord(first_char) <= 122:
            upperCase = ord(first_char) - 32

            word_arr[i] = chr(upperCase) + current_word[1:]

    return "".join(word_arr)

print(spaceAndCapitalize("hello world from python"))

    