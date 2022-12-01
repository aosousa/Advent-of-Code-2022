#!/usr/bin/python

import sys

total_calories = []

def part_one():
    if len(sys.argv) == 1:
        print('Missing file name argument!')
        exit()
    
    calories_per_elf = []

    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        lines = f.readlines()
        lastline = lines[-1]
        temp_calories = []

        for line in lines:
            # if the line is not empty, add the value as an int to a temp list
            # if the line is empty, add the list to the calories list and reset the temp list

            if line.strip() != '':
                temp_calories.append(int(line))

                # when the last line is not an empty line, the temp list needs to be added to the calories list
                if (line is lastline):
                    calories_per_elf.append(temp_calories)
            else:
                calories_per_elf.append(temp_calories)
                temp_calories = []

    for i in calories_per_elf:
        # calculate the sum of the elements in each list
        total_calories.append(sum(i))

    # find the maximum element in the list
    print('Highest number of calories: ', end='')
    print(max(total_calories))

part_one()

def part_two():
    # sort calories list in descending order
    total_calories.sort(reverse=True)
    top_three_calories = sum(total_calories[0:3])
    
    print('The top three Elves are carrying {} calories'.format(top_three_calories), end='')

part_two()