import heapq

def day_1_input(filename):
    with open(filename) as calories_file:
        calories = calories_file.readlines()
    calories_per_elf = []
    buffer = []
    for item in calories:
        if item == '\n':
            calories_per_elf.append(buffer)
            buffer = []
        else:
            buffer.append(int(item.strip()))
    return calories_per_elf

def sum_calories_per_elf(calories_per_elf):
    for i, carried_calories in enumerate(calories_per_elf):
        calories_per_elf[i] = sum(carried_calories)
    return calories_per_elf

calories_per_elf = day_1_input('day_1_input.txt')
calories_per_elf = sum_calories_per_elf(calories_per_elf)
print(max(calories_per_elf))
print(sum(heapq.nlargest(3, calories_per_elf)))
