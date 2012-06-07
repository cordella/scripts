#!/bin/bash
#
# Command line accepts files and compresses them with various programs.
# Will probably rewrite in Python for expansion.

NO_ARGS=0
E_OPTERROR=85

if [ $# -eq "$NO_ARGS" ]    # Script invoked with no command-line args? Exit.
then
  echo "Must provide files to compress!"
  exit $E_OPTERROR
fi

failure() {
    echo -e \\n"Compression failed! Exiting."
    exit 1
}

compressions() {
    echo -e \\n"Operating on ${ARG}"

    ARG_EXT=`echo "${ARG}" | awk -F . '{print $NF}'`
    FOUND="Target file is in"
    FOUND2="format, skipping."

    case "$ARG_EXT" in
    [gG][zZ])
        echo "$FOUND gzip $FOUND2"
        return 6 ;;
    [bB][zZ]2)
        echo "$FOUND bzip2 $FOUND2"
        return 6 ;;
    [rR][zZ])
        echo "$FOUND rzip $FOUND2"
        return 6 ;;
    [xX][zZ])
        echo "$FOUND xz $FOUND2"
        return 6 ;;
    esac
    
    echo -e \\n"Compressing with gzip --best -c"
    gzip --best -c "${ARG}" > "${ARG}.gz" && echo -ne "Done! " || ( if [ -w "${ARG}.gz" ];
        then rm "${ARG}.gz"; fi && failure )

    echo "Compressing with bzip2 --best -k"
    bzip2 --best -k "${ARG}" && echo -n "Done! " || failure

    echo "Compressing with rzip -9k"
    rzip -9k "${ARG}" && echo -n "Done! " || failure

    echo "Compressing with xz -zk9e"
    xz -zk9e "${ARG}" && echo -e "Done!"\\n || failure

    stat -c "%s %n" "${ARG}"* | sort -n | head -1 | cut -s -d " " -f 2 | sed 's/$/ won! Delete other files?/'
    echo -n "(y/n)> "

    read ANSWER
    case "$ANSWER" in
    *[yY]|*[yY][eE][sS]*)
        stat -c "%s %n" "${ARG}"* | sort -n | tail -n +2 | cut -s -d " " -f 2 | xargs rm && echo "Deletion successful."
        return 0 ;;
    *) echo "Not deleting.";;
    esac

    unset ANSWER
    echo -ne "Delete compressed versions?\\n(y/n)> "

    read ANSWER
    case "$ANSWER" in
    *[yY]|*[yY][eE][sS]*)
        stat -c "%n" "${ARG}".* | xargs rm && echo "Deletion successful."
        return 0 ;;
    *) echo "Not deleting."; return 1 ;;
    esac

}

for ((i = 1; i <= "$#"; i++))
do
    eval ARG=\$$i
    if [ -d "${ARG}" ]; then
        echo -e \\n"ERROR: "${ARG}" is a directory, cannot compress."
    elif [ -r "${ARG}" ]; then
        compressions
    else
        echo -e \\n'"${ARG}": not a valid target!'
    fi
done

echo -e \\n"Processed all target files. Exiting."
