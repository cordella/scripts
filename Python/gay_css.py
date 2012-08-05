#/usr/bin/env python
from sys import argv, exit, stdin
from re import sub
import getopt

COLOURS = ('#red', '#orange', '#yellow', '#green', '#blue', '#indigo', '#purple')
SENTINEL = '\\x000000'
CUTOFF = 127

def parse_args():
    args = {}
    usage_str = 'usage: ' + argv[0] + ' [-h] [-wcr] [-n #] [-l #]'
    help_str = usage_str
    try:
        optlist = getopt.getopt(argv[1:], 'hn:wl:cr')[0]
    except getopt.GetoptError, err:
        print(str(err))
        print(usage_str)
        exit(2)

    args['use_word'] = False
    args['use_cycle'] = False
    args['rev_cycle'] = False
    args['offset'] = 0
    args['limit'] = CUTOFF
    for o, a in optlist:
        if o == '-h':
            print(help_str)
            exit(-1)
        elif o == '-n':
            args['offset'] = check_if_int(a)
        elif o == '-w':
            args['use_word'] = True
        elif o == '-l':
            args['limit'] = check_if_int(a)
        elif o == '-c':
            args['use_cycle'] = True
        elif o == '-r':
            args['rev_cycle'] = True
        else:
            assert False, "unhandled option"
    return args


def check_if_int(s):
    try:
        return int(s)
    except ValueError:
        return 0


#def chunks(a, n):
#    for i in range(0, len(a), n):
#        yield a[i:i+n]


def prepare_lines(line, limit=0, per_word=False):
    if per_word is False:
        #temp_gen = ''.join((SENTINEL + char).replace(SENTINEL + ' ', ' ') for char in line)
        temp_gen = (''.join((SENTINEL + char) for char in word) for word in line.decode('utf8').split())
    else:
        temp_gen = (SENTINEL + word for word in line.decode('utf8').split())
    temp_gen = (l.encode('utf8') for l in temp_gen)

    if limit <= 0:
        temp_list = (' '.join(temp_gen),)
    else:
        temp_list = [temp_gen.next()]
        index = 0
        for word in temp_gen:
            if len(temp_list[index] + word) > limit:
                index += 1
                temp_list.append(word)
            else:
                temp_list[index] += ' ' + word
    
    return temp_list


#def colourise(char, i):
#    return COLOURS[i] + char


def rainbow(line, offset):
    i = offset % 7
    while line.find(SENTINEL) != -1:
        line = line.replace(SENTINEL, COLOURS[i], 1)
        i = (i + 1) % 7
    return line
    
def main(args):
    in_text = sub('\\x1b\[.', '', raw_input())
    if in_text.isspace() or in_text == '':
        return
    text = prepare_lines(in_text, args['limit'], args['use_word'])
    for line in text:
        print(rainbow(line, args['offset']))
        if args['use_cycle'] and not args['rev_cycle']:
            args['offset'] += 1
        elif args['use_cycle'] and args['rev_cycle']:
            args['offset'] -= 1
    print('\n')


if __name__ == '__main__':
    args = parse_args()

    print('CS:S Rainbow Command Console loaded.')
    print('''
    Settings
    --------\n
    Initial colour: %s
    Line limit: %s bytes
    Per word: %s
    Cycle initial colour: %s
    Reverse cycle: %s
    ''' % (
        COLOURS[args['offset'] % 7].replace('#', '').title(),
        'Infinity' if args['limit'] <= 0 else args['limit'],
        args['use_word'], args['use_cycle'], args['rev_cycle'])
    )
    print('Enter your message and press return to colour it.\nPress ctrl-c to exit.\n')
    
    try:
        while True:
            main(args)
    except KeyboardInterrupt:
        exit(0)