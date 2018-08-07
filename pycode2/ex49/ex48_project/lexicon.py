"""The word scanner function and definition of words- returns a list of tuples in (type, word) form"""
game_lexicon = {'direction': ['north','south','east','west','down','up','left','right','back'],
                'verb' : ['go','stop','kill','eat'],
                'stop' : ['the','in','of','from','at','it'],
                'noun': ['door','bear','princess','cabinet']
                }

def scan(line):
    '''The function takes the value of line -a string. Splits them into words
    and scans the game_lexicon appending the matching tuple to the setense and returns a list of tuples'''
    words = line.split()
    sentence = []
    for word in words:
        found = False
        for key in game_lexicon.keys():
        
            try:        
                if word.lower() in game_lexicon[key]:
                    found = True
                    break
                elif int(word)%1 == 0:
                    key, word = 'number', int(word)
                    found = True
                    break
                else:
                    pass
                    
            except:
                None

        if found:
            sentence.append((key, word))
        else:
            sentence.append(('error',word))
        
    return sentence
