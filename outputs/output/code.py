import matplotlib.pyplot as plt

# Set the backend to 'Agg' to avoid interactive plotting issues
plt.switch_backend('Agg')

def generate_hilbert_curve(depth):
    """
    Generate the Hilbert curve coordinates for a given depth.

    Parameters:
    - depth: An integer representing the recursion depth (order) of the Hilbert curve.

    Returns:
    - A list of tuples containing the coordinates of the Hilbert curve points.
    """
    if depth == 0:
        return [(0, 0)]

    n = 2 ** depth
    points = []
    for i in range(n * n):
        binary_str = format(i, f'0{2*depth}b')
        reversed_first_half = binary_str[:depth][::-1]
        x_binary = reversed_first_half + binary_str[depth:]
        y_binary = binary_str[:depth] + binary_str[depth:][::-1]
        x = int(x_binary, 2)
        y = int(y_binary, 2)
        points.append((x, y))

    return points

def plot_hilbert_curve(coordinates):
    """
    Plot the Hilbert curve with matplotlib.

    Parameters:
    - coordinates: A list of tuples containing the Hilbert curve points.
    """
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.plot([x for x, y in coordinates], [y for x, y in coordinates], marker='o', linestyle='-')
    ax.set_xlabel('X Coordinate')
    ax.set_ylabel('Y Coordinate')
    ax.set_title('Hilbert Curve')

    # Save the plot to a file instead of displaying it
    plt.savefig('hilbert_curve.png')

# Test cases
test_cases = [
    (0, [(0, 0)]),
    (1, [(0, 0), (1, 0), (1, 1), (0, 1)]),
    (2, [(0, 0), (1, 0), (1, 1), (0, 1), (0, 2), (1, 2), (1, 3), (0, 3)]),
    (3, [(0, 0), (2, 0), (2, 1), (0, 1), (0, 3), (2, 3), (2, 2), (0, 2)])
]

for depth, expected in test_cases:
    coordinates = generate_hilbert_curve(depth)
    plot_hilbert_curve(coordinates)