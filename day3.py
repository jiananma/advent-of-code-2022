from util import process_input


def char_value(char):
    if ord(char) in range(65, 91):
        return ord(char) - 64 + 26
    elif ord(char) in range(97, 123):
        return ord(char) - 96
    else:
        raise Exception("not a valid char")


def partition(lst, size):
    for i in range(0, len(lst), size):
        yield lst[i : i + size]


def puzzle1():
    lines = process_input("day3_input.txt")
    prio = []
    for line in lines:
        left = line[: len(line) // 2]
        right = line[len(line) // 2 :]
        common = set(left).intersection(set(right)).pop()
        prio.append(char_value(common))
    print(sum(prio))


def puzzle2():
    lines = process_input("day3_input.txt")
    prio = []
    for group in partition(lines, 3):
        group_sets = [set(s) for s in group]
        common = set.intersection(*group_sets).pop()
        prio.append(char_value(common))
    print(sum(prio))


if __name__ == "__main__":
    print("start")
    puzzle2()
