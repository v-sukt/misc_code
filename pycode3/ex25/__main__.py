import code

sentence = "All good things come to those who wait."
words = code.break_words(sentence)
print(words)
sorted_words = code.sort_words(words)
print(sorted_words)
code.print_first_word(words)
code.print_last_word(words)
print(words)
code.print_first_word(sorted_words)
code.print_last_word(sorted_words)
print(sorted_words)
sorted_words = code.sort_sentence(sentence)
print(sorted_words)
code.print_first_and_last(sentence)
code.print_first_and_last_sorted(sentence)
