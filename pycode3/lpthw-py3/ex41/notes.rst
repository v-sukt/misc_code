Object-Oriented Jargon
========================

World usage
-------------
``class``
    Tell python to make new type of thing.
object
    Two meanings: [ the most basic type of thing | an instance of something ].
instance
    What you get when you tell python to create a ``class``.
``def``
    how you define a function inside a ``class``.
``self``
    Inside the function in a class, self is a variable for the instance/object being accessed.
inheritance
    The concept that one class can inherit traits from another class, much like child and parent.
composition
    The concept that a class can be composed of other classes as parts, much like how car has wheels.
attribute
    A property classes have that are from composition and are usually variables.
is-a
    A phrase to say that something inherits from another, as in Krisna is-a Gopa
has-a
    A phrase to say that something is composed of other things or has a trait, as in Krishna has-a Flute.


How to read Python Snippets
-------------------------------
* Make a class named X that is-a Y

.. code-block:: python

    class X(Y)

- ``class`` X has-a ``__init__`` that takes self and J parameters

.. code-block:: python

    class X(object):

        def __init__(self, J):


* ``class`` X has-a function named M that takes ``self`` and J parameters.

.. code-block:: python

    class X(object):

        def M(self, J):

* Set foo to an instance of class X.

.. code-block:: python

    foo = X()

* From foo, get the M function, and call it with parameters ``self``, ``J``. Note: self is not visible argument, but it's in use

.. code-block:: python

    foo.M(J)

* From foo, get the K attribute, and set it to Q.

.. code-block:: python

    foo.K = Q

