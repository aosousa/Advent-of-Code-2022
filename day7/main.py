from collections import defaultdict
from itertools import accumulate
import sys

if len(sys.argv) == 1:
    print('Missing file name argument!')
    exit()

part_one_result = 0
part_two_result = 0

# default dictionary in order to automatically create a key-value pair (int value here)
# if the specified key cannot be found
directories = defaultdict(int) 
dir_under_inspection = []

with open(sys.argv[1], 'r', encoding='utf-8') as f:
    lines = [line.strip() for line in f.readlines()]

    for line in lines:
        # https://peps.python.org/pep-0636
        match line.split():
            case ['$', 'cd', '/']:
                dir_under_inspection = ['/']
            case ['$', 'cd', '..']:
                dir_under_inspection.pop()
            case ['$', 'cd', x]:
                dir_under_inspection.append(x+'/')
            case ['$', 'ls']:
                continue
            case ['dir', _]:
                continue
            case [size, _]:
                for i in accumulate(dir_under_inspection):
                    directories[i] += int(size)

part_one_result = sum(size for size in directories.values() if size <= 100000)

unused_space = 70000000 - directories['/'] 
minimum_space_to_delete = 30000000 - unused_space

part_two_result = min(size for size in directories.values() if size >= minimum_space_to_delete)

print('The sum of the total sizes of directories with a total size of at most 100000 is {}'.format(part_one_result))
print('The total size of the directory needed to delete to hit the minimum free space for the update is: {}'.format(part_two_result))