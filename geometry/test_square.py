from square import makeRect, rectArea
import pytest

@pytest.fixture
def grid():
    return [makeRect(1,1), makeRect(2,2),makeRect(1,2)]

def test_grid(grid):
    assert len(grid) == 3
    assert rectArea(grid[0]) == 1
