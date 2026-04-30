# README #

### What is this repository for? ###

This repository contains an assignment project based on the Floyd-Warshall shortest path algorithm.

It includes:

- A recursive implementation in `src/recursion/recursive_floyd.py`
- An iterative implementation in `src/iterative/iterative_floyd.py`
- Unit tests in `src/tests/unittests.py`
- A performance test file in `src/tests/performance_test.py`

* Version: 0.1

### How do I get set up? ###

No external packages are required for this project.

Use Python 3.12 or newer.

If you are running commands from the repository root in PowerShell, set the module path with:

```powershell
$env:PYTHONPATH='src'
```

This allows Python to find the `recursion` and `iterative` modules correctly.

### Running the scripts ###

Run the recursive version:

```powershell
$env:PYTHONPATH='src'; python src/recursion/recursive_floyd.py
```

Run the iterative version:

```powershell
$env:PYTHONPATH='src'; python src/iterative/iterative_floyd.py
```

Run the unit tests:

```powershell
$env:PYTHONPATH='src'; python -m unittest src/tests/unittests.py
```

### Requirements ### 

- Python 3.12+
- No external dependencies
