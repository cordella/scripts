#!/bin/sh
#
# sprunge(1)                          SPRUNGE                          sprunge(1)
#
# NAME
#     sprunge: command line pastebin:
#
# SYNOPSIS
#     <command> | curl -F 'sprunge=<-' http://sprunge.us
#
# DESCRIPTION
#     add ?<lang> <http://pygments.org/docs/lexers/> to resulting url for line numbers and syntax highlighting
#
# EXAMPLES
#     ~$ cat bin/ching | curl -F 'sprunge=<-' http://sprunge.us
#        http://sprunge.us/VZiY
#     ~$ firefox http://sprunge.us/VZiY?py#n-7
#
# SEE ALSO
#     http://github.com/rupa/sprunge
#

curl -F 'sprunge=<-' http://sprunge.us

