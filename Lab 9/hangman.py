from random import randint


def generate_word():

    number_of_words = 0
    word_list = []
    filename = 'dictionary.txt'
    with open(filename, "r") as f:
        for word in f:
            number_of_words += 1
            word = word.rstrip()
            word_list.append(word)

    answer = ""
    while len(answer) < 5:
        x = randint(0, number_of_words - 1)
        answer = word_list[x]

    return answer


def generate_answer_list(word):

    word_list = []
    for i in word:
        word_list.append(i)

    return word_list


def initial_guess_state(x):

    asterix = '*'
    print("The word has", x, 'letters')
    guess_state = asterix * x
    print(guess_state)
    return guess_state


def user_guess():
    letter_guess = str(input("Guess a letter \n"))
    while len(letter_guess) > 1 or len(letter_guess) == 0:
        print("Only Single Letters Please!")
        letter_guess = str(input("Guess a letter \n"))
    return letter_guess.lower()


def right_guess(letter, guess_state, answer_list):
    print('Congratulations, your guess was correct!')
    for i in range(len(answer_list)):
        if letter == answer_list[i]:
            guess_state = guess_state[:i] + letter + guess_state[i+1:]
    print('You currently have the following:', guess_state)
    return guess_state


def wrong_guess(lives, letter, bad_guesses):
    print('Sorry, you guessed wrong, we have taken a life off you, Try again')
    lives -= 1
    print('You have', lives, 'lives left')
    bad_guesses.append(letter)
    print('These are the wrong guesses you have made:')
    print(sorted(bad_guesses))
    return lives


def repeat_guess(letter, guess_state, bad_guesses):
    print('You have already guessed', letter)
    print('Reminder!')
    print('This is what you currently have guessed correctly: \n', guess_state)
    print('This is what you have guessed incorrectly: \n', bad_guesses)
    print("Don't worry, I have not taken a life from you")


def graphic(lives, answer):
    if lives == 8:
        print("____________")
        print("|           ")
        print("|           ")
        print("|           ")
        print("|           ")
        print("|           ")
        print("\n")
    elif lives == 7:
        print("____________")
        print("|/          ")
        print("|           ")
        print("|           ")
        print("|           ")
        print("|           ")
    elif lives == 6:
        print("____________")
        print("|/      |   ")
        print("|           ")
        print("|           ")
        print("|           ")
        print("|           ")
    elif lives == 5:
        print("____________")
        print("|/      |   ")
        print("|       @   ")
        print("|           ")
        print("|           ")
        print("|           ")
    elif lives == 4:
        print("____________")
        print("|/      |   ")
        print("|       @   ")
        print("|       |   ")
        print("|           ")
        print("|           ")
    elif lives == 3:
        print("____________")
        print("|/      |   ")
        print("|       @   ")
        print("|      /|   ")
        print("|           ")
        print("|           ")
    elif lives == 2:
        print("____________")
        print("|/      |   ")
        print("|       @   ")
        print("|      /|\  ")
        print("|           ")
        print("|           ")
    elif lives == 1:
        print("____________")
        print("|/      |   ")
        print("|       @   ")
        print("|      /|\  ")
        print("|      /    ")
        print("|           ")
    elif lives == 0:
        print("____________")
        print("|/      |   ")
        print("|       @   ")
        print("|      /|\  ")
        print("|      / \  ")
        print("|           ")
        print("GAME OVER")
        print("The word was", answer)


def rules():
    print("You have 8 chances to guess letters in the word I am thinking of.")
    print("You may only guess one letter at a time.")
    print("Incorrect guesses means you loose a life.")
    print("Correct guesses and you don't loose a life.")
    print("After every correct guess, you will be prompted to see if you want to guess the full word.")
    print("The game is over when your lives are exhausted or the word is guessed.")
    print("Good Luck!")


def guess_full_word(answer):
    guess = input("Enter your guess: \n")
    guess = guess.lower()
    if guess == answer:
        print('YOU WON, the word was:', guess)
        attempt = True
    else:
        print("Sorry, try again. \n No lives have been lost")
        attempt = False
    return attempt


def main():
    answer = generate_word()
    answer_list = generate_answer_list(answer)
    lives = 8
    bad_guesses = []
    graphic(lives, answer)
    rules()

    guess_state = initial_guess_state(len(answer_list))

    while lives != 0:
        letter = user_guess()

        if letter in bad_guesses or letter in guess_state:
            repeat_guess(letter, guess_state, bad_guesses)

        elif letter in answer_list:
            guess_state = right_guess(letter, guess_state, answer_list)
            if guess_state == answer:
                print('YOU WON, the word was:', guess_state)
                #   Prompt to guess the full word
            full_guess = input("Would you like to guess the word? (Y)es or (N)o \n")
            full_guess = full_guess.upper()
            if full_guess == "Y":
                attempt = guess_full_word(answer)
                if attempt:
                    return 0

        else:
            lives = wrong_guess(lives, letter, bad_guesses)
            graphic(lives, answer)








main()