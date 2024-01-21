# N-Queens Visualizer

Welcome to the N-Queens Visualizer, a Python program that helps you visualize the solution to the classic N-Queens problem. This program generates and displays solutions for the N-Queens puzzle, allowing one to visualize the recursive nature of the problem!

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/nofqueensvisualizer.git
   cd nofqueensvisualizer
2. **Install Dependencies:**
   ```bash
   pip3 install -r requirments.txt

## Usage

Once the installation is complete, you can run the visualizer by running the following from terminal:
```bash
python3 main.py
```
This will launch the program and a solution will generate automatically, if you would like a new solution, press the spacebar!

## Recurrence

The N-Queens problem is often solved using a recursive approach that relies on a recurrence relationship. The recurrence relationship defines how solutions for larger instances of the problem can be built upon solutions for smaller instances. In the context of the N-Queens problem, the recurrence relationship is formulated to find a valid placement of queens on an N×N chessboard. We use backtracking to accomplish this (or 'trying' different possibilites and undoing these possibilites depending on the integrity of the solution). 

1. **Base Case:**
   The base case of the recursion is reached when any particular row is reached at our designated N, i.e, a valid placement of a queen for the entire board has been found.

2. **Recursive Hypothesis:**
   Our hypothesis then assumes that there are given solutions for a smaller input than N, therefore, the placement of N queens is also determined as it scales.

3. **Recursive Step:**
   The next step is to advance the algorithm when considering a board larger than a designated N (N+1). Given the solutions nature: It stands to reason that the solution should recursively call itself for each next row of      valid placement, where N is moved to N+1 until the base case is eventually reached.

## Contributing
Whether its a pull request or open issue: please feel free to contribute!
