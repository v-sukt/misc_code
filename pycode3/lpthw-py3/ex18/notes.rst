multi-arguments for functions
-----------------------------
We can provide multiple arguments to the function. If we are not sure about
the number of arguments, we can use ``function(*args)`` parameters.

We can define functions with only underscore.

.. code-block:: python

    def _(*args):
        print("The arguments received :", args)

The ``*`` from ``*argc``: Tells Python to take all the arguments to the
function and then put them in args as a list.
