Opening File
------------

    Opening a file is very easy operation. you just need to use open(filename) to open the file.
    When opened, you get something like a file descriptor, which can then be used to read the file
    contents, etc.

    Some useful methods for file object - readlines(), read(), seek(), tell(), write(), writelines(), truncate()
    and info in mode, name, buffer, closed, errors, encoding

    While opening file that is too large, it'll load everything in memory. So better provide the size argument to
    open() and process on the section loaded, then we can load rest of the section :

    .. code-block:: python

            with open("log.txt") as infile:
                for line in infile:
                    do_something_with(line)

