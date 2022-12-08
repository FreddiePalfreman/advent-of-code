def part_1():
    with open('day1/input.txt', "r") as file:
        lines = file.readlines()
        highest_elf = 0
        current_elf = 0
        for line in lines:
            if line != "\n":
                current_elf += int(line)
            else:
                if current_elf > highest_elf:
                    highest_elf = current_elf
                current_elf = 0
        print(f"{highest_elf}")


def part_2():
    with open('day1/input.txt', "r") as file:
        lines = file.readlines()
        all_elves = []
        current_elf = 0
        for line in lines:
            if line != "\n":
                current_elf += int(line)
            else:
                all_elves.append(current_elf)
                current_elf = 0
        all_elves.sort(reverse=True)
        print(f"{all_elves}")
        print(f"Top 3 elves total: {all_elves[0]+all_elves[1]+all_elves[2]}")

part_2()