'''Here tests are run so all functions that start with test_ are executed. 
nose.tools.assert_equal() method, checks if both arguments passed to it are same'''

from nose.tools import *
from ex48_project import lexicon, parser

def test_directions():
    assert_equal(lexicon.scan('north'), [('direction', 'north')])
    result = lexicon.scan('north south east')
    assert_equal(result, [('direction', 'north'),
                            ('direction', 'south'),
                            ('direction', 'east')])

def test_verbs():
    assert_equal(lexicon.scan('go'), [('verb','go')])
    result = lexicon.scan('go kill eat')
    assert_equal(result, [('verb','go'),
                            ('verb','kill'),
                            ('verb','eat')])

def test_stops():
    assert_equal(lexicon.scan('the'),[('stop','the')])
    result = lexicon.scan('the in of')
    assert_equal(result, [('stop','the'),
                            ('stop','in'),
                            ('stop', 'of')])

def test_nouns():
    assert_equal(lexicon.scan('bear'), [('noun','bear')])
    result = lexicon.scan("3 91234")
    assert_equal(result, [ ('number', 3),
                           ('number', 91234) ])

def test_errors():
    assert_equal(lexicon.scan('ASDFADFASDF'), [('error', "ASDFADFASDF")])
    result = lexicon.scan('bear IAS princess')
    assert_equal(result, [('noun','bear'),('error','IAS'),('noun','princess')])

def test_parser_verb():
    """test the parser for verb, object, subject then for sentence with subject start and verb start"""
    # single word sentence
    assert_equal( parser.parse_verb( lexicon.scan('go') ), ('verb', 'go')) # verb test

def test_parser_object():
    assert_equal( parser.parse_object( lexicon.scan('south')), ('direction', 'south') ) # direction check
    assert_equal( parser.parse_object( lexicon.scan('princess')), ('noun','princess')) # noun check

def test_parser_subject():
    result = parser.parse_subject( lexicon.scan('go south'), ('noun', 'player'))
    assert_equal( result, parser.Sentence(('noun', 'player'), 
                                    ('verb','go'), 
                                    ('direction','south')))

def test_parser_sentence():
    result = parser.parse_sentence( lexicon.scan("the princess go south") )
    expected = parser.Sentence(('noun','princess'),('verb','go'),('direction','south'))
    assert_equal(result, expected)

def test_parser_errors():
    assert_raises(parser.ParserError,parser.parse_verb, lexicon.scan("something go"))
    assert_raises(parser.ParserError,parser.parse_object, lexicon.scan("something princess"))
    assert_raises(parser.ParserError,parser.parse_subject, lexicon.scan("something south"), ('noun','princess'))
    #try:
    #    result = parser.parse_sentence( lexicon.scan("new princess go south") )
    #except parser.ParserError:
    #    return True
    # Use assert_raises for excception catching and comparison but takes Exception type, the callable 
    # arguments
    assert_raises(parser.ParserError,parser.parse_sentence,lexicon.scan("new princess go south"))

