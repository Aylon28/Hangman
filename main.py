import random


def print_interface(guessed_word):
    print(''.join(guessed_word))
    print('Input a letter:', end=' ')


def choose_a_word(words):
    random.seed()
    return random.choice(words)


def main():
    words = ['python', 'java', 'swift', 'javascript'] # words to guess from
    print("H A N G M A N\n")

    svar = ''
    score = 0
    all = 0

    while svar != 'exit':
        print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:', end=' ')
        svar = input()
        random_word = choose_a_word(words)
        guessed_word = list('-' * len(random_word))
        tried_letters = set()
        tries = 8
        if svar == 'play':
            all += 1
            while tries > 0:
                print_interface(guessed_word)
                user_letter = input()

                if len(user_letter) != 1:
                    print('Please, input a single letter.\n')
                    continue
                if not user_letter.isalpha() or not user_letter.islower():
                    print('Please, enter a lowercase letter from the English alphabet.\n')
                    continue

                if (user_letter in random_word) and (user_letter not in tried_letters):
                    for i in range(len(random_word)):
                        if random_word[i] == user_letter:
                            guessed_word[i] = user_letter
                elif user_letter in tried_letters:
                    print("You've already guessed this letter.")
                else:
                    print("That letter doesn't appear in the word.")
                    tries -= 1
                print()
                tried_letters.add(user_letter)

                if '-' not in guessed_word:
                    print(f"You guessed the word {''.join(guessed_word)}!")
                    print('You survived!')
                    score += 1
                    break
            else:
                print('You lost!')
        elif svar == 'results':
            print(f'You won: {score} times.')
            print(f'You lost: {all - score} times.')


if __name__ == '__main__':
    main()
