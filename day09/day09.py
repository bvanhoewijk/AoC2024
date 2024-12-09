from pprint import pprint
import copy
def part1(dataset):
    res = []
    id = 0
    for i, item in enumerate(dataset):
        if (i+1) % 2 == 0:
            for _ in range(item):
                res.append(".")
        else:
            for _ in range(item):
                res.append(id)
            id += 1

    for i, item in enumerate(res):
        if item == ".":
            last = res.pop()
            while last == ".":
                last = res.pop()
            res[i] = last

    result = 0
    for i, item in enumerate(res):
        result += i * item
    print("Part1",result)


def print_blocks(blocks):
    for block in blocks:
        if block['gap']:
            print("." * block['size'], end="")
        else:
            print(str(block['id']) * block['size'], end="")
    print()

def part2(dataset):
    blocks = []
    id = 0
    for i, item in enumerate(dataset):
        block = {}
        if (i+1) % 2 == 0:
            # for _ in range(item):
            #     res.append(".")
            block['gap'] = True
            block['size'] = len(range(item))
            block['id'] = None
            block['done'] = False
        else:
            block['gap'] = False
            block['size'] = len(range(item))
            block['id'] = id
            block['done'] = False
            id += 1
        blocks.append(block)
    # pprint(blocks)
    print_blocks(blocks)

    seen = set()
    blocks_copy = copy.deepcopy(blocks)

    for i, block in enumerate(blocks):
        if block['gap']:
            print_blocks(blocks)
            to_place = blocks.pop()
                       
            while to_place['gap']:
                to_place = blocks.pop()

            if to_place['size'] <= block['size']:
                blocks[i] = to_place
                size = block['size'] - to_place['size']
            else:
                print("Can't place ", to_place["id"])
                seen.add(to_place['id'])
                # blocks.append({"gap": False, "size" : to_place['size'], "id": to_place['id']})

        else:
            # Not a gap:
            seen.add(block['id'])

    print_blocks(blocks)


if __name__ == "__main__":
    dataset = [list(map(int, list(line))) for line in open("big.txt", "r").readlines()][0]
    part1(dataset)
    # part1(list(map(int, list("2333133121414131402"))))
    part2(list(map(int, list("2333133121414131402"))))
