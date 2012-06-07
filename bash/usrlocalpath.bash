#!/bin/bash
#
# Used for loading manually compiled and installed programs in separate
# subdirectories of /usr/local into the PATH, e.g. /usr/local/rzip/current/bin

NEWPATH="$PATH"

if [ -d "/usr/local/" ] && [ -r "/usr/local/" ]; then
    for BINDIR in /usr/local/*/current/bin; do
        [ -d "$BINDIR" ] && [ -r "$BINDIR" ] && NEWPATH="$NEWPATH:$BINDIR"
    done
    for BINDIR in /usr/local/*/current/sbin; do
        [ -d "$BINDIR" ] && [ -r "$BINDIR" ] && NEWPATH="$NEWPATH:$BINDIR"
    done
    unset BINDIR
fi

if [ "$PATH" != "$NEWPATH" ]; then
    PATH="$NEWPATH"
    export PATH
    unset NEWPATH
fi
