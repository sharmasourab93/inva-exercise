# InvaSystem - Exerices 



1. Write a code to generate 1000 random numbers using threading
   ```python
   import threading
   ```
   Solution in `ex_1.py`


2. You are given a multi-dimensional array of integers representing a terrain elevation map.

height_map = [
    [1, 4, 3, 1, 3, 2],
    [3, 2, 1, 3, 2, 4],
    [2, 3, 3, 2, 3, 1]
]

Each element of the array represents the height of a unit of land. You need to write a Python function to calculate the total volume of water that can be trapped between the land units.

The elevation map is represented by a 2D array height_map where height_map[i][j] represents the height of the land unit at row i and column j. Water can only be trapped in locations where there is a depression between adjacent land units.

Write a function calculate_water_volume(height_map: List[List[int]]) -> int that takes the height_map as input and returns the total volume of trapped water.

You need to implement the logic for calculating the trapped water volume without copying solutions directly from the internet or using external libraries.

Solution in `ex_2.py` 

3. Write a unit test for  Multi-dimensional Array Manipulation (Advanced Python) problem mentioned earlier
   Solution in `test_ex_2.py`

4. Write code to take a csv file , which contains sensor data in columns , build a ETL pipeline to extract column values , find central tendencies of column  values and store all these values in a new csv file , 
use pyspark only , where pipeline runs parallely  
  Solution not attempted.

5. Create a sample api which takes path of csv file as input and return central tendencies if success
    Solution in `ex_4.py`

6. Create fibonacci series with recursive function for 10 numbers
    Fibonacci sequence:
    0
    1
    1
    2
    3
    5
    8
    13
    21
    34
   Solution in `ex_6.py`

7. Create a module with about code where input will be numbers to be generated and output will be array of fibonacci numbers
    Solution in `ex_7.py`.
