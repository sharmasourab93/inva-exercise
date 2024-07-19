# You are given a multi-dimensional array of integers
# representing a terrain elevation map.
#
# height_map = [
#     [1, 4, 3, 1, 3, 2],
#     [3, 2, 1, 3, 2, 4],
#     [2, 3, 3, 2, 3, 1]
# ]
#
# Each element of the array represents the height of a unit of land.
# You need to write a Python function to calculate the total volume of water
# that can be trapped between the land units.
#
# The elevation map is represented by a 2D array height_map where
# height_map[i][j] represents the height of the land unit at row i and column j.
# Water can only be trapped in locations where there is a depression
# between adjacent land units.
#
# Write a function
# calculate_water_volume(height_map: List[List[int]]) -> int
# that takes the height_map as input and returns the total volume of trapped water.
#
# You need to implement the logic for calculating
# the trapped water volume without copying solutions
# directly from the internet or using external libraries.
from typing import List


def calculate_water_volume_util(linear_map: List[int]) -> int:
    """
    Calculate Water Volume util on the given
    linear_map/matrix in between the trappments.
    """

    volume = 0

    for i in range(1, len(linear_map)):
        # Keep a note of Left catchment
        left = linear_map[i]
        for j in range(i):
            left = max(left, linear_map[j])

        # Keep a note of right catchment
        right = linear_map[i]

        for j in range(i+1, len(linear_map)):
            right = max(right, linear_map[j])

        volume = volume + (min(left, right) - linear_map[i])

    return volume


def calculate_water_volume(height_map: List[List[int]]) -> int:

    volume = 0

    for i in range(len(height_map)):
        volume += calculate_water_volume_util(height_map[i])

    return volume


if __name__ == '__main__':
    height_map = [
            [1, 4, 3, 1, 3, 2],
            [3, 2, 1, 3, 2, 4],
            [2, 3, 3, 2, 3, 1]
        ]
    result = calculate_water_volume(height_map)
    print(result)
