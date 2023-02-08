from random import randint

words = ["happy", "jake", "amber", "chelsea", "mady", "monor", "josiah", "adam", "drew", "brande"]

secret_word = "chelsea"

def Convert_list(string):
    l = []
    l[:0] = string
    return l

secret_word_list = Convert_list(secret_word)

counter = 6
for i in secret_word:
    print("_", end = ' ')
print('')

num_correct_letters = 0

correct_letters = []



while counter > 0:
    letters_guessed_correctly = 0
    print("")
    player = input("Guess a letter: ")
    
    if player in secret_word:
        print("You guessed correctly")
        correct_letters.append(player)
        # print("correct list:", correct_letters)

        # guessed_word = False

        # for letter in secret_word:
        #     if letter not in correct_letters:
        #         break 
            

        # you know you have won if you hit here
        # break


            # if letter in correct_letters:
            #     # do something   
            #     num = 1 + 1
            # else:
            #     continue       
        # print("I didn't continue")

        # if correct_letters => all in secretWord
        
    else: 
        counter -= 1
        print(f"Number of guesses left: {counter}")

    for letter in secret_word:            
        if letter in correct_letters: # and letter == :
            letters_guessed_correctly += 1
            print(letter, end = ' ')
        else:
            print("_", end = ' ')

    if letters_guessed_correctly == len(secret_word):
        print("")
        print("You win!")
        break
print("The word was", secret_word)
    
        