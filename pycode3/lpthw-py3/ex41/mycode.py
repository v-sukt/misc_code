import random, sys
from urllib.request import urlopen

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
        "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
        "Set *** to an instance of class %%%.",
    "***.***(@@@)":
        "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'.",
}

# do they want to drill phases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    # strip the new line and convert it as utf-8 string
    WORDS.append(str(word.strip(), encoding="utf-8"))

# if there is issue with internet use the already downloaded file
if len(WORDS) == 1:
    from pathlib import Path
    files = Path("./").rglob("words.txt")
    WORDS = []
    for file in files:
        for word in file.open().readlines():
            WORDS.append(str(word.strip()))


def convert(snippet, phrase):
    # % has class names
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
    # * represent others - functions names or variables
    other_names = random.sample(WORDS, snippet.count("***"))  # the list of second no of elements from first sequence
    results = []
    param_names = []

    # @ has the argument to function
    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(", ".join(
            random.sample(WORDS, param_count)
        ))

    # construct the sentence for both snippet and phrase
    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class names
        for word in class_names:  # works same for snippet and phrase as list is sequential
            result = result.replace("%%%", word, 1)  # replace first occurrence with word

        # fake other names
        for word in other_names:  # works same for snippet and phrase as list is sequential
            result = result.replace("***", word, 1)  # replace first occurrence with word

        # fake parameter lists
        for word in param_names:  # works same for snippet and phrase as list is sequential
            result = result.replace("@@@", word, 1)  # replace first occurrence with word

        results.append(result)  # append the created result to results list

    return results


# keep going until they hit CTRL-D
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)  # shuffle the snippets taken in-place

        for snippet in snippets:
            phrase = PHRASES[snippet]  # get the values using the key (randomized earlier)
            # like code snippet and english meaning
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:  # if asked for phrase first replace positions of meaning and code
                question, answer = answer, question
            print(question)

            input("> ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:  # one that we get with ^D / Ctrl + D
    print("Bye\n")
