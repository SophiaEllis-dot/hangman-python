from random import *

words = ('cat', 'dog', 'shark')

def get_random_word(wordlist):
    return list( 
        wordlist[randint(0, len(wordlist))]
    )   

def create_hidden_word(word):
    hidden_word = []
    for char in word:
        hidden_word.append('-')
    return hidden_word

def update_hidden_word(index, letter):
    global hidden_word
    hidden_word[index] = letter

def check_answer(choice, word):
    for num in range(0, len(word)):
        if choice == current_word[num]:
            update_hidden_word(num, choice)
            return True
    return False

def reset_game():
    global lives
    global current_word
    global hidden_word
    current_word = get_random_word(words)
    hidden_word = create_hidden_word(current_word)
    lives = 5

current_word = get_random_word(words)
hidden_word = create_hidden_word(current_word)
lives = 5
playing = True

while(playing):
    
    if lives > 0:
        print("\nLives: {}".format(lives))
        print("Word: {}\n".format(hidden_word))
        choice = input("please guess a letter\n: " )
        correct_guess = check_answer(choice, current_word)
        if not correct_guess:
            lives -= 1
        if not '-' in hidden_word:
            print('\nGood job')
            choice = input('start new game? y/n\n: ')
            if choice == 'y':
                reset_game()
            else:
                playing = False
    else:
        print('you lost\n')
        choice = input('start new game? y/n\n: ')
        if choice == 'y':
            reset_game()
        else:
            playing = False

