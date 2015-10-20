from random import randint


def generate_word():

    wordbank = ['rhythm', 'xylophone', 'hospital', 'python', 'instantiation',
                'accessor', 'constructor', 'algorithm', 'overlord', 'ploughing', 'zephyr']

    x = randint(0, len(wordbank)-1)
    return wordbank[x]


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


def initial_lives():
    life_total = 8
    return life_total


def user_guess():
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


def graphic(lives):
    if lives == 8:
        print("So you've fled the Nights Watch, you have become a deserter!")
        print("A crime punishable by death by beheading!")
        print("Lucky for you, my sword is in with the smith. TO THE GALLOWS WITH YOU!")
        print("Whats that you say? You didn't actually take the vow?")
        print("Very well, This is what we shall do")
        print("YE OL' HANGMAN")
        print("8 Lives, 8 chances to see if the gods shine favorably on you this day")
        print("Hurry though, my gallows are getting lonely. \n")
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
        print("Another one bites the dust")
        print("GAME OVER")


def rules():
    print("You have 8 chances to guess letters in the word I am thinking of")
    print("You may not guess the word fully, only the letters inside it.")
    print("Incorrect guesses means you loose a life")
    print("Correct guesses and you don't loose a life")
    print("Good Luck!")


def main():
    answer = generate_word()
    answer_list = generate_answer_list(answer)
    lives = initial_lives()
    bad_guesses = []
    graphic(lives)
    rules()

    guess_state = initial_guess_state(len(answer_list))

    while lives != 0:
        letter = user_guess()
        if letter not in bad_guesses:
            if letter in guess_state:
                repeat_guess(letter, guess_state, bad_guesses)
            elif letter in answer_list:
                guess_state = right_guess(letter, guess_state, answer_list)
                if guess_state == answer:
                    print('YOU WON, the word was:', guess_state)
                    return 0
            else:
                lives = wrong_guess(lives, letter, bad_guesses)
                graphic(lives)

        elif letter in bad_guesses:
            repeat_guess(letter, guess_state, bad_guesses)



main()