copying file's contents
=======================

The file contents can be read all-at-once or a section-at-a-time.

.. code-block:: python

    def copy_file(from_file, to_file):
        """Reads from first file and writes to the
        outfile all-at-once"""
        with open(from_file) as in_file, open(to_file, 'w+') as out_file:
            out_file.write(in_file.read())


    def copy_file_part(from_file, to_file, buffer):
        """Reads from first file and writes to the outfile
        one-buffer-byte-at-a-time"""
        try:
            with open(from_file) as in_file, open(to_file, 'w+') as out_file:
                data = in_file.read(buffer)
                count = 1  # this can be removed - just prints the
                while len(data):
                    out_file.write(data)
                    data = in_file.read(buffer)
                    count += 1
            print(count)
            return count
        except:
            return None

This way we can work on files without filling everything into the memory