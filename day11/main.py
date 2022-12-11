import math
import sys

if len(sys.argv) == 1:
    print('Missing file name argument!')
    exit()

class Monkey(object):
    def __init__(self):
        self.items = []
        self.inspections = 0
        self.operation = []
        self.divisible_by = 1
        self.throw_to_if_true = 0
        self.throw_to_if_false = 0

def build_monkeys() -> list[Monkey]:
    monkeys: list[Monkey] = []
    monkey_inspecting = -1

    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines()]

        # build monkey dictionary first using structural pattern matching
        for line in lines:
            match line.split():
                case ['Monkey', m]:
                    monkeys.append(Monkey())
                
                # wildcard pattern to get an arbitrary sequence of elements that follows
                # the previous elements in the pattern
                case ['Starting', 'items:', *items]:
                    monkeys[monkey_inspecting].items = [int(i.replace(',', '')) for i in items]

                case ['Operation:', 'new', '=', 'old', operation, value]:
                    monkeys[monkey_inspecting].operation = '{} {}'.format(operation, value).split()

                case ['Test:', 'divisible', 'by', value]:
                    monkeys[monkey_inspecting].divisible_by = int(value)

                case ['If', 'true:', 'throw', 'to', 'monkey', value]:
                    monkeys[monkey_inspecting].throw_to_if_true = int(value)

                case ['If', 'false:', 'throw', 'to', 'monkey', value]:
                    monkeys[monkey_inspecting].throw_to_if_false = int(value)

                # reset monkeys under inspecting if it's an empty line 
                case []:
                    monkey_inspecting = -1
    
    return monkeys

def monkey_business(monkeys: list[Monkey], rounds: int, divide_worry_level: bool) -> int:
    lcm = math.prod(m.divisible_by for m in monkeys)

    for _ in range(rounds):
        for count, monkey in enumerate(monkeys):
            for item in monkey.items:
                worry_level = int(item)
                monkey.inspections += 1
                
                operator, value = monkey.operation[0], monkey.operation[1]
                if value == 'old':
                    value = worry_level

                match operator:
                    case '+':
                        worry_level += int(value)

                    case '*':
                        worry_level *= int(value)
                
                if divide_worry_level:
                    worry_level = worry_level // 3
                else:
                    worry_level = worry_level % lcm
                
                test = worry_level%monkey.divisible_by == 0
                if test:
                    monkeys[monkey.throw_to_if_true].items.append(worry_level)
                else:
                    monkeys[monkey.throw_to_if_false].items.append(worry_level)

            monkeys[count].items.clear()

    inspections = [monkey.inspections for monkey in monkeys]
    inspections.sort(reverse=True)
    return inspections[0] * inspections[1]

monkeys = build_monkeys()
part_one_result = monkey_business(monkeys, 20, True)
print('The level of monkey business after 20 rounds of stuff-slinging simian shenanigans: {}'.format(part_one_result))

monkeys = build_monkeys()
part_two_result = monkey_business(monkeys, 10000, False)
print('The level of monkey business after 10000 rounds of stuff-slinging simian shenanigans: {}'.format(part_two_result))