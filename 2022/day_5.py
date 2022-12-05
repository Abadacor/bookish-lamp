def day_5_alternative_input(filename):
    with open(filename) as f:
        head = [next(f) for x in range(8)]
    crates = ['' for _ in range(9)]
    for j, elem in enumerate(head):
        for i in range(9):
            if elem[i*4+1] != ' ':
                crates[i] = elem[i*4+1] + crates[i]

    with open(filename) as f:
        instructions = f.readlines()
        instructions = [ins.strip() for ins in instructions[10:]]
        for j, ins in enumerate(instructions):
            instructions[j] = [int(i) for i in ins.split() if i.isdigit()]

    return [[*crate] for crate in crates], instructions

def day_5_input(filename):
    #process current state of crates
    with open(filename) as f:
        head = [next(f) for x in range(9)]
        head = head[::-1]
        for i, elem in enumerate(head):
            if i == 0:
                head[i] = list(map(int,head[i].split()))
            else:
                head[i] = head[i].replace('[', '')
                head[i] = head[i].replace(']', '')
                head[i] = head[i].replace('    ', '.')
                head[i] = head[i].replace(' ', '')
                head[i] = [*head[i].strip()]
    stacks = []
    for i in range(9):
        buffer = []
        for item in head[1:]:
            if item[i] != '.':
                buffer.append(item[i])
        stacks.append(buffer)

    #process instructions
    with open(filename) as f:
        instructions = f.readlines()
        instructions = [ins.strip() for ins in instructions[10:]]
        for j, ins in enumerate(instructions):
            instructions[j] = [int(i) for i in ins.split() if i.isdigit()]
    return stacks, instructions 

def process_instruction_p1(stacks, instruction):
    for i in range(instruction[0]):
        stacks[instruction[2]-1].append(stacks[instruction[1]-1].pop())
    return stacks

def process_all_instructions_p1(stacks, instructions):
    for instruction in instructions:
        stacks = process_instruction_p1(stacks, instruction)
    return stacks

def process_instruction_p2(stacks, instruction):
    buffer = []
    for i in range(instruction[0]):
        buffer.append(stacks[instruction[1]-1].pop())
    stacks[instruction[2]-1] += buffer[::-1]
    return stacks

def process_all_instructions_p2(stacks, instructions):
    for instruction in instructions:
        stacks = process_instruction_p2(stacks, instruction)
    return stacks

#stacks, instructions = day_5_input('/home/romain/Documents/advent_of_code/2022/day_5_input.txt')
#stacks = process_all_instructions_p2(stacks, instructions)
stacks, instructions = day_5_alternative_input('/home/romain/Documents/advent_of_code/2022/day_5_input.txt')
stacks = process_all_instructions_p2(stacks, instructions)
for elem in stacks:
    print(elem)