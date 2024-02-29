class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def __str__(self):
        return f'{self.name} {self.description}'