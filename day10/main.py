import sys

if len(sys.argv) == 1:
    print('Missing file name argument!')
    exit()

x = 1
cycle = 0
signal_strength = 0
pending_cycle = 0
letters = ''

with open(sys.argv[1], 'r', encoding='utf-8') as f:
    lines = [line.strip() for line in f.readlines()]

    i = 0
    while i < len(lines):
        cycle += 1

        signal_strength += x * cycle if cycle%40 == 20 else 0

        if (cycle-1)%40 == 0 or i == len(lines) - 1:
            letters += '\n'

        letters += '#' if (cycle-1)%40 - x in [-1, 0, 1] else '.'

        # similar solution to day 7 using structural pattern matching to detect if it is
        # a noop instruction or an addx instruction
        match lines[i].split():
            case ['noop']:
                pending_cycle = 0
                i += 1
            case ['addx', v]:
                if pending_cycle == 0:
                    i = i
                    pending_cycle = int(v)
                else:
                    pending_cycle = 0
                    x += int(v)
                    i += 1

print('The sum of the signal strengths during the specified cycles is: {}'.format(signal_strength))
print(letters)