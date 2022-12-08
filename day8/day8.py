import numpy as np

def generate_map():
    grid = []
    with open("day8/input.txt") as f:
        data = f.read().splitlines()
        for line in data:
            grid.append(list(map(int, list(line))))
    grid_transposed = np.array(grid).T
    return grid, grid_transposed

def solution(grid, grid_transposed):
    visible_trees = 0
    highest_scenic_score = 0
    directions = ["up", "down", "left", "right"]

    # look at each tree in the grid
    for row in range(0, len(grid)):
        for col in range(0, len(grid[0])):
            visible = [True] * 4
            scenic_score = [0] * 4

            # calculates the directions that the tree is visible from,
            # and how many other trees can be seen from each tree.
            for direction in directions:
                index = directions.index(direction)

                if direction == "up":
                    trees = list(reversed(grid_transposed[col][0:row]))
                elif direction == "down":
                    trees = grid_transposed[col][row+1:]
                elif direction == "left":
                    trees = list(reversed(grid[row][0:col]))
                else:
                    trees = grid[row][col+1:]

                for tree in trees:
                    if tree >= grid[row][col]:
                        visible[index] = False
                        scenic_score[index] += 1
                        break
                    # if the tree is smaller, our tree is still visible
                    else:
                        scenic_score[index] += 1

            # calculate this tree's scenic score, and compare it to the highest
            scenic_score = np.prod(scenic_score)
            highest_scenic_score = max(highest_scenic_score, scenic_score)

            # if the tree is visible from any direction, increment the count
            if any(visible):
                visible_trees += 1
    return visible_trees, highest_scenic_score

grid, grid_transposed = generate_map()
visible_trees, highest_scenic_score = solution(grid, grid_transposed)
print(f"Visible trees: {visible_trees}\nHighest scenic score: {highest_scenic_score}")