Functions returning values
==========================

Functions can return values as seen in this exercise. It's just ``return`` followed by the value to return.

The ``return`` value is useful when

- Some operation needs to be repetitively done, so we make it's function and get the final result
- To perform some re-usable tests and use them as conditions in if (return ``True`` or ``False``)

It can be extended when we define custom data-types (``class``):
to support common operations (like addition, subtraction, etc)
on the data-type we need to add some additional functions.

Some common operations :

+------------------------+-----------------------------------+
| Construction           | Meaning                           |
+========================+===================================+
| a.__init__(self, args) | constructor: a = A(args)          |
+------------------------+-----------------------------------+
| a.__del__(self)        | destructor: del a                 |
+------------------------+-----------------------------------+
| a.__call__(self, args) | call as function: a(args)         |
+------------------------+-----------------------------------+
| a.__str__(self)        | pretty print: print a, str(a)     |
+------------------------+-----------------------------------+
| a.__repr__(self)       | representation: a = eval(repr(a)) |
+------------------------+-----------------------------------+
| a.__add__(self, b)     | a + b                             |
+------------------------+-----------------------------------+
| a.__sub__(self, b)     | a - b                             |
+------------------------+-----------------------------------+
| a.__mul__(self, b)     | a*b                               |
+------------------------+-----------------------------------+
| a.__div__(self, b)     | a/b                               |
+------------------------+-----------------------------------+
| a.__radd__(self, b)    | b + a                             |
+------------------------+-----------------------------------+
| a.__rsub__(self, b)    | b - a                             |
+------------------------+-----------------------------------+
| a.__rmul__(self, b)    | b*a                               |
+------------------------+-----------------------------------+
| a.__rdiv__(self, b)    | b/a                               |
+------------------------+-----------------------------------+
| a.__pow__(self, p)     | a**p                              |
+------------------------+-----------------------------------+
| a.__lt__(self, b)      | a < b                             |
+------------------------+-----------------------------------+
| a.__gt__(self, b)      | a > b                             |
+------------------------+-----------------------------------+
| a.__le__(self, b)      | a <= b                            |
+------------------------+-----------------------------------+
| a.__ge__(self, b)      | a => b                            |
+------------------------+-----------------------------------+
| a.__eq__(self, b)      | a == b                            |
+------------------------+-----------------------------------+
| a.__ne__(self, b)      | a != b                            |
+------------------------+-----------------------------------+
| a.__bool__(self)       | boolean expression, as in if a:   |
+------------------------+-----------------------------------+
| a.__len__(self)        | length of a (int): len(a)         |
+------------------------+-----------------------------------+
| a.__abs__(self)        | abs(a)                            |
+------------------------+-----------------------------------+

So for equality operation we can have function like:

.. code-block:: python

    class ...
        def __eq__(self, obj):
            """function to check equality of two objects"""
            if something:
                return True
            else:
                return False


NOTE: The return value is not necessarily a single value, you can send multiple
values in return - but if they are just comma ',' separated values, you get a tuple
with those values:

.. code-block:: python

    In[2]: def ting(val):
     ... :     return val, val+1, val+2
     ... :
    ting(2)
    Out[3]: (2, 3, 4)
    type(ting(2))
    Out[4]: tuple

