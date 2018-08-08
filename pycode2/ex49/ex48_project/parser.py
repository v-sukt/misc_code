"""Parser functions to parse the lexocon list and form meaningful subject-verb-object sentence 
skipping unwnted sections"""

class ParserError(Exception):
    pass

class Sentence(object):
    """class provides way of storing the subject, verb and object as attributes. Can't use the methods to 
    separate the tuples with subject/verb/object as they are attributes of Sentemce, but doesn't have the 
    sentence structure which can store the list of words that can be parsed over and over without changing 
    its content"""

    def __init__(self, subject, verb, object):
        self.subject = subject[1] #stores the second object from the tuple received
        self.verb = verb[1]
        self.object = object[1]

    def __eq__(self, oneline):
        if self.subject == oneline.subject and self.verb == oneline.verb and self.object == oneline.object:
            return True
        else:
            return False


def peek(word_list):
    """Returns the first object of first tuple send from the tuple list received"""
    if word_list:
        word = word_list[0] # Get the first tuple of list
        return word[0]      # Get the first object from the tuple and return
    else:
        return None

def match(word_list, expecting):
    """Takes the type of the first tuple from list, if matching with expected returns the tuple"""
    if word_list:
        word = word_list.pop(0)
        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None

def skip(word_list, unwanted):
    """From the list of tuples removes unwanted type of tuples till some valid type is available - 
    return the valid tuple back to the caller - returned by the match method"""
    while peek(word_list) == unwanted:
        match(word_list, unwanted)

def parse_verb(word_list):
    """This function skips any unwanted tuples till wanted tuple arrive, then the list's first tuple
    is checked for verb type if so returns the tuple or returns None"""
    skip(word_list, 'stop')  # remove any stop words from start in word_list

    if peek(word_list) == 'verb':
        return match(word_list, 'verb') # return the mathcing tuple of verb type
    else:
        raise ParserError("Expecting a verb next time")

def parse_object(word_list):
    """This function skips any unwanted tuples till wanted tuple arrive, then the list's first tuple
    is checked for the noun/direction as both are objects else returns None"""
    skip(word_list,'stop')  # Remove any stop words from start in word_list

    next = peek(word_list) 

    if next == 'noun':
        return match(word_list, 'noun')
    elif next == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expecting a noun or verb next")

def parse_subject(word_list, subj):
    """Receives the list with subject as argument. Then gets verb and object from the list and returns 
    the Setence object containing all three"""
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return Sentence(subj, verb, obj)

def parse_sentence(word_list):
    """Skips the unwanted tuples from the word_list, then checks if first tuple is of noun type if so, 
    saves its content as subject, else if its of type 'verb', assumes the 'player' is assumed as subject
    and in both cases call parse_subject. In turn, returns the Sentence object"""
    skip(word_list, 'stop')

    start = peek(word_list)

    if start == 'noun':
        subj = match(word_list, 'noun')
        return parse_subject(word_list, subj)
    elif start == 'verb':
        subj = ('noun', 'player')
        return parse_subject(word_list, subj)
    else:
        raise ParserError("Must start with subject, object or noun")
