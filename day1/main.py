#!/usr/bin/python

import sys

total_calories = []

def part_one():
    if len(sys.argv) == 1:
        print('Missing file name argument!')
        exit()
    
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        lines = f.readlines()
        lastline = lines[-1]
        temp_calories = 0

        for line in lines:
            # if the line is not empty, add the value as an int to a temporary variable
            # if the line is empty, add the list to the calories list and reset the temporary variable

            if line.strip() != '':
                temp_calories += int(line)

                # when the last line is not an empty line, the temporary variable needs to be added to the calories list
                if (line is lastline):
                    total_calories.append(temp_calories)
            else:
                total_calories.append(temp_calories)
                temp_calories = 0

    # find the maximum element in the list
    print('Highest number of calories: {}'.format(max(total_calories)))

part_one()

def part_two():
    # sort calories list in descending order
    total_calories.sort(reverse=True)
    top_three_calories = sum(total_calories[0:3])
    
    print('The top three Elves are carrying {} calories'.format(top_three_calories), end='')

part_two()