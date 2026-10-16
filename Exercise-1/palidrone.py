# def check_word(word):
#     word_lower = word.lower()
#     rev = ''
#     for i in range(len(word_lower)-1, -1, -1):
#         rev += word_lower[i]
    
#     if word_lower == rev:
#         return f'{word} is a palidrone'
#     else:
#         return f'{word} is a palidrone'

# print(check_word('hannah'))


#let use recursive function
def is_palindrome(text, left, right):
    """base case and if the the pointer meet, its a palidrone"""
    if left >= right:
        return f'{word} is a palidrone'
        
    if text[left] != text[right]:
        return f'{word} is not palidrone'
    
    return is_palindrome(text, left + 1, right - 1)


# Example usage:
# word = "racecar"
word = "hannah"
print(is_palindrome(word, 0, len(word) - 1))  # Returns True



    



