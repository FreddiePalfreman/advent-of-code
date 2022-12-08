import math

def find_common_item(backpack):
    return list(set(backpack[0]).intersection(set(backpack[1])))[0]

def find_priority(character):
    if character.isupper():
        return ord(character) - 38
    else:
        return ord(character) - 96

def part_one():
    with open("day3/input.txt") as f:
        running_total = 0
        for line in f.read().striplines():
            first_compartment = list(line[:math.floor(len(line)/2)])
            second_compartment = list(line[math.ceil(len(line)/2):])
            backpack = [first_compartment, second_compartment]

            common_item = find_common_item(backpack)
            priority = find_priority(common_item)
            running_total += priority
        return running_total

def part_two():
    with open("day3/input.txt") as f:
        lines = f.read().splitlines()
        running_total = 0
        for count in range(0, len(lines), 3):
            backpack1 = list(lines[count])
            backpack2 = list(lines[count+1])
            backpack3 = list(lines[count+2])
            common_item = set(backpack1).intersection(set(backpack2), set(backpack3))
            priority = find_priority(list(common_item)[0])
            running_total += priority
        return running_total

print(part_two())