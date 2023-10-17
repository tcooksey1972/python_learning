"""
What would happen if we asked for a password that was four letters, numbers, or punctuations? We would have over 78,000,000 possibilities open to us!
We can modify our code as follows:
"""

from string import ascii_letters, digits, punctuation

for i in ascii_letters + digits + punctuation:
    for j in ascii_letters + digits + punctuation:
        for k in ascii_letters + digits + punctuation:
            for l in ascii_letters + digits + punctuation:
                print(i, j, k, l)