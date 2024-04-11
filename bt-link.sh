btdir=/var/lib/bluetooth
adapter=$(ls $btdir)
cd "$btdir/$adapter"
ls .
