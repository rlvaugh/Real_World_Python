"""Read a text file and return a list of strings."""

def text_to_string(filename):
    strings = []
    with open(filename) as f:
        strings.append(f.read())
    return '\n'.join(strings)
