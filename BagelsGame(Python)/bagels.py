import random

MAX_GUESSES=10

def main():
    play_again="yes"
    while play_again!="no":
        print('<------------------Bagels, a deductive logic game.---------------------->')
        print('''
        I am thinking of a 3-digit number. Try to guess what it is.
        
        Here are some clues:
        
        When I say:     That means:
         Pico            One digit is correct but in the wrong position.
         Fermi           One digit is correct and in the right position.
         Bagels          No digit is correct.
        
        I have thought up a number.
        
        You have 10 guesses to get it.
        ''')

        rand_num=str(random.randrange(100,1000))
        print(rand_num)

        right_status_count=0 #To check if atleast one of the digit position is correct.
        has_digit_status=False #To check if any digit exists in guess statement although position is not correct.
        guess="" #For user input

        for i in range(1,MAX_GUESSES+1):
            while True:
                guess=input(f'Guess #{i}: ')
                if len(guess)!=3:
                    print("Please enter a 3 digit number!")
                else:
                    try:
                        guess=int(guess)
                        break
                    except ValueError:
                        print("Please enter a 3 digit number!")

            guess=str(guess)
            for j in range(3):
                if rand_num[j]==guess[j]: # Check if individual positions are correct and maintain a count.
                    right_status_count+=1
                elif guess[j] in rand_num: # Check if the specific digit is atleast present in random number or not.
                    has_digit_status=True

            # The logic as per clues above.
            if right_status_count==3:
                print("You got it!")
                break
            elif right_status_count>0:
                print("Fermi")
            elif has_digit_status:
                print("Pico")
            else:
                print("Bagels")

            # Reset the status for next loop round.
            right_status_count=0
            has_digit_status=False

        play_again=str(input("Do you want to play again? (yes or no)\n> "))

    print("Thanks for playing!")

if __name__ == '__main__':
    main()
