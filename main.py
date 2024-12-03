import random  # to get random numbers

def rollDice():
    while True:  # keep asking until the user wants to stop playing
        try:
            numDice = int(input("Enter the number of dice to roll (1-10): "))
            if numDice >= 1 and numDice <= 10:  # Ensure number is between 1 and 10
                break
            else:
                print("Enter a valid number that is between 1 and 10.")
        except ValueError:
            print("Error. You must enter a number.")

    print(f"\nRolling {numDice} dice: ")
    result = [random.randint(1, 6) for i in range(numDice)]
    print("Results:", result)

    return input("\nDo you want to roll again? (Yes or No): ")

def main():
    print("Welcome to the Dice Rolling game")
    while True:
        userChoice = rollDice()
        if userChoice != 'y' and userChoice != 'yes':
            print("Thanks for using the Dice Rolling Simulator. Goodbye!")
            break

if __name__ == "__main__":
    main()