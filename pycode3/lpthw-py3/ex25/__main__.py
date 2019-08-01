import mycode

sentence = "All good things come to those who wait."

words = mycode.break_words(sentence)
print(words)

sorted_words = mycode.sort_words(words)
print(sorted_words)

mycode.print_first_word(words)
mycode.print_last_word(words)
print(words)

mycode.print_first_word(sorted_words)
mycode.print_last_word(sorted_words)
print(sorted_words)

sorted_words = mycode.sort_sentence(sentence)
print(sorted_words)

mycode.print_first_and_last(sentence)
mycode.print_first_and_last_sorted(sentence)
