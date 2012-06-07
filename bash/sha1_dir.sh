#!/bin/sh
#
# Outputs to stdout the output from sha1sum for each file in
# the directory specified on the command line.

EWD=$1
exec find $EWD -type f -print0 | sort -z | xargs -0 sha1sum -b

