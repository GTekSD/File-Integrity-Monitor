# File-Integrity-Monitor
FIM code based on Integrity from CIA Triad.

Integrity:
Integrity means that data can be trusted. It should be maintained in a correct state, kept so that it may not be tampered with, and should be correct, authentic, and reliable.
Integrity involves maintaining the consistency, accuracy and trustworthiness of data over its entire lifecycle. Data must not be changed in transit, and steps must be taken to ensure data cannot be altered by unauthorized people .

This code basically check if the given files get altered, changed or modified. it will alert user if made any changes in the file or hash.


## Here is a simple flow chart:

```mermaid
graph TD;
    A(Start)-->B(Ask user what they want to do:<br />A. Collect new Baseline<br />B. Begin monitoring files with saved Baseline);
    B-->C(Collect new Baseline<br />1. Calculate HASH value from target files<br />2. Store the filelhash pairs in baseline.txt);
    B-->D(Begin monitoring files with saved Baseline<br />1. Load file:hash pairs from baseline.txt);
    D-->E(Continuously monitor file inteqrity<br />1. Loop through each file target file, calculate the hash,<br />and compare the filelhash to what is baseline.txt);
    E-->E;
    E-->F(Notify user if a file is chanqed or deleted<br />If a file's actual hash is different than what is recorded in the baseline,<br />print to the screen in color, if a file has been changed or deleted.<br />Integrity compromise!);
```

## How to use Python script
To use the Python script to monitor a specified directory for changes to the files within it, follow these steps:

1. If you want to collect a new baseline, select option "A" when prompted:
```
What would you like to do?

    A) Collect new Baseline?
    B) Begin monitoring files with saved Baseline?

Please enter "A" or "B": A
```
    This will calculate the SHA-512 hash value for each file in the "Files" directory and store the filenames and hash values in a file called "baseline.txt".

2. If you want to begin monitoring the files with a saved baseline, select option "B" when prompted:
```
What would you like to do?

    A) Collect new Baseline?
    B) Begin monitoring files with saved Baseline?

Please enter "A" or "B": B
```
    This will load the filenames and hash values from the "baseline.txt" file into a dictionary and begin continuously monitoring the "Files" directory for changes. If a new file is created, the script will print a message indicating that a new file has been created. If an existing file is modified, the script will print a message indicating that the file has changed. If an existing file is deleted, the script will print a message indicating that the file has been deleted.

Note: If the "baseline.txt" file does not exist when you select option "B", the script will throw an error and terminate. Make sure to collect a baseline first by selecting option "A" if you have not done so already.
