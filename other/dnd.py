import random

def explore():
    print("You explore the dungeon and come across a monster!")
    monster_hp = random.randint(10, 20)
    print(f"The monster has {monster_hp} hit points.")
    while monster_hp > 0:
        attack = input("Do you attack the monster? (y/n) ")
        if attack.lower() == "y":
            damage = random.randint(1, 10)
            print(f"You deal {damage} damage to the monster.")
            monster_hp -= damage
        else:
            print("You run away from the monster!")
            return
    print("You defeat the monster!")

def main():
    print("Welcome to the dungeon!")
    while True:
        action = input("What do you want to do? (explore, quit) ")
        if action.lower() == "explore":
            explore()
        elif action.lower() == "quit":
            print("Thanks for playing!")
            return
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
