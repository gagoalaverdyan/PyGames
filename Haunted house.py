def enter_house():
    print('You have entered the haunted house.')
    print('There are three rooms:', ', '.join(objects['rooms']))
    room = input('Which one are you entering?: ')
    enter_room(room)

def enter_room(name, havekey=False):
    if name not in objects['rooms']:
        room = input('You have entered a wrong room name.Try again: ')
        enter_room(room)
    else:
        if name == 'Living room':
            print('You have entered the living room.')
            print('There are three doors:', ', '.join(objects['doors']))
            door = input('Which one are you entering?: ')
            enter_door(door)
        elif name == 'Library':
            print('You have entered the library.')
            print('There are three books:', ', '.join(objects['books']))
            book = input('Which one are you opening?: ')
            read_book(book)
        elif name == 'Basement':
            if not havekey:
                print('The door is locked.')
                enter_house()
            if havekey:
                print('You have found the secret key and entered the basement.')
                print('There are three chests:', ', '.join(objects['chests']))
                chest = input('Which one are you opening?: ')
                open_chest(chest)

def read_book(ord):
    if ord not in objects['books']:
        book = input('You have entered a wrong book order.Try again: ')
        read_book(book)
    else:
        if ord == 'B':
            print('The poisonus bees attacked and killed you.\n G A M E  O V E R')
        if ord == 'C':
            print('You have been frozen in time by the books charms.\n G A M E  O V E R')
        if ord == 'A':
            enter_room('Basement', havekey=True)

def enter_door(color):
    if color not in objects['doors']:
        door = input('You have entered a wrong door color.Try again: ')
        enter_door(door)
    else:
        if color == 'Green':
            print('The spiders attacked and killed you.\n G A M E  O V E R')
        elif color == 'Blue':
            print('You left the house and the door locked behind you.\n G A M E  O V E R')
        elif color == 'Red':
            enter_room('Library')

def open_chest(size):
    if size not in objects['chests']:
        chest = input('You have entered a wrong chest size.Try again: ')
        open_chest(chest)
    else:
        if size == 'Small':
            print('You found the treasure and won! Congratulations!')
        elif size == 'Medium':
            print('You got killed by the trap.\n G A M E  O V E R')
        elif size == 'Large':
            print('The chest was empty.\n G A M E  O V E R')

objects = {
    'rooms': ['Living room', 'Library', 'Basement'],
    'doors': ['Red', 'Green', 'Blue'],
    'books': ['A', 'B', 'C'],
    'chests': ['Large', 'Medium', 'Small']
}

enter_house()