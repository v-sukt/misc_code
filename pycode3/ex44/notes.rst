Inheritance vs Composition
=============================

**Inheritance** is when the class inherits from a parent so defined with

.. code-block:: python

    class ChildClass(BaseClass):

        def __init__(self):
            pass

So to provide the details to the Super's constructors, one can initialize it in Child's constructor.
as whenever a Child's *object* is initialized the parent's constructor is **auto-called**

Whereas in case **Composition**, we create the objects of some other classes inside the new class in
order to use them. This is defined with something like -

.. code-block:: python

    class ClassA(object):

        def __init__(self):
            pass


    class ClassB(object):

        def __init__(self):
            pass


    class NewClass(object):

        def __init__(self, valA, valB):
            self.obj_a = ClassA(valA)
            self.obj_b = classB(valB)


Some advice from author :

    Most of the uses of *inheritance* can be simplified or replaced with *composition*, and *multiple inheritance* should be avoided at all costs.

Now we'll see various things that these two provide.

providing the info to the parent from child
-----------------------------------------------
In *Inheritance* we know the parent's constructor (``__init__()`` method) is auto-called inside the child's constructor.
In some cases just getting the methods of parent is not sufficient, there needs to something passed onto the parent
while initializing the class object. Now that's done with a special method

::

    super(args_for_super_class)

This is invoked inside ``__init__()``

overriding method of in derived class
---------------------------------------

In *Inheritance* we know the parent's constructor (``__init__()`` method) is auto-called inside the child's constructor.
In some cases just having the access to methods of parent is not sufficient as it's implementation is different for each
subclass, so to create different implementation for each subclass we *use method with similar name in the child*, this way
the same named method from parent is overridden and so won't be called. (with exception to ``__init__()``)