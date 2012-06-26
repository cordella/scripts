#/usr/bin/env python
from sys import argv

COLOURS = ('#red', '#orange', '#yellow', '#green', '#blue', '#indigo', '#purple')

def colourise(char, i):
    return COLOURS[i] + char

def rainbow(line):
    i = 0
    new_line = []
    for word in line.split(' '):
        new_line.append(colourise(word, i))
        i = (i + 1) % 7
    return ' '.join(new_line)

if __name__ == '__main__':

    line =  ' '.join(argv[1:])
    print(rainbow(line))
    
