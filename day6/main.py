import sys

if len(sys.argv) == 1:
    print('Missing file name argument!')
    exit()

def find_first_marker(data: str, unique_characters: int) -> int:
    for i in range(0, len(data)-(unique_characters-1)):
        data_portion = data[i:i+unique_characters]
        if len([x for x in set(data_portion) if data_portion.count(x) > 1]) == 0:
            return i + unique_characters

    return 0

part_one_result = 0
part_two_result = 0

with open(sys.argv[1], 'r', encoding='utf-8') as f:
    data = f.read().strip()

    part_one_result = find_first_marker(data, 4)
    part_two_result = find_first_marker(data, 14)

print('{} characters need to be processed before the first start-of-packet marker is detected.'.format(part_one_result))
print('{} characters need to be processed before the first start-of-message marker is detected.'.format(part_two_result))