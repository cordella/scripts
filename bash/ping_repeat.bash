i=1; a=1+1+1+1+1
HOSTNAME=$1
ping $HOSTNAME

while [ $? != 0 ]; do
    sleep 1;
    if [ $i == $a ]; then
        echo
        i=1
    else
        i=$i+1
    fi
    ping $HOSTNAME
done
