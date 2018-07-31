#!/usr/bin/env python2.7
'''Summarises the keywords, Data-types, Operators, String formatters in Python'''

def keywords_list():
    """pydoc has the description of keywords and function prints the list of them 
    and - python and operator logical and
    del - delete the reference to an object | like variable/function/module/class/element of list
    from - used to import modules into current namespace from...import - import selective from module
    not - logical not operator ! negation
    while - the loop : while condition: expressions
    as - for creating alias while importing : import urllib as ulb
    elif - else if under if statement blocks
    global - used to define a global variable insdie a function
    or - logical or operator
    with - to enclose the execution of block of code within method of context manager (a class with __enter__ and __exit__ methods). At finish of block 
           the __exit__ is called automatically e.g. file class
           with open("ex13.py", w) as my_file:
               my_file.write("some random text!!\n")
           my_file.write("some more")  #fails to execute as the file is already closed at end of with block
    assert - used to check assumptions/assertions, this can be used for the debugging the code logic
                     assert condition, message 
            the condition is executed and if it's wrong the message is displayed with AssertionError
                a = 5
                assert a < 6 #no errors generated
                assert a < 4 #exception is generated for this
    else - for non matching section of if statement
    if - for testing the condition if condition: statements
    pass - it's null statement in python, much like : of bash, nothing happens. Useful instead blank line of code
    yield - yield is used inside a function like a return statement. But yield returns a generator. Generator is 
            an iterator that generates one item at a time. A large list of value will take up a lot of memory. Generators 
            are useful in this situation as it generates only one value at a time instead of storing all the values in memory. 
         For example,
            >>> g = (2**x for x in range(100))
          will create a generator g which generates powers of 2 up to the number two raised to the power 99. We can generate 
          the numbers using the next() function as shown below.
            >>> next(g)
            1
            >>> next(g)
            2
            >>> next(g)
            4
            >>> next(g)
            8
            >>> next(g)
            16
          And so on... This type of generator is returned by the yield statement from a function. Here is an example.
   
            def generator():
                for i in range(6):
                    yield i*i
    
            g = generator()
            for i in g:
                print(i)
    
            Output
            0
            1
            4
            9
            16
            25

    break - used to break the execution of while/for loop
    except - holds the block of try-except to be executed if the exception is caught
    import - to import modules
    print - print the text
    class - to define a class 
    exec - function used to execute a string python code
    in - in operator to check if the object on left is in the object in right x in y
    is - operator that returns if two names are references to the same object
          a = 55
          b = a   #just a new reference to object location containing 55 check with id(a), id(b)
          a is b -> True
          c = 55
          a is c -> False
          a == c -> True
    return - to return the values of function 
    def - to define functions def function_name(arguments): statements
    for - used for looping
    lambda - creates and returns an inline function which is evaluated
               a = lambda x: x*2
               for i in range(1,6):
                  print a(i)    #will print the 2,4,6, etc
    try: used as a part of try..catch block usually to ensure the programs doesn't get abruptuly exeited showing exceptions - or to handle when unexpected values are provided by user, etc. 

    """
    keywords = ["and", "del", "from", "not", "while", "as", "elif", "global", 
                "or", "with", "assert", "else", "if", "pass", "yield",
                "break", "except", "import", "print", "class", "exec",
                "in", "raise", "continue", "finally", "is", "return", 
                "def", "for", "lambda", "try" ]
    print "Keywords\n", keywords

def data_types():
    """ The basic data types in python are 
    string - any character/string - default return of raw_input()
    float - floatig point numbers - real values 2.3333 like
    numbers - int or long type 
    lists - the arrays of python, [] enclosed
    dictionary - list of the key value pairs, {} enclosed
    tuple - ordered, immutable collection, enclosed in ()
    binary - True or False
    None - this is always false, null value 'None' keyword
    python being object oriented as many classes that many data-types :)
    """
    data_types = ["string", "numbers", "floats", "lists", 
                 "dictionaries", "tuple", "set", "None"]
    print "Data Types\n", data_types

def string_formats():
    """ The formatting strings that can be used with print, etc (String Formatting operations)
    %d/%i - digit/numbers signed integer
    %u - unsigned decimal
    %s - string - calls str() of the class
    %x - hexadecimal 
    %o - octal 
    %e/%E - Floating point exponential format
    %g/%G - Same as "e" if exponent is greater than -4 or less than precision, "f" otherwise
    %c - single character (integer or character)
    %r - raw : repr() presentation of object 
    """
    print "String Formatting operators\n", r"%d %i %u, %x %o, %e %E %g %G, %f %F, %c %s %r"
   

def operator_list():
    """ Various operators in python:
    + - * / - you know these
    ** - exponential / power
    // - floor division, the result is whole number on left side of number line
    % - modulo operator - provides reminder of division
    < > <= >= == != <>(deprecated not equal) - comparison operators mean as they represent
    @ - matrix multiplication operator
    : - slicing operator string[3:9]
    . - attribute reference a.attribute
    +=, -=, *=, /=, //=, **=, %= - augmented assignment operators do operation and assign the new value to the variable
    
    BITWISE
    << - (x << y) Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y. 
    >> - (x >> y) Returns x with the bits shifted to the right by y places. This is the same as //'ing x by 2**y. 
    & - (x & y)  Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0. 
    | - (x | y)  Does a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1. 
    ~ - (~ x) Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. This is the same as -x - 1. 
    ^ - (x ^ y)  Does a "bitwise exclusive or". Each bit of the output is the same as the corresponding bit in x if that bit in y is 0, and it's the complement of the bit in x if that bit in y is 1. 
    """
    print "Operators\n", r"+ - * / ** // % < > @  : . +=  <<  >>  & | ~ ^"

if __name__ == "__main__":
    keywords_list()
    data_types()
    string_formats()
    operator_list()
else:
    print "functions imported:\n keywords_list()\ndata_types()\nstring_formats()\noperator_list()\n"

