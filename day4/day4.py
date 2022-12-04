def solution():
    with open("day4/input.txt") as f:
        lines = f.read().splitlines()
        full_overlaps = 0
        partial_overlaps = 0
        for line in lines:
            elves = line.split(',')
            elf_bounds = []
            for elf in elves:
                start = int(elf.split('-')[0])
                end = int(elf.split('-')[1])
                elf_bounds.append([start, end])

            # calculate full overlaps
            if elf_bounds[0][0] >= elf_bounds[1][0] and elf_bounds[0][1] <= elf_bounds[1][1]:
                full_overlaps += 1
            elif elf_bounds[1][0] >= elf_bounds[0][0] and elf_bounds[1][1] <= elf_bounds[0][1]:
                full_overlaps += 1

            # calculate partial overlaps
            if elf_bounds[0][0] <= elf_bounds[1][0] and elf_bounds[0][1] >= elf_bounds[1][0]:
                partial_overlaps += 1
            elif elf_bounds[1][0] <= elf_bounds[0][0] and elf_bounds[1][1] >= elf_bounds[0][0]:
                partial_overlaps += 1

        return full_overlaps, partial_overlaps

print(solution())