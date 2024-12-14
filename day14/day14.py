import re
from tqdm import tqdm

def quadrants(dataset_size):
    # Q1
    q1 = [0, dataset_size[0] // 2, 
          0, dataset_size[1] // 2]

    q2 = [dataset_size[0] // 2+1, dataset_size[0], 
          0, dataset_size[1] // 2]
     
    q3 = [0, dataset_size[0] // 2, 
          dataset_size[1] // 2 +1, dataset_size[1]]

    q4 = [dataset_size[0] // 2+1, dataset_size[0], 
          dataset_size[1] // 2+1, dataset_size[1]]
    return [q1, q2, q3, q4]

def part1(seconds):
    dataset_size = (103, 101)
    locations = {}
    dataset = load_data()
    for px, py, vx, vy in dataset:

        npx = px + vx*seconds
        npy = py + vy*seconds

        px = npx % dataset_size[1]
        py = npy % dataset_size[0]

        if (px, py) in locations:
            locations[(px, py)] += 1
        else:
            locations[(px, py)] = 1

    safety_factor = 1
    for q in quadrants(dataset_size):
        robots_in_quadrant = 0
        for y in range(q[0], q[1]):
            for x in range(q[2], q[3]):
                if (x, y) in locations:
                    robots_in_quadrant += locations[(x,y)]
        safety_factor *= robots_in_quadrant
    print("Part 1", safety_factor)
    # print_robot(dataset_size, locations)

def load_data():
    dataset = []
    for line in open("big.txt").readlines():
        px, py, vx, vy = map(int, re.findall(r"-?\d+", line))
        dataset.append((px, py, vx, vy))
    return dataset

def part2():
    map_size = (103, 101)

    min_safety = float("inf")
    min_seconds = 0
    dataset = load_data()
    for second in tqdm(range(103*101)):
        locations = {}
        for px, py, vx, vy in dataset:
            npx = px + vx*second
            npy = py + vy*second

            px = npx % map_size[1]
            py = npy % map_size[0]

            if (px, py) in locations:
                locations[(px, py)] += 1
            else:
                locations[(px, py)] = 1

        safety_factor = 1
        for q in quadrants(map_size):
            robots_in_quadrant = 0
            for y in range(q[0], q[1]):
                for x in range(q[2], q[3]):
                    if (x, y) in locations:
                        robots_in_quadrant += locations[(x,y)]
            safety_factor *= robots_in_quadrant
        if safety_factor < min_safety:
            min_safety = safety_factor
            min_seconds = second
    print(f"Part 2 {min_seconds} seconds, min safety:{min_safety}")
    


def print_robot(dataset_size, locations):
    print("size", dataset_size)
    for y in range((dataset_size[0])):
        for x in range((dataset_size[1])):
            if (x, y) in locations:
                print(locations[(x, y)], end="")
            else:
                print(".", end="")
        print()
    print()

if __name__ == "__main__":
    part1(100)
    part2()