import sys

if len(sys.argv) == 1:
    print('Missing file name argument!')
    exit()

total_calories = []

with open(sys.argv[1], 'r', encoding='utf-8') as f:
    lines = [line.strip() for line in f.readlines()]
    lastline = lines[-1]
    temp_calories = 0

    for line in lines:
        # if the line is not empty, add the value as an int to a temporary variable
        # if the line is empty, add the list to the calories list and reset the temporary variable

        if line != '':
            temp_calories += int(line)

            # when the last line is not an empty line, the temporary variable needs to be added to the calories list
            if (line is lastline):
                total_calories.append(temp_calories)
        else:
            total_calories.append(temp_calories)
            temp_calories = 0

    total_calories.sort(reverse=True)
    top_three_calories = sum(total_calories[0:3])

# find the maximum element in the list
print('Highest number of calories: {}'.format(max(total_calories)))
print('The top three Elves are carrying {} calories'.format(top_three_calories), end='')