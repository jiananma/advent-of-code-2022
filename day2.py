from util import process_input

MAPPING = {
    "A X": 1 + 3,
    "A Y": 2 + 6,
    "A Z": 3 + 0, 
    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 1 + 6,
    "C Y": 2 + 0, 
    "C Z": 3 + 3
    }

MAPPING2 = {
    "A X": 3 + 0,
    "A Y": 1 + 3,
    "A Z": 2 + 6, 
    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 2 + 0,
    "C Y": 3 + 3, 
    "C Z": 1 + 6
    }


def puzzle1():
    lines = process_input("day2_test.txt")
    print(sum([MAPPING[l] for l in lines]))
    print(sum([MAPPING2[l] for l in lines]))


if __name__ == "__main__":
    print("start")
    puzzle1()
