#!/bin/bash
#This script will list the files in a directory, along with outputting that list to a file
#Filename: filelist.sh
#Don't forget to chmod +x on this file!

#Setting variables
location=$1  #First variable, this will specify the directory the script runs against
filename=$2  #Second variable, this will specify what the file name should be

if [ -z "$location" ]
then
        echo "ERROR, Missing Argument: Please provide a location argument"
        exit 0 #A graceful exit
fi

if [ -z "$filename" ]
then
        echo "ERROR, Missing Argument: Please provide a filename"
        exit 0 #A graceful exit
fi

ls $location > $filename
echo "Script is complete and has indexed the $location"
echo "################"  #Only for formatting on screen
echo "Displaying contents of $filename"
echo "################"
cat $filename
