def generate_number(n):
    n ^= n * 64
    n %= 16777216

    n ^= n // 32
    n %= 16777216

    n ^= n * 2048
    n %= 16777216

    return n


def part1(numbers):
    # numbers = [1, 10, 100, 2024]
    for i in range(len(numbers)):
        for _ in range(2000):
            numbers[i] = generate_number(numbers[i])
    print("Part 1", sum(numbers))


def get_diff(n, num_iter):
    diff = []
    for _ in range(num_iter):
        new_n = generate_number(n)
        last_n = n % 10
        new_n_last = new_n % 10
        diff.append((new_n_last - last_n, new_n_last))

        n = new_n
    return diff


def part2(numbers):
    num_iter = 2000
    to_buy = dict()
    for number in numbers:  # [1,2,3,2024]:
        diffs = get_diff(number, num_iter)
        # Monkey can only remember one sequence of four
        # So track a tuple with last four items
        to_track = set()
        for i in range(len(diffs) - 4):
            pattern = tuple(x[0] for x in diffs[i : i + 4])
            result = diffs[i + 3][1]
            if pattern not in to_track:
                if pattern in to_buy:
                    to_buy[pattern] += result
                else:
                    to_buy[pattern] = result
                to_track.add(pattern)

    # 2108 is too high
    print("Part 2", max(to_buy.values()))


if __name__ == "__main__":
    numbers = [int(item) for item in open("big.txt", "r").readlines()]
    part1(numbers)
    part2(numbers)
