# Expense 8 Puzzle Problem Solver

This project is a Python-based implementation of a modified version of the classic 8 puzzle problem, known as the "Expense 8 Puzzle Problem." In this puzzle, you are given a 3x3 grid with 8 tiles placed on it, and your goal is to rearrange the tiles from a starting configuration to a desired configuration. The twist in this version is that each tile's number also represents the cost associated with moving that tile.

## Usage

To run the solver, use the following command line invocation:

```
main.py <start-file> <goal-file> <method> <dump-flag>
```

- `<start-file>` and `<goal-file>` are required input files that specify the initial and target configurations.
- `<method>` can be one of the following search methods:
  - `bfs`: Breadth First Search
  - `ucs`: Uniform Cost Search
  - `dfs`: Depth First Search
  - `dls`: Depth Limited Search (Extra Credit for CSE 4308 students)
  - `ids`: Iterative Deepening Search (Extra Credit for CSE 4308 students)
  - `greedy`: Greedy Search
  - `a*`: A* Search (Default if no method is given)
- `<dump-flag>` is optional and can be set to `true` to dump a search trace for analysis in a file named `trace-<date>-<time>.txt`.

## Input Files

Both the start file and goal file should follow the format shown in the sample files included in this project.

### Sample Start file
```
2 8 3
1 6 4
7 0 5
```

### Sample Goal file
```
1 2 3
8 0 4
7 6 5
```

## Output Format

The solver provides the following output:

- Number of nodes popped
- Number of nodes expanded
- Number of nodes generated
- Maximum fringe size
- Solution depth and cost
- A sequence of steps to reach the solution

Here's an example output for the A* search with a dump flag set to `true`:

```
Nodes Popped: 97
Nodes Expanded: 64
Nodes Generated: 173
Max Fringe Size: 77
Solution Found at depth 12 with a cost of 63.
Steps:
    Move 7 Left
    Move 5 Up
    Move 8 Right
    Move 7 Down
    Move 5 Left
    Move 6 Down
    Move 3 Right
    Move 2 Right
    Move 1 Up
    Move 4 Up
    Move 7 Left
    Move 8 Left
```

