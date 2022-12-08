import numpy as np
from pprint import pprint

def generate_map():
    tree_map = []
    with open("day8/input.txt") as f:
        data = f.read().splitlines()
        for line in data:
            tree_map.append(list(map(int, list(line))))
    return tree_map

def count_visible(tree_map):
    tree_map_rotated = np.array(tree_map).T
    visible_trees = 0
    highest_scenic_score = 0

    for row in range(0, len(tree_map)):
        for col in range(0, len(tree_map[0])):
            # if (row == 0) or (row == len(tree_map)-1) or (col == 0) or (col == len(tree_map[0])-1):
            #     visible_trees += 1
            # else:

            # look at the numbers before this one in the column
            #print(f"row, col = {row}, {col}")
            #print("col comparison")
            done = False
            visible_before_col = True
            visible_trees_before_col = 0
            #print(tree_map_rotated[col][0:row], list(reversed(tree_map_rotated[col][0:row])))
            for i in list(reversed(tree_map_rotated[col][0:row])):
                if i >= tree_map[row][col]:
                    visible_before_col = False
                if (not done):
                    if i < tree_map[row][col]:
                        visible_trees_before_col += 1
                        #print("smaller")
                    elif i == tree_map[row][col]:
                        visible_trees_before_col += 1
                        #print("equal")
                        done = True
                    else:
                        #print("larger")
                        visible_before_col += 1
                        done = True

            done = False
            # look at the numbers after this one in the column
            visible_after_col = True
            visible_trees_after_col = 0
            #print("col comparison")
            for i in tree_map_rotated[col][row+1:]:
                if i >= tree_map[row][col]:
                    visible_after_col = False
                if (not done):
                    if i < tree_map[row][col]:
                        visible_trees_after_col += 1
                        #print("smaller")
                    elif i == tree_map[row][col]:
                        visible_trees_after_col += 1
                        #print("equal")
                        done = True
                    else:
                        visible_trees_after_col += 1
                        #print("larger")
                        done = True

            done = False
            # look at the numbers before this one in the row
            visible_before_row = True
            visible_trees_before_row = 0
            #print("row comparison")
            for i in list(reversed(tree_map[row][0:col])):
                if i >= tree_map[row][col]:
                    visible_before_row = False
                if (not done):
                    if i < tree_map[row][col]:
                        visible_trees_before_row += 1
                        #print("smaller")
                    elif i == tree_map[row][col]:
                        visible_trees_before_row += 1
                        #print("equal")
                        done = True
                    else:
                        visible_trees_before_row += 1
                        #print("larger")
                        done = True

            done = False
            # look at the numbers after this one in the row
            visible_after_row = True
            #print("row comparison")
            visible_trees_after_row = 0
            for i in tree_map[row][col+1:]:
                if i >= tree_map[row][col]:
                    visible_after_row = False
                if (not done):
                    if i < tree_map[row][col]:
                        visible_trees_after_row += 1
                        #print("smaller")
                    elif i == tree_map[row][col]:
                        visible_trees_after_row += 1
                        #print("equal")
                        done = True
                    else:
                        visible_trees_after_row += 1
                        #print("larger")
                        done = True


            #print(f"row, col = {row}, {col}, visible_before_col = {visible_trees_before_col}, visible_after_col = {visible_trees_after_col}, visible_before_row = {visible_trees_before_row}, visible_after_row = {visible_trees_after_row}")
            scenic_score = visible_trees_before_col * visible_trees_after_col * visible_trees_before_row * visible_trees_after_row
            if scenic_score > highest_scenic_score:
                highest_scenic_score = scenic_score

            if visible_before_col or visible_after_col or visible_before_row or visible_after_row:
                visible_trees += 1

    return visible_trees, highest_scenic_score

tree_map = generate_map()
visible_trees, highest_scenic_score = count_visible(tree_map)
print(f"HIGHEST SCENIC SCORE: {highest_scenic_score}")