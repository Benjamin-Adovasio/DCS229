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

#### Write your class here
def generate_random_list(n):
    data = []
    for _ in range(n):
        data.append(random.randint(0, 1000))

    if 42 not in data:
        data[random.randint(0, n - 1)] = 42

    return data


### write your tests in main function
def main():
    pass

#  only execute when you run this file directily
if __name__ == "__main__":
    main()