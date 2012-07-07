#/usr/bin/env python
#from sys import argv
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--offset', dest='offset', type=int, default=0, help='offset the first colour of the rainbow')
    parser.add_argument('-w', '--word', action='store_true', dest='use_word', help='use per-word mode')
    parser.add_argument('text', help='the text to rainbow')

    return parser.parse_args()


COLOURS = ('#red', '#orange', '#yellow', '#green', '#blue', '#indigo', '#purple')

def colourise(char, i):
    return COLOURS[i] + char

def rainbow(line, offset):
    i = (0 + offset) % 7
    count = 0
    new_line = ''
    for char in line:
        if char.isspace():
            new_line += char
        else:
            new_line += colourise(char, i)
            count += 1
            i = (i + 1) % 7
    return (new_line, count)


def rainbow_word(line, offset):
    i = (0 + offset) % 7
    count = 0
    new_line = []
    for word in line.split(' '):
        new_line.append(colourise(word, i))
        count += 1
        i = (i + 1) % 7
    return (' '.join(new_line), count)

if __name__ == '__main__':
    args = parse_args()

    if args.use_word == True:
        rainbow_func = rainbow_word
    else:
        rainbow_func = rainbow
    text, count = rainbow_func(args.text, args.offset)
    print(text)
    print(len(args.text) + count*8)
