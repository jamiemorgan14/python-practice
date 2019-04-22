secret_word = "hello"
guess = ""
max_guesses = 3
guesses = 0
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guesses < max_guesses:
        guess = input("Enter guess: ")
        guesses += 1
        print(f"{guesses} guesses")
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, you lose!")
else:
    print("You win!")
