secretWord = "happy"

counter = 6

while counter > 0:
    for i in secretWord:
        print("_", end = ' ')
    print('')
    player = input("Geuss a letter: ")
    
    if player in secretWord:
        print("you guessed correctly")
    else: 
        counter -= 1
        print(f"Number of guesses left: {counter}")
        