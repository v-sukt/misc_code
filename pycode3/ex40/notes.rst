Modules, Classes, and Objects
==============================

Modules can hold objects, classes, methods/functions.
They are useful to make your code look cleaner.

They are like dictionaries.

.. code-block:: python

    mystuff = {'apple': 'I AM APPLE'}

Module ``mystuff.py``:

.. code-block:: python

    def apple():
        print("I AM APPLE")

to get the apple from dict we use [key], whereas
to get the apple from module we use .key. e.g.

.. code-block:: python

    import mystuff as ms
    ms.apple()
    print(mystuff['apple'])

Classes are like **mini-modules**. When you *instantiate*/*create*
a class what you get is called an object. You instantiate (create) a
class by calling the class like it’s a function, like this:

for a class like:

.. code-block:: python

    class MyStuff(object):
        def __init__(self):
            some_var = 'someval'

        def method1(self, value):
            print("This will replace old value "
                  "of some_var with new one")
            self.some_var = value

    thing = MyStuff()
    print("Created with value :", thing.some_var)
    thing.method1(10)
    print("Current value :", thing.some_var)


Here’s why classes are used instead of modules:
    You can take this MyStuff class and use it
    to craft many of them, millions at a time
    if you want, and each one won’t interfere with
    each other. When you import a module there
    is only one for the entire program unless you
    do some monster hacks.


Something important to really know :

• Classes are like blueprints or definitions for creating new mini-modules.
• Instantiation is how you make one of these mini-modules and import it at the same time. “Instantiate” just means to create an object from the class.
• The resulting created mini-module is called an object, and you then assign it to a variable to work with it.

    **Important**

    The objects defined at the module level are available for once
    so could be used for static things. e.g. ``logging`` module has ``DEBUG``,
    ``ERROR`` etc. levels in current exercise there is ``hapy_bday`` object
    available at module level, unlike ``Song`` class which can create
    ``no. of objects``.