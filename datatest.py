import unittest
from data import *


class DataTests(unittest.TestCase):

    def test_team_name(self):
        self.assertEqual(get_team_name(
            "Gençlerbirliği Ankara SK (4)"), "Gençlerbirliği Ankara SK")
    
    def test_data_as_matrix(self):
        data = ft_to_numbers(teams_to_numbers(getdatalist()))
        self.assertEqual(get_data_as_matrix(data)[0], [0, 9, -1])


if __name__ == "__main__":
    unittest.main()