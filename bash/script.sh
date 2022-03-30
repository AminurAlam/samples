#!/usr/bin/env bash

#single line comment

: << 'COMMENT'
    multiline comment
    write anything here
COMMENT



###printing something
#    -n    do not output the trailing newline
#    -e    enable interpretation of backslash escapes
#    -E    disable interpretation of backslash escapes (default)
echo "hello world!"
echo "i'm printing
multiple lines"
echo -e "\n"



###variables
STR="string"
NUM1=5
NUM2=7

#printing variables
echo $STR $NUM1         # works without quotes
echo "$STR $NUM1"       # works with double quotes
echo '$STR $NUM1'       # doesnt work with single quotes

echo $NUM1+$NUM2        # addition doesnt work
echo $(($NUM1+$NUM2))   # it works now



###loops

#while loop
NUM=1
while [ $NUM -le 10 ] ; do
	echo -n $NUM
	((++NUM))
done

#until loop
NUM=1
until [ $NUM -gt 10 ] ; do
	echo -n $NUM
	let NUM+=1
done
	
#for loop
for NUM in {1..10} ; do
	echo -n $NUM
done



###statments

#if statement
if [ true ] ; then
	echo -e "\nTRUE"
else
	echo -e "\nFALSE"
fi



###function

callme() {
	echo "Hello, $1"
}

callme "John Doe"
