path = input()

with open(path, "r") as file:
    for i in enumerate(file):
        if len(i[1]) > 79:
            print(f'Line {i[0] + 1}: S001 Too long')