def play_game():

    print("Welcome to Treasure Hunt!")
    print("Solve riddles to find the treasure!\n")

    # First Riddle
    print("You are in a forest.")
    print("Riddle: I speak without a mouth and hear without ears. What am I?")

    while True:
        answer = input("Your answer: ").lower()

        if answer == "echo":
            print("Correct! Moving ahead...\n")
            break
        else:
            print("Wrong! Try again.")

    # Second Riddle
    print("You entered a dark cave.")
    print("Riddle: The more you take, the more you leave behind. What am I?")

    while True:
        answer = input("Your answer: ").lower()

        if answer == "footsteps":
            print("Correct! Moving ahead...\n")
            break
        else:
            print("Wrong! Try again.")

    # Third Riddle
    print("You reached a river.")
    print("Riddle: What has to be broken before you can use it?")

    while True:
        answer = input("Your answer: ").lower()

        if answer == "egg":
            print("Correct! You found the treasure!")
            break
        else:
            print("Wrong! Try again.")


if __name__ == "__main__":
    play_game()
