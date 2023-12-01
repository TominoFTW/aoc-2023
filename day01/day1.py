print("*********************************")
print("\tAOC 2023 - Day 01")
print("*********************************")


with open('input.txt') as f:
    lines = f.read().splitlines()


# Part 1
def Part1():
    first = 0
    second = 0
    last = False

    sum = 0

    for line in lines:
        for char in line:
            if char.isdigit() and not first:
                first = char
            elif char.isdigit() and first:
                second = char
                last = True
            
        if not last:
            second = first
        sum += (int(first) * 10 + int(second))
        first = 0
        second = 0
        last = False

    return sum


# Part 2
def Part2():
    first = 0
    second = 0
    last = False

    sum = 0
    for line in lines:
        line = line.replace('one', 'o1ne').replace('two', 't2wo').replace('three', 't3hree').replace('four', 'f4our').replace('five', 'f5ive').replace('six', 's6ix').replace('seven', 's7even').replace('eight', 'e8ight').replace('nine', 'n9ine')

        for char in line:
            if char.isdigit() and not first:
                first = char
            elif char.isdigit() and first:
                second = char
                last = True

        if not last:
            second = first

        sum += (int(first) * 10 + int(second))
        first = 0
        second = 0
        last = False
    
    return sum

sum


if __name__ == '__main__':
    print(Part1())
    print(Part2())
