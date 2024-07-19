# Write a unit test for  Multi-dimensional Array Manipulation (Advanced Python)

import pytest
from ex_2 import calculate_water_volume_util, calculate_water_volume


@pytest.fixture(scope="function")
def height_map():
    return [
        [1, 4, 3, 1, 3, 2],
        [3, 2, 1, 3, 2, 4],
        [2, 3, 3, 2, 3, 1]
    ]


@pytest.fixture(scope="function")
def height_map_data_split(request, height_map):
    return height_map[request.param]


@pytest.mark.parametrize("height_map_data_split, result", [(0, 2), (1, 4), (2, 1)],
                         indirect=["height_map_data_split"])
def test_calculate_water_volume_util(height_map_data_split, result):
    assert calculate_water_volume_util(height_map_data_split) == result


def test_calculate_water_volume(height_map):

    assert calculate_water_volume(height_map) == 7

