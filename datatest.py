import unittest
from data import get_team_name


class DataTests(unittest.TestCase):

    def test_team_name(self):
        print("test")
        self.assertEqual(get_team_name(
            "Gençlerbirliği Ankara SK (4)"), "Gençlerbirliği Ankara SK")


if __name__ == "__main__":
    unittest.main()