import sys
from pathlib import Path


def main(language_file, encoding, errors):
    line = language_file.readline()
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)
    else:
        pass


def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    print(raw_bytes, "<====>", cooked_string)


script, encoding, error = sys.argv
filename = Path(script + '/' + 'languages.txt')

if filename.exists() and not filename.stat().st_size == 0:
    languages = filename.open(encoding="utf-8")
else:
    from urllib import request
    f = request.urlopen("https://learnpythonthehardway.org/python3/languages.txt")
    filename.open("w+b").write(f.read1())
    languages = filename.open(encoding="utf-8")

main(languages, encoding, error)
filename.unlink()
