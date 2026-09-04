import unittest
from dataclasses import dataclass
from pathlib import Path

from pystruct import normalize


@dataclass
class User:
    name: str


class NormalizeTests(unittest.TestCase):
    def test_containers(self):
        self.assertEqual(normalize({"x": (1, 2), "y": {3, 1}}), {"x": [1, 2], "y": [1, 3]})

    def test_dataclass_and_path(self):
        self.assertEqual(normalize(User("medu")), {"name": "medu"})
        self.assertEqual(normalize(Path("a/b")), "a/b")


if __name__ == "__main__":
    unittest.main()
