######################################
# DCS 229 -- Project 3: Search
# Date: March 4, 2026
# Name: Benjamin Adovasio
# Resources Used: 
# https://pressbooks.palni.org/anopenguidetodatastructuresandalgorithms/chapter/search/
# 
##########################################
# import statement to support more type hints
from __future__ import annotations

import random #to generate the 100 random values
import time #for part 4, to calculae total time


class Search:

    """
    This function generates the list of random integers.
    """
    def generate_random_list(self, n):
        data = []
        for _ in range(n):
            data.append(random.randint(0, 1000))

        if 42 not in data:
            data[random.randint(0, n - 1)] = 42

        return data
    
    """
    This funciton preforms a search on the list for the target value, and prints the number of checks it took to find the target.
    """
    def linear_search_print(self, arr, target):
        checks = 0
        for value in arr:
            if value == target:
                print("Unsuccessful checks:", checks)
                return checks
            checks += 1

        print("Not found.")
        return checks
    
    """
    This function pre
    """
    def linear_search_count(self, arr, target):
        checks = 0
        for value in arr:
            checks += 1
            if value == target:
                return checks
        return checks
    

    def binary_search_recursive(self, arr, target, low, high):
        if low > high:
            return -1

        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return self.binary_search_recursive(arr, target, mid + 1, high)
        else:
            return self.binary_search_recursive(arr, target, low, mid - 1)
        
def main():
    search = Search() #search object to call Search() class

    """
    Part 1: Implement a Linear Search in your language of choice [Python]. Use the following plan to test your implementation on an array [Python List] of 100 randomly generated values (in random order). Randomly generate 100 values, and use Linear Search to find the value 42. Have your search print the number of unsuccessful checks before finding the value 42 (or reporting not found). 
    """
    arr = search.generate_random_list(100) #generate the list of 100 random integers
    search.linear_search_print(arr, 42) #search for the value 42 using linear search and print the number of checks it took to find 42

    """
    Part 2: Take the search function from exercise 1, and modify it to count and return the number of checks Linear Search takes to find the value 42 in a random array. Write a loop to repeat this experiment 100 times, and average the number of checks it takes to find a specific value. What is that number close to? How does it change if you increase the number of tests from 100 to 1,000?
    """
    total = 0
    tests = 100

    for _ in range(tests):
        arr = search.generate_random_list(100) #generate the list of 100 random integers
        total += search.linear_search_count(arr, 42) #search for the value 42 using linear search and add the number of checks it took to find 42 to the total
    print("Average number of checks for 100 tests:", total / tests) #print the average number of checks it took to find 42 for 100 tests

    """
    Part 3: The reasoning used to determine the time complexity of Binary Search closely resembles similar arguments from chapter 2 on recursion. Implement Binary Search as a recursive algorithm by adding extra parameters for the high and low variables. Make sure your function is tail-recursive to facilitate tail-call optimization.
    """
    arr = sorted(search.generate_random_list(100)) #generate the list of 100 random integers and sort it for binary search
    index = search.binary_search_recursive(arr, 42, 0, len(arr) - 1) #search for the value 42 using binary search and get the index of 42
    print("Index of 42 in sorted array:", index) #print the index of 42 in the sorted array

    """
    Part 4: With your implementations of Linear and Binary Search, write some tests to generate a number of random queries. Calculate the total time to conduct n/2 queries on a randomly generated dataset. Be sure to include the sorting time for your Binary Search database before calculating the total time for all queries. Compare your result to the Linear Search total query time. Next, repeat this process for n, 2*n, and 4*n queries. At what number of queries does Sorting + Binary Search start to show an advantage over Linear Search?
    """
    
#  only execute when you run this file directily
if __name__ == "__main__":
    main()