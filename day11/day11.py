from collections import Counter

def blink(dataset, num_blinks):
    
    all_counter = Counter(dataset)
    # We only have to deal with each **type** of number and count that occurence. 
    # So we can use a counter :-).
    for blink in range(num_blinks):
        counter = Counter()
        for item, count in all_counter.items():
            item_str = str(item)
            if item == 0:
                counter[1] += count
            elif len(item_str) % 2 == 0:
                a = int(item_str[0:len(item_str)//2])
                b = int(item_str[len(item_str)//2:])
                counter[a] += count
                counter[b] += count
            else:
                counter[item * 2024] += count
        all_counter = counter
    return all_counter


def part2(dataset):
    pass

if __name__ == "__main__":
    # dataset = "510613 358 84 40702 4373582 2 0 1584".split(" ")
    dataset = [int(item) for item in open("big.txt", "r").readlines()[0].split(" ")]
    print("Part1", blink(dataset, 25).total())
    print("Part2", blink(dataset, 75).total())