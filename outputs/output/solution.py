# imports
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import pytest

def generate_hilbert_curve(depth):
    """
    Generate the coordinates of a Hilbert curve at a given depth.

    Parameters:
    depth (int): The depth of the Hilbert curve. Higher depths result in more complex curves.

    Returns:
    list: A list of tuples representing the (x, y) coordinates of the Hilbert curve.
    """
    if depth == 0:
        return [(0, 0)]

    # Recursive call for smaller depth
    sub_curve = generate_hilbert_curve(depth - 1)

    # Calculate new points based on the previous curve and direction
    n = len(sub_curve)
    half_n = n // 2

    # Rotate and translate to form the new curve
    rotated = [(y, -x) for x, y in sub_curve]
    translated = [(x + half_n, y + half_n) for x, y in rotated]

    # Combine all parts of the curve
    curve = translated + [(x + n, y) for x, y in reversed(sub_curve)] + \
            [(x + n, y - n) for x, y in sub_curve] + [(x, y - n) for x, y in reversed(translated)]

    return curve

def plot_hilbert_curve(curve):
    """
    Plot the Hilbert curve using matplotlib.

    Parameters:
    curve (list): A list of tuples representing the (x, y) coordinates of the Hilbert curve.
    """
    x_coords = [point[0] for point in curve]
    y_coords = [point[1] for point in curve]

    plt.figure(figsize=(8, 8))
    plt.plot(x_coords, y_coords, 'b-', linewidth=2)
    plt.title('Hilbert Curve')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.axis('equal')
    plt.grid(True)
    plt.show()

# Example usage
depth = 3
hilbert_curve = generate_hilbert_curve(depth)
plot_hilbert_curve(hilbert_curve)

# Tests
def test_generate_hilbert_curve():
    # Test for depth 0
    assert generate_hilbert_curve(0) == [(0, 0)]

    # Test for depth 1
    expected_depth_1 = [(0, 0), (1, 0), (1, 1), (0, 1)]
    assert generate_hilbert_curve(1) == expected_depth_1

    # Test for depth 2
    expected_depth_2 = [
        (0, 0), (1, 0), (1, 1), (0, 1),
        (0, 2), (1, 2), (1, 3), (0, 3),
        (2, 3), (2, 2), (3, 2), (3, 3),
        (3, 1), (2, 1), (2, 0), (3, 0)
    ]
    assert generate_hilbert_curve(2) == expected_depth_2

def test_plot_hilbert_curve():
    # Capture the plot output
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111)

    def mock_show(*args, **kwargs):
        pass

    with pytest.raises(SystemExit) as excinfo:
        with patch('matplotlib.pyplot.show', new=mock_show):
            plot_hilbert_curve([(0, 0), (1, 0), (1, 1), (0, 1)])

    assert excinfo.type == SystemExit
    assert excinfo.value.code == 0

if __name__ == "__main__":
    pytest.main()
