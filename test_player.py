import unittest
from player import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Living Room", "A cozy living room")

    def test_add_item(self):
        self.room.add_item("Book")
        self.assertEqual(self.room.items, ["Book"])

    def test_remove_item(self):
        self.room.add_item("Book")
        self.room.remove_item("Book")
        self.assertEqual(self.room.items, [])

    def test_str(self):
        self.assertEqual(str(self.room), "Living Room A cozy living room")

if __name__ == '__main__':
    unittest.main()