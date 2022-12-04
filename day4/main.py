#!/usr/bin/python

import sys

def main():
    if len(sys.argv) == 1:
        print('Missing file name argument!')
        exit()

    assignment_pairs = 0
    overlapping_assignment_pairs = 0

    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines()]

        for line in lines:
            section_ids = line.split(',')
            first_section_id_range = [int(s) for s in section_ids[0].split('-')]
            second_section_id_range = [int(s) for s in section_ids[1].split('-')]

            a, b, c, d = first_section_id_range[0], first_section_id_range[1], second_section_id_range[0], second_section_id_range[1]
            x, y = abs(a - b), abs(c - d)

            if (x > y and a <= c and b >= d) or (x < y and a >= c and b <= d) or (x == y and a == c and b == d):
                assignment_pairs += 1

            for i in range(a, b+1):
                if i >= c and i <= d:
                    overlapping_assignment_pairs += 1
                    break
    
    print('One range fully contains the other in {} assignment pairs'.format(assignment_pairs))
    print('The ranges overlap in {} assignment pairs'.format(overlapping_assignment_pairs))

if __name__ == '__main__':
    main()