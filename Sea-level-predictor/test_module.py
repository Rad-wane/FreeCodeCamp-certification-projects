import unittest
import sea_level_predictor
import matplotlib as mpl


# the test case
class LinePlotTestCase(unittest.TestCase):
    def setUp(self):
        self.ax = sea_level_predictor.draw_plot()

    def test_plot_title(self):
        actual = self.ax.get_title()
        expected = "Rise in Sea Level"
        self.assertEqual(actual, expected, "Expected line plot title to be 'Rise in Sea Level'")
    
    def test_plot_labels(self):
        actual = self.ax.get_xlabel()
        expected = "Year"
        self.assertEqual(actual, expected, "Expected line plot xlabel to be 'Year'")
        actual = self.ax.get_ylabel()
        expected = "Sea Level (inches)"
        self.assertEqual(actual, expected, "Expected line plot ylabel to be 'Sea Level (inches)'")
        actual = self.ax.get_xticks().tolist()
        expected = [1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0]
        self.assertEqual(actual, expected, "Expected x tick labels to be '1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0'")

    
    

if __name__ == "__main__":
    unittest.main()
