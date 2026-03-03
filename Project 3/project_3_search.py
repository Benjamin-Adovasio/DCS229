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
    

    def linear_search_count(self, arr, target):
        checks = 0
        for value in arr:
            checks += 1
            if value == target:
                return checks
        return checks
    


### write your tests in main function
def main():
    pass

#  only execute when you run this file directily
if __name__ == "__main__":
    main()