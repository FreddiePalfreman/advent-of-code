import numpy as np

def generate_grid():
    x = 0
    y = 0
    x_coords = []
    y_coords = []
    with open("2022/day9/input.txt", "r") as f:
        lines = f.read().splitlines()
        for line in lines:
            line = line.split(" ")
            if line[0] == "L":
                x -= int(line[1])
            elif line[0] == "R":
                x += int(line[1])
            elif line[0] == "U":
                y += int(line[1])
            elif line[0] == "D":
                y -= int(line[1])
            x_coords.append(x)
            y_coords.append(y)
        min_x = min(x_coords)
        max_x = max(x_coords)
        min_y = min(y_coords)
        max_y = max(y_coords)
        width = abs(min_x) + abs(max_x) + 1
        height = abs(min_y) + abs(max_y) + 1
        grid = [["." for i in range(width)] for j in range(height)]

        start_position = [0 - min_x, 0 - min_y]
        grid[len(grid)-1-start_position[1]][start_position[0]] = "S"
        return grid

def print_grid(grid):
    for row in grid:
        print(" ".join(row))
    print()

def get_start_coordinates():
    start = []
    for row in grid:
        for col in row:
            if col == "S":
                start = [row.index(col), grid.index(row)]
    return start

def get_head_tail_coordinates(grid):
    head = []
    tail = []
    start = []
    for row in grid:
        for col in row:
            if col == "H":
                head = [row.index(col), grid.index(row)]
            if col == "T":
                tail = [row.index(col), grid.index(row)]
            if col == "S":
                start = [row.index(col), grid.index(row)]
    if head == []:
        head = start[:]
    if tail == []:
        tail = start[:]

    return head, tail

def simulate_motions(grid):
    head, tail = get_head_tail_coordinates(grid)
    with open("2022/day9/input.txt", "r") as f:
        motions = f.read().splitlines()
        for motion in motions:
            print(f"=== {motion} ===")
            motion = motion.split(" ")
            for count in range(int(motion[1])):
                if grid[rope[count-1][1][0]][rope[count-1][1][0]] == "h":
                    grid[rope[count-1][1][0]][rope[count-1][1][0]] = "#"
                if grid[rope[count-1][1][0]][rope[count-1][1][0]] not in ["S", "h", "#"]:
                    grid[rope[count-1][1][0]][rope[count-1][1][0]] = "."
                if grid[rope[count][1][1]][rope[count][1][0]] != "S":
                    grid[rope[count][1][1]][rope[count][1][0]] = "#"

                if motion[0] == "L":
                    rope[count-1][1][0] -= 1
                elif motion[0] == "R":
                    rope[count-1][1][0] += 1
                elif motion[0] == "U":
                    rope[count-1][1][0] -= 1
                elif motion[0] == "D":
                    rope[count-1][1][0] += 1
                if grid[rope[count-1][1][0]][rope[count-1][1][0]] == "#":
                    grid[rope[count-1][1][0]][rope[count-1][1][0]] = "h"
                else:
                    grid[rope[count-1][1][0]][rope[count-1][1][0]] = "H"

                # if the head is ever two steps U, D, L or R from the tail, the tail must also move one step in that direction
                # otherwise, if the head and tail aren't touching and aren't in the same row or column, the tail always moves one step diagonally to keep up
                # same column, different rows
                if abs(rope[count-1][1][0] - rope[count][1][0]) == 2 and abs(rope[count-1][1][0] - rope[count][1][1]) == 0:
                    if rope[count-1][1][0] > rope[count][1][0]:
                        rope[count][1][0] += 1
                    else:
                        rope[count][1][0] -= 1

                # same row, different columns
                elif abs(rope[count-1][1][0] - rope[count][1][0]) == 0 and abs(rope[count-1][1][0] - rope[count][1][1]) == 2:
                    if rope[count-1][1][0] > rope[count][1][1]:
                        rope[count][1][1] += 1
                    else:
                        rope[count][1][1] -= 1

                elif abs(rope[count-1][1][0] - rope[count][1][0]) == 2 and abs(rope[count-1][1][0] - rope[count][1][1]) == 1:
                    if rope[count-1][1][0] > rope[count][1][0]:
                        rope[count][1][0] += 1
                    else:
                        rope[count][1][0] -= 1
                    if rope[count-1][1][0] > rope[count][1][1]:
                        rope[count][1][1] += 1
                    else:
                        rope[count][1][1] -= 1
                elif abs(rope[count-1][1][0] - rope[count][1][0]) == 1 and abs(rope[count-1][1][0] - rope[count][1][1]) == 2:
                    if rope[count-1][1][0] > rope[count][1][0]:
                        rope[count][1][0] += 1
                    else:
                        rope[count][1][0] -= 1
                    if rope[count-1][1][0] > rope[count][1][1]:
                        rope[count][1][1] += 1
                    else:
                        rope[count][1][1] -= 1

                if grid[rope[count][1][1]][rope[count][1][0]] != "S":
                    grid[rope[count][1][1]][rope[count][1][0]] = "T"

                #print_grid(grid)

        grid[rope[count][1][1]][rope[count][1][0]] = "#"
        if grid[rope[count-1][1][0]][rope[count-1][1][0]] == "h":
            grid[rope[count-1][1][0]][rope[count-1][1][0]] = "#"
        print(f"\n\n FINAL GRID:")
        print_grid(grid)

        count = 0
        for row in grid:
            for col in row:
                if col in ["#", "S"]:
                    count += 1
        print(f"count: {count}")

