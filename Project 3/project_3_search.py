######################################
# DCS 229 -- Project 3: Search
# Date: March 4, 2026
# Name: Benjamin Adovasio
# Resources Used: 
# https://pressbooks.palni.org/anopenguidetodatastructuresandalgorithms/chapter/search/
# 
##########################################

import random #to generate the 100 random values
import time #for part 4, to calculae total time
from collections.abc import Sequence

#I decided to put all 4 functions into one class to keep it organized 
class Search:

    """
    This function generates the list of random integers.
    """
    def generate_random_list(self, n: int) -> list[int]:
        array: list[int] = [] #array starts as blank
        for element in range(n): #will run n times
            array.append(random.randint(0, 1000)) #random integer between 0-1000

        #I added this for testing purposes, to make sure 42 was in the list
        #if 42 not in array:
        #    array[random.randint(0, n - 1)] = 42

        return array
    
    """
    This funciton preforms a search on the list for the target value, and prints the number of checks it took to find the target.
    """
    def linear_search_print(self, arr: Sequence[int], target: int) -> int: 
        checks = 0 #check count starts at 0
        for value in arr:
            if value == target:
                print("Unsuccessful checks:", checks) 
                return checks
            checks += 1 #adds 1 to the number of checks

        print("Not found.") #Only gets printed if the code doesnt return earlier
        return checks
    
    """
    This function is the same as the previous one, but instead of printing the number of checks, it returns the number of checks. 
    """
    def linear_search_count(self, arr: Sequence[int], target: int) -> int:
        checks = 0
        for value in arr:
            checks += 1
            if value == target:
                return checks 
        return checks
    
    """
    This function uses recursive searching.
    """
    def binary_search_recursive(
        self,
        arr: Sequence[int],
        target: int,
        low: int,
        high: int,
    ) -> int:
        if low > high:
            return -1 #base case: if low is greater than high, the target is not found

        mid = (low + high) // 2 #finds the middle

        if arr[mid] == target: #stops if target found
            return mid #in this case mid would be the index of the target
        elif arr[mid] < target: #either the left or right half of array is then searched
            return self.binary_search_recursive(arr, target, mid + 1, high)
        else:
            return self.binary_search_recursive(arr, target, low, mid - 1)
        
def main() -> None:
    search = Search() #search object to call Search() class

    """
    Part 1: Linear search on 100 integers
    """
    arr = search.generate_random_list(100) #generate the list of 100 random integers
    search.linear_search_print(arr, 42) #search for the value 42 using linear search and print the number of checks it took to find 42

    """
    Part 2: Same as 1, but return number of checks
    """
    total = 0
    tests = 100

    for _ in range(tests):
        arr = search.generate_random_list(100) #generate the list of 100 random integers
        total += search.linear_search_count(arr, 42) #search for the value 42 using linear search and add the number of checks it took to find 42 to the total
    print("Average number of checks for 100 tests:", total / tests) #print the average number of checks it took to find 42 for 100 tests

    """
    Part 3: Uses the recursive search
    """
    arr = sorted(search.generate_random_list(100)) #generate the list of 100 random integers and sort it for binary search
    index = search.binary_search_recursive(arr, 42, 0, len(arr) - 1) #search for the value 42 using binary search and get the index of 42
    print("Index of 42 in sorted array:", index) #print the index of 42 in the sorted array

    """
    Part 4: Tests

    At what number of queries does Sorting + Binary Search start to show an advantage over Linear Search?:
    Sorting + binary search shows an advantage at around 500 queries
    """
    n = 1000
    arr = search.generate_random_list(n) #generate the list of n random integers

    for multiplier in [0.5, 1, 2, 4]: #I used a "multiplier" to avoid rewriting the code for each query
        query_count = int(n * multiplier) 
        queries = []

        for _ in range(query_count):
            queries.append(random.choice(arr))

        # Linear timing
        start = time.perf_counter()
        for q in queries:
            search.linear_search_count(arr, q)
        end = time.perf_counter()
        linear_time = end - start

        # Sorting + Binary timing
        start = time.perf_counter()
        sorted_arr = sorted(arr)
        for q in queries:
            search.binary_search_recursive(sorted_arr, q, 0, len(sorted_arr) - 1)
        end = time.perf_counter()
        binary_time = end - start

        print("\nQueries:", query_count)
        print("Linear time:", linear_time)
        print("Sorting + Binary time:", binary_time) 

#  only execute when you run this file directily
if __name__ == "__main__":
    main()
