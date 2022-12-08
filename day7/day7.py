from pprint import pprint

folders = []

def navigate_to_active_directory(filesystem, active_dir):
    """
    Navigates to the active directory.
    Returns the active directory.
    """
    temp_dir = filesystem
    for index in active_dir:
        temp_dir = temp_dir[index]
    return temp_dir

def search_folder(search, folder_name):
    """
    Searches a folder for a folder with the given name.
    If the folder is found, returns the index of the folder.
    If the folder is not found, returns -1.
    """
    for file in search:
        if type(file) == list:
            if file[0] == folder_name:
                return search.index(file)
    return -1

def create_filesystem():
    with open("day7/input.txt", "r") as f:
        filesystem = [["/"]]
        active_dir = [0]
        data = f.read().splitlines()

        for line in data:
            line=line.split()
            # user-typed command
            if line[0] == "$":
                if line[1] == "cd":
                    if line[2] == "..":
                        active_dir.pop()
                    elif line[2] == "/":
                        active_dir = [0]
                    else:
                        temp_dir = navigate_to_active_directory(filesystem, active_dir)
                        # look for the folder.
                        # if no folder exists with the given name, create it.
                        index = search_folder(temp_dir, line[2])
                        if index > -1:
                            active_dir.append(index)
                        else:
                            temp_dir.append([line[2]])
                            active_dir.append(temp_dir.index([line[2]]))
            # ls output
            else:
                temp_dir = navigate_to_active_directory(filesystem, active_dir)
                if line[0] == "dir":
                    if search_folder(temp_dir, line[1]) == -1:
                        temp_dir.append([line[1]])
                # if not a folder, it is a file with a size
                else:
                    temp_dir.append({"name": line[1],
                                    "size": line[0]})
        return filesystem

def find_folder_sizes(filesystem):
    total_size = 0
    for file in filesystem:
        if type(file) == dict:
            total_size += int(file["size"])
        elif type(file) == list:
            total_size += find_folder_sizes(file)
    folders.append({"name": filesystem[0], "size": total_size})
    return total_size

def part_one():
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

if __name__ == "__main__":
    filesystem = create_filesystem()
    size_used = find_folder_sizes(filesystem[0])

    part_one()
    part_two(size_used)
