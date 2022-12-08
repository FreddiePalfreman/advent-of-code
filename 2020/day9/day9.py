from itertools import product

def find_first_invalid(preamble):
    with open("2020/day9/input.txt") as f:
        numbers = f.read().splitlines()
        for count in range(preamble, len(numbers)):
            possibilities = list(product(numbers[count-preamble:count], numbers[count-preamble:count]))
            for i in range(0, len(possibilities)-1, preamble):
                possibilities.remove(possibilities[i])
            possibilities = [map(int, i) for i in list(map(list, possibilities))]
            possibilities = list(map(list, possibilities))
            possibilities = list(map(sum, possibilities))
            if int(numbers[count]) not in possibilities:
                return numbers[0:count], numbers[count]

def find_contiguous_set(numbers, target):
    contiguous_sets = []
    # find every contiguous sequence of numbers
    for i in range(0, len(numbers)):
        for j in range(0, len(numbers)):
            contiguous_sets.append(numbers[i:j+1])
    contiguous_sets = list(filter(None, contiguous_sets))
    # find the contiguous sequences that sums to the target
    contiguous_sets = [list(map(int, i)) for i in contiguous_sets]
    contiguous_sets = list(filter(lambda x: sum(x) == int(target), contiguous_sets))

    best_sequence = []
    for i in contiguous_sets:
        if sum(i) < sum(best_sequence) or best_sequence == []:
            best_sequence = i

    print(min(best_sequence)+max(best_sequence))



if __name__ == "__main__":
    numbers, target = find_first_invalid(25)
    find_contiguous_set(numbers, target)