
#find * -exec md5sum {} \; > hash_original                                                                                                                                                            
#find * -exec md5sum {} \; > hash_modefied
#diff hash_original hash_modefied

#!/bin/bash

echo "Enter a directory path or file name:"
read path

# Create a baseline file containing the MD5 hashes of the specified files
find "$path" -exec md5sum {} \; > baseline.txt

# Continuously check the files for changes
while true; do
    # Calculate the current MD5 hashes of the files
    find "$path" -exec md5sum {} \; > current.txt

    # Compare the current hashes with the baseline
    diff baseline.txt current.txt

    # Sleep for 1 second before checking again
    sleep 1
done
