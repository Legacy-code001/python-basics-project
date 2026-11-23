def compose(f, g):
    return lambda x: f(g(x))

def pipe(*funcs):
    def inner(x):
        result = x
        for func in funcs:
            result=func(result)
            return result
    return inner

"""helper function"""
def whitspace(text: str) -> :
    return text.strip()

def lowercase(text: str) -> :
    return text.lower()

def removeVowel(text: str) -> :
    vowels = "aeiouAEIOU"
    return "".join(val for val in text if val not in vowels)

def reverseString(text: str) -> :
    # basecase, if string is empty return it
    if len(text) == 0:
        return ""
    
    return text[-1] + reverseString(text[:-1])

text_pipeline = pipe(
    whitspace,
    lowercase,
    removeVowel
    reverseString

)