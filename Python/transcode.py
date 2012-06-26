#!/usr/bin/env python
#
# Version-agnostic transcoder for text files.
from sys import version_info, stdin, stdout, stderr, exit

def transcode(text, in_enc, out_enc, force=False):
    """ Transcode a string from one standard encoding to another.
    Python's standard encodings are defined at http://docs.python.org/py3k/library/codecs.html#standard-encodings

    """

    from codecs import lookup
    #return text.decode(in_enc).encode(out_enc)

    # If the input is ASCII, treat it as UTF-8
    ASCII_CODEC = lookup('ascii')
    decoder = lookup(in_enc)
    decoder = lookup('utf-8') if decoder == ASCII_CODEC else decoder

    encoder = lookup(out_enc)

    if encoder == decoder and force == False:
        stderr.write('input and output codecs are the same; not transcoding\n')
        return text
    else:
        return encoder.encode(decoder.decode(text)[0])[0]


if __name__ == '__main__':
    """ Implements the above transcode function as a fully functional command line program. """
    import argparse
    from chardet import detect
    from os.path import expanduser, exists, isfile, isdir

    if version_info[0] == 3:
        stdin_input = stdin.buffer.read
        stdout_output = stdout.buffer.write
    else:
        stdin_input = stdin.read
        input = raw_input
        stdout_output = stdout.write

    def write_out_file(out_file, text):
        open(out_file, 'wb').write(text)
        stderr.write('\noutput written to ' + args.out_file + '\n')

    def parse_args():
        """ Set up, and return the results of, the argument parser. """
        parser = argparse.ArgumentParser(add_help=False, usage='%(prog)s [options] [encodings] input-file')
        encodings = parser.add_argument_group(title='encodings <http://docs.python.org/py3k/library/codecs.html#standard-encodings>')
        optional = parser.add_argument_group(title='options')

        encodings.add_argument('-d', '--decode-from', metavar='CODEC', dest='in_enc', default='detect', help='input encoding (default: detect); note: ASCII is treated as UTF-8')
        encodings.add_argument('-e', '--encode-to', metavar='CODEC', dest='out_enc', default='utf-8', help='output encoding (default: utf-8)')

        optional.add_argument('-h', '--help', action='help', help='print this help and exit')
        optional.add_argument('-i', '--input', metavar='FILE', dest='in_file', default='/dev/stdin', help='the text file to transcode (default: - for stdin)')
        optional.add_argument('-o', '--output', metavar='FILE', dest='out_file', default='/dev/stdout', help='output file (default: stdout)')
        optional.add_argument('-f', '--force', action='store_true', dest='force_enc', help='force transcode if input and output encodings are the same')
        optional.add_argument('-y', '--yes', action='store_true', dest='force_write', help='always overwrite existing output files')

        return parser.parse_args()


    args = parse_args()

    # Determine if the input is a file or stdin
    if args.in_file == '/dev/stdin' or args.in_file == '-':
        text = stdin_input()
    else:
        text = open(expanduser(args.in_file), 'rb').read()

    # Detect the input encoding if none is given
    if args.in_enc == 'detect':
        in_enc = detect(text)['encoding']
        stderr.write("\nchardet detected the '" + in_enc + "' encoding\n")
    else:
        in_enc = args.in_enc

    text_enc = transcode(text, in_enc, args.out_enc, args.force_enc)

    out_file = expanduser(args.out_file)
    if out_file == '/dev/stdout':
        stderr.write('\n')
        stdout_output(text_enc)
    elif isdir(args.out_file):
        stderr.write('\noutput path is a directory; no output written\n')
        exit(1)
    elif isfile(out_file):
        if args.force_write == True:
            write_out_file(out_file, text_enc)
        else:
            stderr.write('\noutput file exists\noverwrite? [y/N]: ')
            answer = input()
            print(answer)
            if answer.strip().lower() in ('y', 'yes', 'ye'):
                write_out_file(out_file, text_enc)
            else:
                stderr.write('no output written\n')
    else:
        write_out_file(out_file, text_enc)

