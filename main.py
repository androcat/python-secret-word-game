secretWord = "happy"

counter = 6
for i in secretWord:
    print("_", end = ' ')
print('')

correctLetters = []

while counter > 0:
   
    player = input("Geuss a letter: ")
    
    if player in secretWord:
        print("You guessed correctly")
        correctLetters.append(player)
        print("correct list:", correctLetters)
        for letter in secretWord:
            if letter in correctLetters: # and letter == :
                print(letter, end = ' ')
            else:
                print("_", end = ' ')
        print('')
   
    else: 
        counter -= 1
        print(f"Number of guesses left: {counter}")
        