import difflib
import sys

with open('test_out.txt', 'r') as hosts0:
    with open('out.txt', 'r') as hosts1:
        diff = difflib.unified_diff(
            hosts0.readlines(),
            hosts1.readlines(),
            fromfile='hosts0',
            tofile='hosts1',
        )
        for line in diff:
            sys.stdout.write(line)
