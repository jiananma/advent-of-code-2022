from util import process_input



def puzzle1():
    lines = process_input("day4_input.txt")
    count = 0
    for line in lines:
        assignment1 = line.split(",")[0]
        assignment2 = line.split(",")[1]
        start1 = int(assignment1.split("-")[0])
        end1 = int(assignment1.split("-")[1])
        start2 = int(assignment2.split("-")[0])
        end2 = int(assignment2.split("-")[1])
        if start1 <= start2 and end1 >= end2:
            count += 1
        elif start1 >= start2 and end1 <= end2:
            count += 1
    print(count)


def puzzle2():
    lines = process_input("day4_input.txt")
    count = 0
    for line in lines:
        assignment1 = line.split(",")[0]
        assignment2 = line.split(",")[1]
        start1 = int(assignment1.split("-")[0])
        end1 = int(assignment1.split("-")[1])
        start2 = int(assignment2.split("-")[0])
        end2 = int(assignment2.split("-")[1])
        start_min = min(start1, start2)
        start_max = max(start1, start2)
        end_min = min(end1, end2)
        end_max = max(end1, end2)
        if start_max <= end_min:
            count += 1
    print(count)


if __name__ == "__main__":
    print("start")
    # puzzle1()
    puzzle2()
