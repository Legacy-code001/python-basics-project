def manual_palindrome(text):
    str = ""
    text_cleaned = text.strip().lower().replace(" ", '')
    length = len(text_cleaned)
    for  i in  range(length - 1, -1, -1):
        str += text_cleaned[i]
    if text_cleaned == str:
        return True
    else:
        return False

