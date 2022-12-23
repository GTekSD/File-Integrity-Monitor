
#find * -exec md5sum {} \; > hash_original                                                                                                                                                            
#find * -exec md5sum {} \; > hash_modefied
#diff hash_original hash_modefied

#!/bin/bash

echo "Enter a directory path or file name:"
read path

# Get the current date and time in the format "DD-MM-YYYY_HH:MM:SS"
current_datetime=$(date +%d-%m-%Y_%H:%M:%S)

# Create a file named "hash_DD-MM-YYYY_HH:MM:SS.txt" containing the MD5 hashes of the specified files
find "$path" -exec md5sum {} \; > "hash_$current_datetime.txt"

# Continuously check the files for changes
while true; do
    # Calculate the current MD5 hashes of the files
    find "$path" -exec md5sum {} \; > "hash_$current_datetime.txt"

    # Compare the current hashes with the baseline
    diff "hash_$current_datetime.txt" "hash_$current_datetime.txt"

    # Sleep for 1 second before checking again
    sleep 1
done
