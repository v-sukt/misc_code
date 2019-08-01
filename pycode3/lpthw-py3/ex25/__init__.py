from .mycode import *

sentence = "All good things come to those who wait."

words = break_words(sentence)
print(words)

sorted_words = sort_words(words)
print(sorted_words)

print_first_word(words)
print_last_word(words)
print(words)

print_first_word(sorted_words)
print_last_word(sorted_words)
print(sorted_words)

sorted_words = sort_sentence(sentence)
print(sorted_words)

print_first_and_last(sentence)
print_first_and_last_sorted(sentence)
