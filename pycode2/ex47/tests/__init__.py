"""The ex47 project test modules. 

Some guidelines for tests:
    1. Test files go in tests/ and are named BLAH_tests.py; otherwise nosetests won't run them. This also keeps your 
       tests from clashing with your other code.
    2. Write one test file for each module you make.
    3. Keep your test cases (functions) short, but do not worry if they are a bit messy. Test cases are usually kind of
       messy.
    4. Even though test cases are messy, try to keep them clean and remove any repetitive code you can. Create helper 
       functions that get rid of duplicate code. You will thank me later when you make a change and then have to change 
       your tests. Duplicated code will make changing your tests more difficult.
    5. Finally, do not get too attached to your tests. Sometimes, the best way to redesign something is to just delete it
       and start over.

Doctests:

    Module showing how doctests can be included with source code
    Each '>>>' line is run as if in a python shell, and counts as a test.
    The next line, if not '>>>' is the expected output of the previous line.
    If anything doesn't match exactly (including trailing spaces), the test fails.

     def multiply(a, b):
        \"""
        >>> multiply(4, 3)
        12
        >>> multiply('a', 3)
        'aaa'
        \"""
        return a * b

    This can be separated from the code as one needs the python documentation for the code writte. 
    e.g. another .txt file which does everything from importing the module to running the tests

    sample_tests.txt |
    
        This is a doctest based regression suite for unnecessary_math.py
        Each '>>' line is run as if in a python shell, and counts as a test.
        The next line, if not '>>' is the expected output of the previous line.
        If anything doesn't match exactly (including trailing spaces), the test fails.
         
        >>> from unnecessary_math import multiply
        >>> multiply(3, 4)
        12
        >>> multiply('a', 3)
        'aaa'
"""