def simulate_motions_two(grid, knots):
    rope = [["H", get_start_coordinates()]]
    for count in range(1, knots):
        rope.append([str(count), get_start_coordinates()])

    with open("2022/day9/input.txt", "r") as f:
        motions = f.read().splitlines()
        for motion in motions:
            motion = motion.split(" ")
            for count in range(int(motion[1])):

                for knot in rope:
                    compare = grid[knot[1][1]][knot[1][0]]
                    if compare not in ["S", "#"]:
                        if compare == "h":
                            grid[knot[1][1]][knot[1][0]] = "#"
                        else:
                            grid[knot[1][1]][knot[1][0]] = "."

                # move the knot at the head of the rope
                if motion[0] == "L":
                    rope[0][1][0] -= 1
                elif motion[0] == "R":
                    rope[0][1][0] += 1
                elif motion[0] == "U":
                    rope[0][1][1] -= 1
                elif motion[0] == "D":
                    rope[0][1][1] += 1

                if grid[rope[0][1][1]][rope[0][1][0]] == "#":
                    grid[rope[0][1][1]][rope[0][1][0]] = "h"
                else:
                    grid[rope[0][1][1]][rope[0][1][0]] = rope[0][0]

                # move the other knots
                for count in range(1, len(rope)):
                    # same row, different columns
                    if abs(rope[count-1][1][0] - rope[count][1][0]) == 2 and abs(rope[count-1][1][1] - rope[count][1][1]) == 0:
                        if rope[count-1][1][0] > rope[count][1][0]:
                            rope[count][1][0] += 1
                        else:
                            rope[count][1][0] -= 1

                    # same column, different rows
                    elif abs(rope[count-1][1][0] - rope[count][1][0]) == 0 and abs(rope[count-1][1][1] - rope[count][1][1]) == 2:
                        if rope[count-1][1][1] > rope[count][1][1]:
                            rope[count][1][1] += 1
                        else:
                            rope[count][1][1] -= 1

                    # digonal 1
                    elif abs(rope[count-1][1][0] - rope[count][1][0]) == 2 and abs(rope[count-1][1][1] - rope[count][1][1]) == 1:
                        if rope[count-1][1][0] > rope[count][1][0]:
                            rope[count][1][0] += 1
                        else:
                            rope[count][1][0] -= 1
                        if rope[count-1][1][1] > rope[count][1][1]:
                            rope[count][1][1] += 1
                        else:
                            rope[count][1][1] -= 1

                    # diagonal 2
                    elif abs(rope[count-1][1][0] - rope[count][1][0]) == 1 and abs(rope[count-1][1][1] - rope[count][1][1]) == 2:
                        if rope[count-1][1][0] > rope[count][1][0]:
                            rope[count][1][0] += 1
                        else:
                            rope[count][1][0] -= 1
                        if rope[count-1][1][1] > rope[count][1][1]:
                            rope[count][1][1] += 1
                        else:
                            rope[count][1][1] -= 1

                    # long diagonal (2 away))
                    elif abs(rope[count-1][1][0] - rope[count][1][0]) == 2 and abs(rope[count-1][1][1] - rope[count][1][1]) == 2:
                        if rope[count-1][1][0] > rope[count][1][0]:
                            rope[count][1][0] += 1
                        else:
                            rope[count][1][0] -= 1
                        if rope[count-1][1][1] > rope[count][1][1]:
                            rope[count][1][1] += 1
                        else:
                            rope[count][1][1] -= 1

                    if count == len(rope)-1:
                        symbol = "#"
                    else:
                        symbol = rope[count][0]

                    # place the knot on the grid
                    if grid[rope[count][1][1]][rope[count][1][0]] not in ["S", "#", "h"]:
                        grid[rope[count][1][1]][rope[count][1][0]] = symbol

            print_grid(grid)

    count = 0
    for row in grid:
        for col in row:
            if col in ["#", "S", "h"]:
                count += 1
    print(f"count: {count}")


if __name__ == "__main__":
    grid = generate_grid()
    simulate_motions_two(grid, 10)
