#/usr/bin/env python
from sys import argv

COLOURS = ('#red', '#orange', '#yellow', '#green', '#blue', '#indigo', '#purple')

def colourise(char, i):
    return COLOURS[i] + char

def rainbow(line):
    i = 0
    new_line = ''
    for char in line:
        if char.isspace():
            new_line += char
        else:
            new_line += colourise(char, i)
            i = (i + 1) % 7
    return new_line

if __name__ == '__main__':

    line =  ' '.join(argv[1:])
    print(rainbow(line))
    
