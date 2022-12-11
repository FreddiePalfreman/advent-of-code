import re
from math import floor, prod

class Monkey:
    def __init__(self, name, items, operation, test, true_throw, false_throw):
        self.name = name
        self.items = items
        self.test = test
        self.modulo = 0
        self.operation = operation
        self.true_throw = true_throw
        self.false_throw = false_throw
        self.inspection_count = 0

    def inspect_item(self, old):
        #print(f"\t{self.name} inspects {old}")
        new = eval(self.operation, {"old": old})
        #print(f"\t  Worry level changed from {old} to {new}")
        #new = floor(new/3)
        #print(f"\t  Worry level divided to three to {new}")
        new = new % self.modulo
        if (new % self.test) == 0:
            #print(f"\t  Current worry level is divisible by {self.test}")
            #print(f"\t  Item with worry level {new} is thrown to {self.true_throw.name}")
            self.true_throw.items.append(new)
        else:
            #print(f"\t  Current worry level is not divisible by {self.test}")
            #print(f"\t  Item with worry level {new} is thrown to {self.false_throw.name}")
            self.false_throw.items.append(new)

    def inspect_all_items(self):
        self.inspection_count += len(self.items)
        for item in self.items:
            self.inspect_item(item)
        self.items = []

def instantiate_monkeys():
    monkeys = []
    with open("2022/day11/input.txt") as f:
        lines = f.read().splitlines()
        for count in range(len(lines)):
            line = lines[count]
            if re.match(r'Monkey \d', line):
                name = re.findall(r'(\d)', line)[0]
                items = list(map(int, re.findall(r': (.*)', lines[count+1].strip())[0].split(", ")))
                operation = re.findall(r'= (.*)', lines[count+2].strip())[0]
                divisor = int(re.findall(r'\d+', lines[count+3].strip())[0])
                if_true = int(re.findall(r'\d+', lines[count+4].strip())[0])
                if_false = int(re.findall(r'\d+', lines[count+5].strip())[0])
                monkey = Monkey(name, items, operation, divisor, if_true, if_false)
                monkeys.append(monkey)
            count += 7

    mods = []
    for monkey in monkeys:
        print(f"monkey {monkey.name}: {monkey.items}")
        mods.append(monkey.test)
    common_multiple = prod(mods)
    print(mods, common_multiple)

    for monkey in monkeys:
        monkey.true_throw = monkeys[monkey.true_throw]
        monkey.false_throw = monkeys[monkey.false_throw]
        monkey.modulo = common_multiple

    return monkeys

def simulate_rounds(monkeys, no_rounds):
    for i in range(no_rounds):
        print(f"\nROUND {i}")
        for monkey in monkeys:
            monkey.inspect_all_items()

def calculate_monkey_business(monkeys):
    print("CALCULATING MONKEY BUSINESS")
    inspections = []
    for monkey in monkeys:
        inspections.append(monkey.inspection_count)
    print(inspections)
    inspections.sort(reverse=True)
    return inspections[0] * inspections[1]


if __name__ == "__main__":
    monkeys = instantiate_monkeys()
    simulate_rounds(monkeys, 10000)
    print(f"\nMONKEY BUSINESS: {calculate_monkey_business(monkeys)}")