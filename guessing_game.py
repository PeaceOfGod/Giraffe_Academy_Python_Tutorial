secret_word = "Giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
print("You have just 3 Trials, Are you set???")
while guess != secret_word and not(out_of_guesses):
    if(guess_count < guess_limit):
        guess = str(input("Enter your guess here: "))
        guess_count += 1
    else:
        out_of_guesses = True
    #print("Your Guess is Wrong, Try Again!")
if out_of_guesses:
    print("Out of Guesses, YOU LOSE!")
else:
    print("YOU WIN!")
