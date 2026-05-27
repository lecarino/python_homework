def make_hangman(secret_word):
    guesses = []
    tries = 6
    def hangman_closure(letter):
        nonlocal tries
        #initilize the word to be printed out whenever user guesses
        word = []
        # Within the inner function, each time it is called, the letter should be appended to the guesses array
        guesses.append(letter)
        print(f"guesses: {guesses}")
        #2 options: if letter in word then we add it into the word: if secret_word is "alphabet", and guesses is ["a", "h"], then "a__ha__" should be printed out
        for char in secret_word:
            if char in guesses:
                word.append(char)
            else:
                word.append("_")

        if letter not in secret_word:
            tries -= 1
            print(f"you have {tries} tries left.")
                
        print("".join(word))

        if "_" not in word:
            print(f"The word was: {secret_word}")
            return True
            
        if tries <= 0:
            return False

    return hangman_closure

# PROGRAM
user_input = input("What's the secret word you want to try out? ")
game = make_hangman(user_input)
while True:
    guess = input("Type a letter as your guess: ")
    status = game(guess)
    if status is True:
        print("YOU WIN")
        break
    elif status is False:
        print("Game Over! You ran out of guesses.")
        break

