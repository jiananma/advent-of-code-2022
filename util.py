def process_input(filename):
    with open(filename, 'r') as file:
        raw = file.readlines()
        temp = [line.rstrip('\n') for line in raw]
    return temp