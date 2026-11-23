def censor_words(text, banned_word):
    # Guard case: if the banned word is empty, return the text unchanged
    if not banned_word:
        return text
        
    # Replace all exact case-sensitive matches globally
    return text.replace(banned_word, "***")
