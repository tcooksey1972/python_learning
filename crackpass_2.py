"""
What would happen if we asked for a password that was four letters?
If we allow for both uppercase and lowercase versions of 26 letters, we could represent this mathematically as:

52 x 52 x 52 x 52
Notice we have over 7,000,000 possibilities.

We can modify our code as follows:
"""


from string import ascii_letters
 
for i in ascii_letters:
    for j in ascii_letters:
        for k in ascii_letters:
            for l in ascii_letters:
                print(i, j, k, l)