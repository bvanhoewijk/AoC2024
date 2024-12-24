from pprint import pprint
def part1():
    a, b = "".join(open("big.txt").readlines()).split("\n\n")
    connects = [x.split(" ") for x in b.split("\n")]

    states_dict = dict()
    for state in [(x.split(": ")[0], int(x.split(": ")[1])) for x in a.split("\n")]:
        states_dict[state[0]] = state[1]

    while connects:
        todo = connects.pop(0)
        in1, op, in2, _, out = todo[0], todo[1], todo[2], todo[3], todo[4]
        if in1 in states_dict and in2 in states_dict:
            if op == "AND":
                states_dict[out] = states_dict[in1] & states_dict[in2]
            elif op == "XOR":
                states_dict[out] = states_dict[in1] ^ states_dict[in2]
            elif op == "OR":
                states_dict[out] = states_dict[in1] | states_dict[in2]
        else:
            connects.append(todo)

    solution = ""
    z_keys = [val for val in states_dict.keys() if val.startswith("z")]
    for key in sorted(z_keys, reverse=True):
        solution += str(states_dict[key])
    print("Part 1", int(solution, 2))

def main():
    # part1()
    a, b = "".join(open("big.txt").readlines()).split("\n\n")
    connects = [x.split(" ") for x in b.split("\n")]

    states_dict = dict()
    for state in [(x.split(": ")[0], int(x.split(": ")[1])) for x in a.split("\n")]:
        states_dict[state[0]] = state[1]

    while connects:
        todo = connects.pop(0)
        in1, op, in2, _, out = todo[0], todo[1], todo[2], todo[3], todo[4]
        if in1 in states_dict and in2 in states_dict:
            if op == "AND":
                states_dict[out] = states_dict[in1] & states_dict[in2]
            elif op == "XOR":
                states_dict[out] = states_dict[in1] ^ states_dict[in2]
            elif op == "OR":
                states_dict[out] = states_dict[in1] | states_dict[in2]
        else:
            connects.append(todo)

    solutionx = ""
    solutiony = ""
    solutionz = ""

    x_keys = [val for val in states_dict.keys() if val.startswith("x")]
    for key in sorted(x_keys, reverse=True):
        solutionx += str(states_dict[key])
    y_keys = [val for val in states_dict.keys() if val.startswith("y")]
    for key in sorted(y_keys, reverse=True):
        solutiony += str(states_dict[key])
    z_keys = [val for val in states_dict.keys() if val.startswith("z")]
    for key in sorted(z_keys, reverse=True):
        solutionz += str(states_dict[key])
    
    xandy = str(bin(int(solutionx, 2) + int(solutiony, 2)))
    z_only = str(bin(int(solutionz, 2)))
    print(xandy, z_only, end="\n", sep="\n")
    for i, item in enumerate(list(xandy)):
        if list(z_only)[i] != list(xandy)[i]:
            print(len(xandy) - (i), xandy[i]) 

    # 0b110010100111111011 011111 0 011 011100011011100110
    # 0b110010101011111011 100000 0 100 011100011011100110
    
# 0b1010110
# 0011100011011100110

if __name__ == "__main__":
    main()