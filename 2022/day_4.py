def day_4_input(filename):
    with open(filename) as f:
        data = [y for y in [x.split(",") for x in f.read().splitlines()]]
        data = [(tuple(map(int, x.split("-"))), tuple(map(int, y.split("-")))) for x,y in data]
    return data

def find_full_overlap(data):
    overlap = lambda r1,r2: r1.issubset(r2) or r2.issubset(r1)
    return sum(overlap(set(range(x[0],x[1]+1)), set(range(y[0],y[1]+1))) for x,y in data)


def find_overlap(data):
    return sum(len(set(range(x[0],x[1]+1)) & set(range(y[0],y[1]+1))) > 0 for x,y in data)

data  = day_4_input('C:\\Users\\romai\\Documents\\GitHub\\bookish-lamp\\2022\\day_4_input.txt')
print(find_full_overlap(data))
print(find_overlap(data))
