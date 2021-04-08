"""
Dea Roys
CP1404 Practicals week 5
word occurrence
"""

text = input("Text:").upper()
words = text.split()
words_list = {}

for word in words:
 words_list[word] = words_list.get(word, 0) +1

words = list(words_list.keys())
words.sort()
length_longest_word = max(len(word) for word in words)
for word in words :
 print("{:{}} : {}".format(word, length_longest_word,words_list[word]))
