Reading and Writing Files
-------------------------
There are fre useful commands that you can use with the file objects
like ones below:

- ``close()`` : You know this, to close the file.

    Has no effect if the file is closed. So can be safely used
    specially with *recursion with open file*

- ``read(size)``: Reads the contents of the file matching size in ``bytes`` (no. of characters). You can assign the result to a variable.

   if there is no size or is negative reads till EOF

- ``readline()``: Reads just one line of a text file (till newline or till EOF).
- ``truncate()``: Empties the file. Watch out if you care about the file.
- ``write('stuff')``: Writes “stuff” to the file.
- ``seek(0)``: Moves the read/write location to the beginning of the file.

The last code block can be written as :

.. code-block:: python

    line1 = input("line 1: ")
    line2 = input("line 2: ")
    line3 = input("line 3: ")
    print("I'm going to write these to the file.")

    target.write(line1)
    target.write("\n")
    target.write(line2)
    target.write("\n")
    target.write(line3)
    target.write("\n")

With reformatting :

.. code-block:: python

    lines = []
    lines.append(input("line 1:") + "\n")
    lines.append(input("line 2:") + "\n")
    lines.append(input("line 3:") + "\n")
    target.writelines(lines)

File open modes
===============
There are following modes available

+-------------+-----------------------------------------------------------------+
| Character   | Meaning                                                         |
+=============+=================================================================+
| 'r'         | open for reading (default)                                      |
+-------------+-----------------------------------------------------------------+
| 'w'         | open for writing, truncating the file first                     |
+-------------+-----------------------------------------------------------------+
| 'x'         | open for exclusive creation, failing if the file already exists |
+-------------+-----------------------------------------------------------------+
| 'a'         | open for writing, appending to the end of the file if it exists |
+-------------+-----------------------------------------------------------------+
| 'b'         | binary mode                                                     |
+-------------+-----------------------------------------------------------------+
| 't'         | text mode (default)                                             |
+-------------+-----------------------------------------------------------------+
| '+'         | open a disk file for updating (reading and writing)             |
+-------------+-----------------------------------------------------------------+

- Default mode is ``rt``
- ``w+b`` opens and truncates the file to 0 bytes
- ``r+b`` opens the file without truncation
- ``w+``, ``r+``, and ``a+`` opens file in read and write mode

    The position in file will be different depending on the character used

