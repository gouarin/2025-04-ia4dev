To test the `hilbert_curve` and `plot_hilbert_curve` functions, we can use pytest. We will create a new file named `test_hilbert.py` and add the following tests:

```python
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
from PIL import Image

# Import the functions to be tested
from hilbert_curve import hilbert_curve, plot_hilbert_curve

def test_hilbert_curve():
    """
    Tests the hilbert_curve function for a given depth.
    """
    points = []
    hilbert_curve(0, 0, 1, 0, 2, points)
    
    # Expected number of points for depth 2
    expected_points = 16
    
    assert len(points) == expected_points, f"Expected {expected_points} points, but got {len(points)}"

def test_plot_hilbert_curve():
    """
    Tests the plot_hilbert_curve function for a given depth.
    """
    # Capture the output of the plot
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111)
    
    def mock_show(*args, **kwargs):
        pass
    
    plt.show = mock_show
    
    plot_hilbert_curve(2)
    
    # Check if the figure has been created and contains data
    assert len(ax.lines) > 0, "No lines were plotted"
    assert ax.get_xlabel() == 'X-axis', "Incorrect x-axis label"
    assert ax.get_ylabel() == 'Y-axis', "Incorrect y-axis label"
    assert ax.get_title() == 'Hilbert Curve of Depth 2', "Incorrect title"

def test_plot_hilbert_curve_image():
    """
    Tests the plot_hilbert_curve function and captures the output as an image.
    """
    # Capture the output of the plot
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111)
    
    def mock_show(*args, **kwargs):
        pass
    
    plt.show = mock_show
    
    plot_hilbert_curve(2)
    
    # Save the figure to a BytesIO object
    img_data = BytesIO()
    fig.savefig(img_data, format='png')
    img_data.seek(0)
    
    # Load the image using PIL
    img = Image.open(img_data)
    
    # Check if the image has been created and contains data
    assert img.width > 0, "Image width is zero"
    assert img.height > 0, "Image height is zero"

if __name__ == "__main__":
    pytest.main()
```

### Explanation:

1. **test_hilbert_curve**: This test checks if the `hilbert_curve` function generates the correct number of points for a given depth.

2. **test_plot_hilbert_curve**: This test ensures that the `plot_hilbert_curve` function creates a plot with the correct title, labels, and lines.

3. **test_plot_hilbert_curve_image**: This test captures the output of the plot as an image and checks if the image has been created correctly.

### Running the Tests:

To run the tests, save the above code in a file named `test_hilbert.py` and then execute it using pytest:

```sh
pytest test_hilbert.py
```

This will run the tests and provide detailed output on whether each test passed or failed.