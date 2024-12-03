import unittest
from unittest.mock import patch
from mylib.logic import wiki  


class TestWikiFunction(unittest.TestCase):
    @patch("mylib.logic.wikipedia.summary")
    def test_wiki(self, mock_summary):
        mock_summary.return_value = "Fanta Cake is a delicious dessert"

        result = wiki(name="Fanta Cake", length=1)

        mock_summary.assert_called_once_with("Fanta Cake", 1)
        self.assertEqual(result, "Fanta Cake is a delicious dessert")


if __name__ == "__main__":
    unittest.main()