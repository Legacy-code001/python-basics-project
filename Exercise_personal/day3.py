def filter_process():
   word_list = ["apple", "education", "ice", "ocean", "python", "umbrella"]
   output = [word for word in word_list if len(word) >= 5 and word[0] in "aeiou"]
   print(output)
filter_process()