#!/bin/sh
#
# Makes a file.sha1 with the output from sha1sum for one file
# specified on the command line.

FILETOSUM=$1

sha1sum -b $FILETOSUM > $FILETOSUM.sha1
sha1sum -c $FILETOSUM.sha1
