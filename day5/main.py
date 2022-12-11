import re
import sys

if len(sys.argv) == 1:
    print('Missing file name argument!')
    exit()

moves = []

with open(sys.argv[1], 'r', encoding='utf-8') as f:
    lines = [line.replace('\n', '') for line in f.readlines()]

    # get the number of crates
    num_crates = int((len(lines[0]) + 1) / 4)
    crates = [[] for i in range(num_crates)]

    # get the list of moves and crate positions
    for line in lines:
        x = line.strip()

        if len(x) > 0:
            if x[0:4] == 'move':
                moves.append([int(v) for v in re.findall(r'\b\d+\b', x)])

            elif x[0] != '1':
                for i in range(0, len(line), 4):
                    crate = line[i:i+3].strip()
                    
                    if crate != '':
                        idx = 0 if i == 0 else int(i / 4)
                        crates[idx].append(crate[1])

    part_one_crates = [crate[:] for crate in crates]
    part_two_crates = [crate[:] for crate in crates]

    # loop moves to make the required changes to each crate in each part of the challenge
    for move in moves:
        amount, origin, destination = move

        crates_to_move = []
        
        for i in range(amount):
            crate_to_move = part_one_crates[origin - 1].pop(0)
            part_one_crates[destination - 1].insert(0, crate_to_move)

            crate_to_move_two = part_two_crates[origin - 1].pop(0)
            crates_to_move.append(crate_to_move_two)
        
        crates_to_move.reverse()
                    
        for j in crates_to_move:
            part_two_crates[destination - 1].insert(0, j)

    top_crates_part_one = ''.join(c[0] for c in part_one_crates if c)
    top_crates_part_two = ''.join(c[0] for c in part_two_crates if c)

    print('After the rearragement procedure done by CrateMover 9000 is completed, the crate that ends up on top of each stack is: {}'.format(top_crates_part_one))
    print('After the rearragement procedure done by CrateMover 9001 is completed, the crate that ends up on top of each stack is: {}'.format(top_crates_part_two))