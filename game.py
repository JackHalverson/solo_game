from player import Room, Item, Player
from text import text_speed, text_color, text_effects
from utility import Utility
import time

mapping = {
    "printn": text_speed.print_normal,
    "prints": text_speed.print_slow,
    "bold": text_effects.bold,
    "italic": text_effects.italic,
    "clear": Utility.clear_screen
}

printn = mapping["printn"]
prints = mapping["prints"]
bold = mapping["bold"]
italic = mapping["italic"]
clear = mapping["clear"]

clear()

printn("You wake up in an empty office the blue light from your monitor piercing your eyes, you faintly make out some text on the monitor:")
print()
printn(bold(text_color.blue('"RESET COMPLETE"')))
print()
printn("As you strain your mind, attempting to recall any detail, it becomes increasingly evident that your memory is blank, devoid even of your own name. With no other immediate course of action, you decide to explore your surroundings.")
time.sleep(2)

room = Room("Office", "You are in an empty office.")
player = Player("Player")

option1 = room.add_option("Look around", f"As you look around you notice that most of tables and computers are covered in a fine layer of dust as if no one has been here for months. At the end of the room there stands a large grey door with logo reading:\n{bold(text_color.purple(' "Avaant Industrys"'))}")
option2 = room.add_option("Check out monitor", f"The monitor displays the message: \n{bold(text_color.blue("RESET COMPLETE"))}\nYou have no idea what this means.")
option3 = room.add_option("Examine desks", f"The desks are cluttered with papers and office supplies. there are notes that refure a project called {bold(text_color.purple('Leap'))}. There is also a newspapers that catches your eye, The headline reads: {bold('Avaant Industries: The Future of Technology')}. \n you also notice a small key sticking out between some papers.")
option4 = room.add_hidden_option("Check door", "You approach the door and atempt to open it but it's locked. You notice a small keyhole.")
option5 = room.add_hidden_option("Take newspaper", f"You pick up the newspaper that caught your eye")
option6 = room.add_hidden_option("Pick up key", "You pick up the key that was hidden between the papers.")
option7 = room.add_hidden_option("Look at sticky note", f"the sticky note reads: {italic(text_color.yellow( "Type 'i' to check your inventory"))} whatever that means.")

item1 = room.add_item("key", "A small silver key with the letter 'A' engraved on it.")
item2 = room.add_item("newspaper", "Avaant Industries: Shaping the Future of Technology\n\nFounded just five years ago, Avaant Industries has quickly risen to prominence\nas a trailblazer in technological innovation. With a steadfast commitment to\npushing boundaries and challenging the status quo, Avaant has become\nsynonymous with cutting-edge solutions that redefine the possibilities of \ntomorrow.\n\nUnder the visionary leadership of CEO Jameson Dan, Avaant Industries continues\nto chart a course towards a future where technology seamlessly integrates\ninto every aspect of our lives. In a recent statement, Jameson expressed\nexcitement about the company's upcoming endeavors, hinting at groundbreaking\ndevelopments poised to revolutionize industries worldwide.")

room_loop = False

while not room_loop:
    clear()

    print(room.description)
    print()
    for option in room.options:
        printn(text_color.cyan("- " + option.name))
    print()

    choice = input("Choose an option: ").lower()
    print()

    if choice == "quit":
        break

    for option in room.options:
        if choice == option.name.lower():
            printn(option.description)
            print()
            break

    if choice == "i":
        if len(player.inventory) == 0:
            printn("You have no items.")
            print()
            time.sleep(2)
            continue
        else:
            clear()
            printn("You have:")
            print()
            for item in player.inventory:
                printn(text_color.green("> " + item.name))
            print()
                
            item_choice = input("Choose an item to investigate: ").lower()
            print()
            for item in player.inventory:
                if item_choice == item.name.lower():
                    printn((text_color.green(item.description)))
                    print()
                    input("Press enter to continue")
                    break
    
    elif choice == option1.name.lower():
        room.move_hidden_option_to_options(option4)
        room.remove_option(option1)
        

    elif choice == option2.name.lower():
        room.move_hidden_option_to_options(option7)
        room.remove_option(option2)

    elif choice == option3.name.lower():
        room.move_hidden_option_to_options(option5)
        room.move_hidden_option_to_options(option6)
        room.remove_option(option3)
    
    elif choice == option5.name.lower():
        room.move_item_to_inventory("newspaper", player)
        room.remove_option(option5)
    
    elif choice == option6.name.lower():
        room.move_item_to_inventory("key", player)
        room.change_option_description("Check door", "You walk up to the door, and seeing the small keyhole you unlock the door and walk through.")
        room.remove_option(option6)

    elif choice == option7.name.lower():
        room.remove_option(option7)

    elif choice == "check door":
        if item1 in player.inventory:
            room.remove_item("key")
            room_loop = True
    else:
        printn(italic(text_color.red("Invalid choice.")))
        print()

    time.sleep(1)
        
