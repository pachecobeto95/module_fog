#! /bin/bash
python write_file.py $1 $2
scp ./params.txt pi@192.168.0.1:/home/pi
rm ./params.txt

