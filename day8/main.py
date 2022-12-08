#!/usr/bin/python

import sys

def main():
    part_one_result = 0
    part_two_result = 0

    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines()]

        for idx, line in enumerate(lines):
            for count, value in enumerate(line):
                # trees on the edges
                if idx == 0 or idx == len(lines) - 1 or count == 0 or count == len(line) - 1:
                    part_one_result += 1
                
                if idx != 0 and idx != len(lines) - 1 and count != 0 and count != len(line) - 1:
                    top, right, bottom, left = True, True, True, True

                    # compare against top edge
                    t = idx - 1 # can be a cause of errors
                    while t >= 0:
                        if (int(value) <= int(lines[t][count])):
                            top = False
                            break
                        t -= 1

                    if top:
                        part_one_result += 1
                        continue

                    # compare against right edge
                    r = count + 1
                    while r < len(line):
                        if int(value) <= int(line[r]):
                            right = False
                            break
                        r += 1

                    if right:
                        part_one_result += 1
                        continue

                    # compare against bottom edge
                    b = idx + 1
                    while b < len(line):
                        if int(value) <= int(lines[b][count]):
                            bottom = False
                            break
                        b += 1
                    
                    if bottom:
                        part_one_result += 1
                        continue

                    # compare against left edge
                    l = count - 1
                    while l >= 0:
                        if int(value) <= int(line[l]):
                            left = False
                            break
                        l -= 1

                    if left:
                        part_one_result += 1
                        continue

    print('{} trees are visible from outside the grid'.format(part_one_result))
    print('The highest scenic score possible for any tree is: {}'.format(part_two_result))

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Missing file name argument!')
        exit()
    
    main()