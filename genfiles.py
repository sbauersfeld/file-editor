import random
import string

with open("1kb.py", 'w') as f:
    f.write(''.join(random.choices(string.ascii_lowercase, k=1000)))

with open("10kb.py", 'w') as f:
    f.write(''.join(random.choices(string.ascii_lowercase, k=10000)))

with open("100kb.py", 'w') as f:
    f.write(''.join(random.choices(string.ascii_lowercase, k=100000)))

with open("1mb.py", 'w') as f:
    f.write(''.join(random.choices(string.ascii_lowercase, k=1000000)))