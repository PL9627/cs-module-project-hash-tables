# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
from collections import Counter

commFreq = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

with open('ciphertext.txt', 'r') as f:
    cphr = f.read()

c = Counter(filter(str.isalnum, cphr))

mapping = {key: value for (key, value) in zip([i[0] for i in c.most_common()], commFreq)}

output = ""

for char in cphr:
    char_out = char

    if char in mapping.keys():
        char_out = mapping[char]
    output += char_out

if __name__ == "__main__":
    print(output)