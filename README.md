# Advent of Code 2024

Repository for storing the code for [Advent of Code 2024](https://adventofcode.com/2024). 

Rules I impose on myself:
1. Code must not be generated via A.I.
2. When I get stuck for a prolonged amount of time, I can go to reddit for help for hints. But I am not allowed to copy-paste code.
3. Same goes for YouTube. 

Goal is to solve fun programming exercises to improve my coding skills.

## Day 20: ⭐
- [x] Part 1: Quick BFS to get the path. Next, from each point try a cheat of 2 spots.
- [ ] Part 2: in progress.

## Day 19: ⭐⭐
- [x] Part 1: Recursively find all possible patterns. I used the `@cache` from functools for caching the results.
- [x] Part 2: Accidentally solved Part 2 as well.

## Day 18: ⭐⭐
- [x] Part 1: Maze traversal (BFS).
- [x] Part 2: Maze traversal with blockades. I solved it using bruteforce (~5 minutes). Later solved it with binary search: ~0.5s. This way it only does 12 path traversels for my dataset.

## Day 17: ⭐⭐
- [x] Part 1: implement op codes
- [x] Part 2: find some input. Reverse engineered the program into it's components. Did this with help from [HyperNeutrino](https://www.youtube.com/watch?v=y-UPxMAh2N8).

## Day 16: ⭐
- [x] Part 1: Shortest path via Dijkstra's algorithm: BFS + sorted queue with cost
- [ ] Part 2: Find all possible shortest paths. I don't know how to do tackle this one.

## Day 15: ⭐
- [x] Part 1: Move robots that move boxes
- [ ] Part 2: Boxes have size 2. Stuck with this one.

## Day 14: ⭐⭐ 
- [x] Part 1: Position of robots at time step 100
- [x] Part 2: Which time shows a christmas tree?
  - I went for reddit for this one. Approach was to find the second where the safety factor is smallest.

## Day 13: ⭐⭐
- [x] Part 1: Systems of equations. Solved with sympy library.
- [x] Part 2: Same, but with bigger numbers.

## Day 12: ⭐
- [x] Part 1: Find area and perimeter of fences. (BFS)
- [ ] Part 2: Find length of sides of perimeter. Still stuck with this one.

## Day 11: ⭐⭐
- [x] Part 1: Count numbers that have a certain criteria. The list becomes very big very quick.
- [x] Part 2: Much longer list. Python's `Counter` makes short work of this.

## Day 10: ⭐⭐ 
- [x] Part 1: Find number of trails from a starting point: shortest path.
- [x] Part 2: Find number of trails from a starting point: all paths that go from 0 - 9 in a trail. Difference between part1 and part2 is essentially a `set()` replaced with a `list()`

## Day 09: ⭐⭐
- [x] Part 1: Disk defragmenting single digits
- [x] Part 2: Disk defragmenting complete files. This one took me quite some time to get the pointers correct. 
    - [ ] I borked the commits of Part2. Fix later.

## Day 08: ⭐⭐
- [x] Part 1: Tower locations along an axis in a grid.
- [x] Part 2: Same, but slightly more complicated.

## Day 07: ⭐⭐
- [x] Part 1: Find the correct operators: "*" and "+" to get to a solution.
- [x] Part 2: Find the correct operators: "*", "+" and "||". This solution is very slow, but it works. (takes about 3')

## Day 06: ⭐⭐
- [x] Part 1: Traverse grid and count steps of guard.
- [x] Part 2: Introduce loops the security guard will take

## Day 05: ⭐⭐
- [x] Part 1: Check if sorted
- [x] Part 2: Sort according to rules

## Day 04: ⭐⭐
- [x] Part 1: Find "XMAS" string in matrix
```text
..X..
.XMAS
..XSX
```
- [x] Part 2: Find a 'cross':

```text
M.S
.A.
M.S
```

## Day 03: ⭐⭐
- [x] Part 1: Regex find and do `mul(x, y)` 
- [x] Part 2: Same but with added `do()` and `don't()` to do an instruction.

## Day 02: ⭐⭐
- [x] Part 1: Comparing increasing/decreasing lists
- [x] Part 2: Same, but up to one item removed.

## Day 01: ⭐⭐
- [x] Part 1: Sorting and comparing numbers
- [x] Part 2: Finding occurences and multiply
