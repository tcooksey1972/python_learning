"""
Consider how many possible number combinations you could have if your password (for your phone or otherwise) was secured by only a four-digit password. There are 10,000 possible digits. Generally, we could consider the possibilities as follows:

10 x 10 x 10 x 10
Notice that, in the worst case, bad actors would need to attempt 10,000 possible passwords.

We could attempt to represent this in code. 
Consider the following code-based representation of the above problem:

"""
from string import digits

for i in digits:
    for j in digits:
        for k in digits:
            for l in digits:
                print(i, j, k, l)