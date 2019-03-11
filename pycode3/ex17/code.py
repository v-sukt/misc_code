"""simple example to copy a file into another"""
from sys import argv
from os.path import exists


def copy_file(from_file, to_file):
    """Reads from first file and writes to the outfile
    all-at-once"""
    with open(from_file) as in_file, open(to_file, 'w+') as out_file:
        out_file.write(in_file.read())


def copy_file_part(from_file, to_file, buffer):
    """Reads from first file and writes to the outfile
    one-buffer-byte-at-a-time in binary mode"""
    try:
        with open(from_file, "r+b") as in_file, open(to_file, 'w+b') as out_file:
            data = in_file.read(buffer)
            count = 1  # this can be removed - just prints the
            while len(data):
                out_file.write(data)
                data = in_file.read(buffer)
                count += 1
        print(count)
        return count
    except OSError:
        return None


if __name__ == '__main__':
    script, from_file, to_file = argv
    print(f"Copying from {from_file} to {to_file}.")

    # indata = open(from_file).read()
    in_file = open(from_file)
    indata = in_file.read()

    print(f"The input file is {len(indata)} bytes long.")
    print(f"Does the output file exists? {exists(to_file)}")
    print("Ready, hit RETURN to continue, CTRL-C to abort.")
    input()

    # open(to_file, 'w').write(indata)
    out_file = open(to_file, 'w')
    out_file.write(indata)

    print("Alright, all done.")

    out_file.close()
    in_file.close()
