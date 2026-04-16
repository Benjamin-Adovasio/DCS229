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

    def generate_random_list(self, n: int) -> list[int]:
        """
        This function generates a list of n random integers between 0 and 1000, and returns the list.
        Args: n: the number of random integers to generate
        Returns: a list of n random integers between 0 and 1000
        """
        array: list[int] = [] #array starts as blank
        for element in range(n): #will run n times
            array.append(random.randint(0, 1000)) #random integer between 0-1000

        #I added this for testing purposes, to make sure 42 was in the list
        #if 42 not in array:
        #    array[random.randint(0, n - 1)] = 42

        return array
    
    def linear_search_print(self, arr: Sequence[int], target: int) -> int: 
        """
        This function performs a linear search for the target value in the given array. It prints the number of unsuccessful checks it took to find the target value, and returns the number of checks. If the target value is not found, it prints "Not found." and returns the total number of checks.
        Args: arr: the array to search through, target: the value to search for
        Returns: the number of checks it took to find the target value, or the total number of checks if the target value is not found
        """
        checks = 0 #check count starts at 0
        for value in arr:
            if value == target:
                print("Unsuccessful checks:", checks) 
                return checks
            checks += 1 #adds 1 to the number of checks

        print("Not found.") #Only gets printed if the code doesnt return earlier
        return checks
    

    def linear_search_count(self, arr: Sequence[int], target: int) -> int:
        """
        This function performs a linear search for the target value in the given array. It returns the number of checks it took to find the target value, or the total number of checks if the target value is not found.
        Args: arr: the array to search through, target: the value to search for
        Returns: the number of checks it took to find the target value, or the total number of checks if the target value is not found
        """
        checks = 0
        for value in arr:
            checks += 1
            if value == target:
                return checks 
        return checks
    

    def binary_search_recursive(
        self,
        arr: Sequence[int],
        target: int,
        low: int = 0,
        high: int | None = None,
    ) -> int:
        """
        This function performs a binary search for the target value in the given sorted array. It returns the index of the target value if found, or -1 if not found.
        Args: arr: the sorted array to search through, target: the value to search for
        Returns: the index of the target value if found, or -1 if not found
        """
        if high is None:
            high = len(arr) - 1

        if low > high:
            return -1 #base case: if low is greater than high, the target is not found

        mid = (low + high) // 2 #finds the middle

        if arr[mid] == target: #stops if target found
            return mid #in this case mid would be the index of the target
        elif arr[mid] < target: #either the left or right half of array is then searched
            return self.binary_search_recursive(arr, target, mid + 1, high)
        else:
            return self.binary_search_recursive(arr, target, low, mid - 1)
        
def main(n: int = 1000) -> None:
    """
    This function is the main function that runs the search tests. It generates random lists of integers, performs linear and binary searches, and prints the results.
    Args: n: the number of random integers to generate for the tests (default is 1000)
    Returns: None
    """
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
    index = search.binary_search_recursive(arr, 42) #search for the value 42 using binary search and get the index of 42
    print("Index of 42 in sorted array:", index) #print the index of 42 in the sorted array

    """
    Part 4: Tests

    """
    arr = search.generate_random_list(n) #generate the list of n random integers

    for multiplier in [0.5, 1, 2, 4]: #I used a "multiplier" to avoid rewriting the code for each query
        query_count = int(n * multiplier) 
        queries = []

        for _ in range(query_count):
            queries.append(random.choice(arr))

        # Linear timing
        start = time.perf_counter() #start time is recorded before any of the queries are searched for using linear search
        for q in queries:
            search.linear_search_count(arr, q) #search for each query using linear search on the unsorted array
        end = time.perf_counter() #end time is recorded after all queries have been searched for using linear search
        linear_time = end - start

        # Sorting + Binary timing
        start = time.perf_counter() #start time is recorded before the array is sorted and any of the queries are searched for using binary search
        sorted_arr = sorted(arr) #the array is sorted before the queries are searched for using binary search, but the time it takes to sort the array is included in the total time for this part
        for q in queries:
            search.binary_search_recursive(sorted_arr, q) #search for each query using binary search on the sorted array
        end = time.perf_counter()
        binary_time = end - start 

        print("\nQueries:", query_count)
        print("Linear time:", linear_time)
        print("Sorting + Binary time:", binary_time) 

#  only execute when you run this file directily
if __name__ == "__main__":
    main()
