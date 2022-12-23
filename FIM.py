import os
import hashlib

def calculate_file_hash(filepath):
    with open(filepath, 'rb') as f:
        data = f.read()
        return hashlib.sha512(data).hexdigest()

def erase_baseline_if_already_exists():
    if os.path.exists('baseline.txt'):
        # Delete it
        os.remove('baseline.txt')

print("What would you like to do?")
print("    A) Collect new Baseline?")
print("    B) Begin monitoring files with saved Baseline?")
response = input("Please enter 'A' or 'B': ")

if response.upper() == "A":
    # Delete baseline.txt if it already exists
    erase_baseline_if_already_exists()

    # Calculate Hash from the target files and store in baseline.txt
    # Collect all files in the target folder
    files = os.listdir('Files')

    # For each file, calculate the hash, and write to baseline.txt
    for f in files:
        filepath = os.path.join('Files', f)
        hash_value = calculate_file_hash(filepath)
        with open('baseline.txt', 'a') as f:
            f.write(f"{filepath}|{hash_value}\n")

elif response.upper() == "B":
    file_hash_dictionary = {}

    # Load file|hash from baseline.txt and store them in a dictionary
    with open('baseline.txt', 'r') as f:
        for line in f:
            filepath, hash_value = line.strip().split('|')
            file_hash_dictionary[filepath] = hash_value

    # Begin (continuously) monitoring files with saved Baseline
    while True:
        files = os.listdir('Files')

        # For each file, calculate the hash and compare with the baseline
        for f in files:
            filepath = os.path.join('Files', f)
            hash_value = calculate_file_hash(filepath)

            # Notify if a new file has been created
            if filepath not in file_hash_dictionary:
                # A new file has been created!
                print(f"{filepath} has been created!")

                # Update the baseline
                file_hash_dictionary[
