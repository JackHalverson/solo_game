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
option3 = room.add_option("Examine desks", f"The desks are cluttered with papers and office supplies. there are notes that refer a project called {bold(text_color.purple('Leap'))}. There is also a newspaper that catches your eye, The headline reads: {bold('Avaant Industries: The Future of Technology')}. \n you also notice a small key sticking out between some papers.")
option4 = room.add_hidden_option("Check door", "You approach the door and attempt to open it but it's locked. You notice a small keyhole.")
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
            room.move_item_to_room("key", player)
            room_loop = True
    else:
        printn(italic(text_color.red("Invalid choice.")))
        print()

    time.sleep(1)
        

printn("you look around the hallway. There are two doors, one to your left and one to your right. you also see bulletin board further down on the wall")

room2 = Room("Hallway", "You are in a dimly lit hallway.")

#options for room2
option1 = room2.add_hidden_option("Look around", "you look around the hallway. There are two doors, one to your left and one to your right. you also see bulletin board further down on the wall")
option2 = room2.add_option("Check left door", "You walk up to the left door and try to open it but it's locked. You notice a small keypad next to the door.")
option3 = room2.add_option("Check right door", f"You walk up to the right door and try to open it but it's locked. there is a small screen by the door with the number {text_color.blue("0")}")
option4 = room2.add_option("Look at bulletin board", "you walk up to the bulletin board and see a few notices and a flyer.")
option5 = room2.add_hidden_option("Take employee notice", "you take the employee notice from the bulletin board. you also notice a sticky note that was under the bulletin board.")
option6 = room2.add_hidden_option("Look at flyer", "it appears to be a flyer about an upcoming food drive. it's not very interesting.")
option7 = room2.add_hidden_option("Grab sticky note", "you pull the sticky note off of the bulletin board.")


#items for room2
item1 = room2.add_item("employee notice", f"notice to employees: \n\nPlease be advised that the company will be conducting standard maintenance and testing procedures on January 10th. As a result, the building will be temporarily closed on that day.\nWe apologize for any inconvenience this may cause. Please ensure that all personal belongings are secured before leaving the premises.\n\n-Management")
item2 = room2.add_item("sticky note", f"the sticky note reads: {italic(text_color.yellow("the door code is: 1985   Dont forget again Jeff!"))} {text_color.green("whoever left this note must have been forgetful")}")

room_loop = False

while not room_loop:
    clear()

    print(room2.description)
    print()
    for option in room2.options:
        printn(text_color.cyan("- " + option.name))
    print()

    choice = input("Choose an option: ").lower()
    print()

    if choice == "quit":
        break

    for option in room2.options:
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
        room2.remove_option(option1)
        room2.move_hidden_option_to_options(option2)
        room2.move_hidden_option_to_options(option3)
        room2.move_hidden_option_to_options(option4)
    
    elif choice == option2.name.lower():
        printn(text_color.blue("ENTER CODE:"))
        imput_code = input()
        if imput_code == "1985":
            room_loop = True
            print()
            printn(italic(text_color.green("code accepted.")))
            printn("You hear a click. The door unlocks and you walk through.")
        else:
            print()
            printn(italic(text_color.red("Invalid code.")))
        
    elif choice == option3.name.lower():
        pass

    elif choice == option4.name.lower():
        room2.remove_option(option4)
        room2.move_hidden_option_to_options(option5)
        room2.move_hidden_option_to_options(option6)

    elif choice == option5.name.lower():
        room2.move_item_to_inventory("employee notice", player)
        room2.remove_option(option5)
        room2.move_hidden_option_to_options(option7)

    elif choice == option6.name.lower():
        room2.remove_option(option6)
    
    elif choice == option7.name.lower():
        room2.move_item_to_inventory("sticky note", player)
        room2.remove_option(option7)
    
    else:
        printn(italic(text_color.red("Invalid choice.")))
        print()
    
    time.sleep(1)