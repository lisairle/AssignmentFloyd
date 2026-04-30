"""
This module contains a simple performance test which
compares the recursive version of Floyds algorithm with the
imperative version
"""

import sys
sys.path.append('../')
from recursion.recursive_floyd import recursive_floyd_warshall
from iterative.iterative_floyd import iterative_floyd
from time import process_time
from time import perf_counter
from sys import maxsize
NO_PATH =  maxsize

def reset_graph():
    global GRAPH
    GRAPH = [
        [0, 7, NO_PATH, 8],
        [NO_PATH, 0, 5, NO_PATH],
        [NO_PATH, NO_PATH, 0, 2],
        [NO_PATH, NO_PATH, NO_PATH, 0]
    ]

def performance_test(function_handle):
    """
    A function that performs a simple performance test
    function_handle -> The function which is being tested. 
                       It must take no parameters

    Please complete this function
    """
    
    start_time = perf_counter()

    for _ in range(1000):
        reset_graph()
        function_handle()

    end_time = perf_counter()

    print(f"{end_time - start_time:.10f}")
    

print ("Recursion Test Time")
performance_test(recursive_floyd_warshall)

print ("Iterative Test Time")
performance_test(iterative_floyd)

    


