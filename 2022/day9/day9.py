def generate_grid():
    """
    Generates a grid of the size needed to fit the path of the rope.
    """
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
    """
    Prints the grid in a readable format. Any place that is 'h' is replaced with '#',
    as the h means that it is hiding a space visited by the end of the rope.
    """
    for row in grid:
        to_print = []
        for col in row:
            if col == "h":
                col = "#"
            to_print.append(col)
        print(''.join(to_print))
    print()

def get_start_coordinates(grid):
    """
    Returns the starting coordinates on the grid.
    """
    start = []
    for row in grid:
        for col in row:
            if col == "S":
                start = [row.index(col), grid.index(row)]
    return start[:]

def simulate_motions(grid, rope):
    """
    Given a rope containing the knot names and their start coordinates, this
    simulates the movement of the rope based on the motions in the input file.

    The head of the rope is moved first, then the other knots are moved to
    follow the head.

    The tail of the rope marks spaces it has visited with a #, and a final version
    of the grid is printed, with a count of #s.
    """
    with open("2022/day9/input.txt", "r") as f:
        motions = f.read().splitlines()
        for motion in motions:
            motion = motion.split(" ")
            for count in range(int(motion[1])):
                # remove knots from the grid as they are about to be moved.
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

                # if the head will be covering a trailing knot space, mark it in lowercase
                if grid[rope[0][1][1]][rope[0][1][0]] == "#":
                    grid[rope[0][1][1]][rope[0][1][0]] = "h"
                else:
                    grid[rope[0][1][1]][rope[0][1][0]] = rope[0][0]

                # move the other knots behind the head
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
    start_position = get_start_coordinates(grid)

    rope1 = [["H", start_position[:]], ["T", start_position[:]]]

    rope2 = [["H", get_start_coordinates(grid)]]
    for count in range(1, 10):
        rope2.append([str(count), get_start_coordinates(grid)])

    simulate_motions(grid, rope2)