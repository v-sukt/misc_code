#Set the common formatter for the section below
formatter = "%r %r %r %r" # try later with * 4

print formatter % (1, 2, 3, 4) # the formatter can print the numbers
print formatter % ("one", "two", "three", "four") # can even print single word strings
print formatter % (True, False, False, True) # also can print the boolean values
print formatter % (formatter, formatter, formatter, formatter) # can also print the formatter string
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",  # note this output - will be quoted in " unlike others due to ' in the string
    "So I said goodnight.", # note the last comma added - no error, just accepted as is
)  # the las but not least can print the begger strings - separated by comma character
