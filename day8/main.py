#!/usr/bin/python

import sys

def main():
    part_one_result = 0
    part_two_result = 0

    scenic_scores = []

    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines()]

        for idx, line in enumerate(lines):
            for count, value in enumerate(line):
                # trees on the edges
                if idx == 0 or idx == len(lines) - 1 or count == 0 or count == len(line) - 1:
                    part_one_result += 1
                
                if idx != 0 and idx != len(lines) - 1 and count != 0 and count != len(line) - 1:
                    top, right, bottom, left = True, True, True, True
                    top_blocked_at, right_blocked_at, bottom_blocked_at, left_blocked_at = 0, 0, 0, 0

                    # compare against top edge
                    t = idx - 1
                    while t >= 0:
                        top_blocked_at += 1

                        if int(value) <= int(lines[t][count]):
                            top = False
                            break

                        t -= 1

                    # compare against right edge
                    r = count + 1
                    while r < len(line):
                        right_blocked_at += 1

                        if int(value) <= int(line[r]):
                            right = False
                            break

                        r += 1

                    # compare against bottom edge
                    b = idx + 1
                    while b < len(line):
                        bottom_blocked_at += 1

                        if int(value) <= int(lines[b][count]):
                            bottom = False
                            break

                        b += 1

                    # compare against left edge
                    l = count - 1
                    while l >= 0:
                        left_blocked_at += 1

                        if int(value) <= int(line[l]):
                            left = False
                            break

                        l -= 1

                    if left or bottom or top or right:
                        part_one_result += 1
                        scenic_scores.append(top_blocked_at * right_blocked_at * bottom_blocked_at * left_blocked_at)
                        continue

    part_two_result = max(scenic_scores)

    print('{} trees are visible from outside the grid'.format(part_one_result))
    print('The highest scenic score possible for any tree is: {}'.format(part_two_result))

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Missing file name argument!')
        exit()
    
    main()