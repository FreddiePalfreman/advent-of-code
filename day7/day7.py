from pprint import pprint
import sys

folders = []

def create_filesystem():
    with open("day7/input.txt", "r") as f:
        filesystem = [["/"]]
        active_dir = [0]
        data = f.read().splitlines()

        for line in data:
            line=line.split()
            if line[0] == "$":
                if line[1] == "cd":
                    if line[2] == "..":
                        active_dir.pop()
                    elif line[2] == "/":
                        active_dir = [0]
                    else:
                        #go to given directory
                        temp_dir = filesystem
                        for index in active_dir:
                            temp_dir = temp_dir[index]
                        found = False
                        for file in temp_dir:
                            if type(file) == list:
                                if file[0] == line[2]:
                                    found = True
                                    active_dir.append(temp_dir.index(file))
                        if not found:
                            temp_dir.append([line[2]])
                            active_dir.append(temp_dir.index([line[2]]))
                elif line[1] == "ls":
                    pass

            # output from ls command
            else:
                temp_dir = filesystem
                for index in active_dir:
                    temp_dir = temp_dir[index]
                if line[0] == "dir":
                    found = False
                    for file in temp_dir:
                        if type(file) == list:
                            if file[0] == line[1]:
                                found = True
                    if not found:
                        temp_dir.append([line[1]])
                else:
                    temp_dir.append({"name": line[1],
                                    "size": line[0]})
        return filesystem

def recursive_file_sizes(filesystem):
    total_size = 0
    for file in filesystem:
        if type(file) == dict:
            total_size += int(file["size"])
        elif type(file) == list:
            total_size += recursive_file_sizes(file)
    folders.append({"name": filesystem[0], "size": total_size})
    return total_size

def part_one(filesystem):
    total = 0
    for folder in folders:
        if folder["size"] < 100000:
            total += folder["size"]
    print("Part 1:", total)

def part_two(total_size_used):
    space_to_free = -(70000000 - total_size_used - 30000000)
    best_candidate = {"name": "", "size": -1}
    for folder in folders:
        if folder["size"] > space_to_free:
            if folder["size"] < best_candidate["size"] or best_candidate["size"] == -1:
                best_candidate = folder
    print("Part 2:", best_candidate)

filesystem = create_filesystem()
size_used = recursive_file_sizes(filesystem[0])

part_one(filesystem)
part_two(size_used)
