from util import process_input


def puzzle1():
    lines = process_input("day1_input.txt")
    elves = []
    current_cal = 0
    for line in lines:
        if line != "":
            current_cal += int(line)
        else:
            elves.append(current_cal)
            current_cal = 0

    elves.append(current_cal)

    elves.sort()
    print(elves[-1])
    print(sum(elves[-3:]))


if __name__ == "__main__":
    print("start")
    puzzle1()
