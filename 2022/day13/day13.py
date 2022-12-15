import ast

def recursively_compare(left, right):
    #print(f"Compare {left} vs {right}")
    if type(left) == int and type(right) == int:
        if left < right:
            #print("True")
            return True
        elif left == right:
            #print("E")
            return "E"
        else:
            #print("False")
            return False
    elif type(left) == int and type(right) == list:
        return recursively_compare([left], right)
    elif type(left) == list and type(right) == int:
        return recursively_compare(left, [right])
    else:
        for count in range(min(len(left), len(right))):
            comparison = recursively_compare(left[count], right[count])
            # print(comparison)
            if comparison == True:
                return True
            elif comparison == "E":
                continue
            else:
                return False

        # If the loop was never entered because a list was empty, make sure it comes first
        if min(len(left), len(right)) == 0 and len(left) != 0:
            return False

        # If looking through everything in the list still hasn't decided our ordering, check the list lengths
        if len(left) > len(right):
            return False
        elif len(left) == len(right):
            return "E"
        else:
            return True

def part_one():
    sum_of_correct_indices = 0
    with open("2022/day13/input.txt", "r") as f:
        lines = f.read().splitlines()
        for count in range(0, len(lines)-1, 3):
            left = ast.literal_eval(lines[count])
            right = ast.literal_eval(lines[count+1])
            left = [[el] for el in left]
            right = [[el] for el in right]
            print(f"left: {left}, right: {right}")
            comparison = recursively_compare(left, right)
            if comparison == "E":
                comparison = True
            if comparison:
                sum_of_correct_indices += (count + 3) // 3
            print(f"{(count + 3) // 3}. {comparison}")

    print(f"sum_of_correct_indices: {sum_of_correct_indices}")

def part_two():
    lists = [[[2]], [[6]]]
    with open("2022/day13/input.txt", "r") as f:
        lines = f.read().splitlines()
        for count in range(0, len(lines)-1, 3):
            left = ast.literal_eval(lines[count])
            right = ast.literal_eval(lines[count+1])
            lists.append([[el] for el in left])
            lists.append([[el] for el in right])

    # bubble sort lists
    for count in range(len(lists)):
        for count2 in range(len(lists) - count - 1):
            if recursively_compare(lists[count2], lists[count2+1]) == False:
                lists[count2], lists[count2+1] = lists[count2+1], lists[count2]
    print(f"Product of divider packets: {(lists.index([[2]])+1)*(lists.index([[6]])+1)}")

if __name__ == "__main__":
    # part_one()
    part_two()
