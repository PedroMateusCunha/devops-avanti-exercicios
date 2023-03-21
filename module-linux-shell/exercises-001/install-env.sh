#!/bin/bash

directory="diretorio-generico"
file_name="arquivo-generico"


mkdir -p /tmp/$directory{,-link}
touch /tmp/$directory/$file_name-{1..10}.txt
chmod 664 /tmp/$directory/$file_name-{1..10}.txt

touch /tmp/$directory/$file_name-777-{1..10}.txt
chmod 777 /tmp/$directory/$file_name-777-{1..10}.txt

touch /tmp/$directory-link/$file_name-original-soft.txt
touch /tmp/$directory-link/$file_name-original-hard.txt
chmod 777 -R /tmp/$directory-link
touch /tmp/$directory-link/$file_name-original.txt

ln -d /tmp/$directory-link/$file_name-original-hard.txt /tmp/$directory/$file_name-777-hard.txt
ln -d /tmp/$directory-link/$file_name-original.txt /tmp/$directory/$file_name-hard.txt
ln -s /tmp/$directory-link/$file_name-original-soft.txt /tmp/$directory/$file_name-777-soft.txt
ln -s /tmp/$directory-link/$file_name-original.txt /tmp/$directory/$file_name-soft.txt
