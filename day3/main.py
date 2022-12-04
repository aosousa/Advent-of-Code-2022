#!/usr/bin/python

import sys

priorities = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

def priority(letter: str):
    """Return the priority value of a letter according to the Advent of Code
    2022's day 3 strategy guide.

    Lowercase item types a through z have priorities 1 through 26 (see priorities dictionary above).
    Uppercase item types A through Z have priorities 27 through 52.

    Args:
        letter: Letter in a rucksack
    
    Returns:
        The priority value of a letter according to the strategy guide.
    """

    val = priorities[letter.lower()]

    # instead of adding uppercase variations of the alphabet just for the 
    # different priorities, we know the difference between an lowercase and
    # uppercase letter is always 26 (e.g., a = 1, A = 27), so add that number to
    # the priority_sum variable if the letter found is uppercase
    if letter.isupper():
        val += 26
    
    return val

def part_one(input_list: list[str]):
    priority_sum = 0

    for line in input_list:       
        half_index = len(line) // 2
        first_half, second_half = line[:half_index], line[half_index:]
        
        for i in first_half:
            if i in second_half:
                priority_sum += priority(i)
                break

    print('The sum of the priorities of the item types that appear in both compartments of the rucksack is: {}'.format(priority_sum))

def part_two(input_list: list[str]):
    priority_sum = 0

    i = 0
    while i < len(input_list):
        for j in input_list[i]:
            if j in input_list[i+1] and j in input_list[i+2]:
                priority_sum += priority(j)
                break
        
        i += 3

    print('The sum of the priorities of the badge item types is: {}'.format(priority_sum))

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Missing file name argument!')
        exit()

    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines()]
        part_one(lines)
        part_two(lines)