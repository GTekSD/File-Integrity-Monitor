import hashlib
import os

def calculate_file_hash(filepath):
    with open(filepath, 'rb') as f:
        data = f.read()
    filehash = hashlib.sha512(data).hexdigest()
    return filehash

def erase_baseline_if_already_exists():
    if os.path.exists('baseline.txt'):
        os.remove('baseline.txt')

print('')
print('What would you like to do?')
print('')
print('    A) Collect new Baseline?')
print('    B) Begin monitoring files with saved Baseline?')
print('')
response = input('Please enter "A" or "B": ')
print('')

if response.upper() == 'A':
    # Delete baseline.txt if it already exists
    erase_baseline_if_already_exists()

    # Calculate Hash from the target files and store in baseline.txt
    # Collect all files in the target folder
    files = os.listdir('Files')

    # For each file, calculate the hash, and write to baseline.txt
    for f in files:
        filepath = 'Files/' + f
        hash = calculate_file_hash(filepath)
        with open('baseline.txt', 'a') as f:
            f.write(f'{filepath}|{hash}\n')

elif response.upper() == 'B':
    file_hash_dictionary = {}

    # Load file|hash from baseline.txt and store them in a dictionary
    with open('baseline.txt', 'r') as f:
        file_paths_and_hashes = f.readlines()
    
    for f in file_paths_and_hashes:
        file_hash_dictionary[f.split('|')[0]] = f
