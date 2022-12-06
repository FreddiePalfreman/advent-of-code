def solution(distinct_characters):
    with open("day6/input.txt", "r") as f:
        buffer = list(f.read())
        print("PARSING")
        for count in range(0, len(buffer)):
            print(set(buffer[count:count+distinct_characters]))
            if len(set(buffer[count:count+distinct_characters])) == distinct_characters:
                print(f"{distinct_characters} unique characters first found at pos. {count+distinct_characters}")
                break

solution(14)