print("Hello so, lets Start The Game :\nYou Have Only 10 Guesses for getting a correct no.\n")
for i in range(10):
    print("Sir Guess a Number please :-")
    #n=27
    a=int(input(" "))
    if a==18:
         print("Congratulations! Sir You guessed the Right")
    elif a<18:
        print("You guess is less than right number!\nPlease try again\nGuess left :"+str(10-i))
    elif a>18:
        print("You guess is greater than right number!\nPlease try again\nGuess left :"+str(10-i))
    if i==9:
        print("Sorry!You are out of Guesses")
