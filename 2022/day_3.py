def day_3_input(filename):
    with open(filename) as itemLists_file:
        itemLists = itemLists_file.readlines()
    itemLists1 = [[elem.strip()[:len(elem)//2], elem.strip()[len(elem)//2:]] for elem in itemLists]
    return [elem.strip() for elem in itemLists], itemLists1

def find_duplicates(rucksack):
    duplicates = list(set(rucksack[0])&set(rucksack[1]))
    for i, dup in enumerate(duplicates):
        if dup.islower():
            duplicates[i] = ord(dup) - 96
        else:
            duplicates[i] = ord(dup) - 38
    return duplicates

def sum_all_duplicates(rucksacks):
    duplicates = []
    for rucksack in rucksacks:
        duplicates += find_duplicates(rucksack)
    return sum(duplicates)

def find_common_letter(rucksackTrio):
    common_letter = list(set(rucksackTrio[0])&set(rucksackTrio[1])&set(rucksackTrio[2]))
    for i, dup in enumerate(common_letter):
        if dup.islower():
            common_letter[i] = ord(dup) - 96
        else:
            common_letter[i] = ord(dup) - 38
    return common_letter

def browse_all_trios(rucksacks):
    badges = []
    for i in range(3, len(rucksacks)+1, 3):
        badges += find_common_letter(rucksacks[i-3:i])
    return sum(badges)

rucksacks, semirucksacks = day_3_input('C:\\Users\\romai\\Documents\\GitHub\\bookish-lamp\\2022\\day_3_input.txt')
print(sum_all_duplicates(semirucksacks))
print(browse_all_trios(rucksacks))