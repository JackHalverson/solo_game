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
        self.options = []
        self.hidden_options = []

    def add_item(self, item, description):
        thing = Item(item, description)
        self.items.append(thing)
        return thing

    def remove_item(self, item: str):
        for i in self.items:
            if i.name == item:
                self.items.remove(i)
                break

    def move_item_to_inventory(self, item: str, player):
        for i in self.items:
            if i.name == item:
                player.inventory.append(i)
                self.items.remove(i)
                break

    def change_item_description(self, item: str, new_description: str):
        for i in self.items:
            if i.name == item:
                i.description = new_description
                break

    def __str__(self):
        return f'{self.name} {self.description}'
    
    def add_option(self, name, description):
        option = Option(name, description)
        self.options.append(option)
        return option
    
    def remove_option(self, option):
        self.options.remove(option)
    
    def change_option_description(self, option: str, new_description):
        for i in self.options:
            if i.name == option:
                i.description = new_description
        for i in self.hidden_options:
            if i.name == option:
                i.description = new_description

    def add_hidden_option(self, name, description):
        option = Option(name, description)
        self.hidden_options.append(option)
        return option
    
    def move_hidden_option_to_options(self, option):
        self.options.append(option)
        self.hidden_options.remove(option)


class Option:
    def __init__(self, name, description):
        self.name = name
        self.description = description