def calculate_score_part_1(round):
    score = 0
    # rock
    if round[2] == "X":
        score += 1
        if round[0] == "A":
            score += 3
        elif round[0] == "C":
            score += 6
    # paper
    elif round[2] == "Y":
        score += 2
        if round[0] == "A":
            score += 6
        elif round[0] == "B":
            score += 3
    # scissors
    elif round[2] == "Z":
        score += 3
        if round[0] == "B":
            score += 6
        elif round[0] == "C":
            score += 3
    return score

def calculate_score_part_2(round):
    score = 0
    # lose
    if round[2] == "X":
        score += 0
        if round[0] == "A":
            score += 3
        elif round[0] == "B":
            score += 1
        else:
            score += 2
    # draw
    elif round[2] == "Y":
        score += 3
        if round[0] == "A":
            score += 1
        elif round[0] == "B":
            score += 2
        else:
            score += 3
    # win
    elif round[2] == "Z":
        score += 6
        if round[0] == "A":
            score += 2
        elif round[0] == "B":
            score += 3
        else:
            score += 1
    return score



def calculate_strategy_score():
    overall_score = 0
    with open("day2/input.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            overall_score += calculate_score_part_2(line)
        return overall_score

print(calculate_strategy_score())