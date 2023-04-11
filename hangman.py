class Hangman:
    def print_hangman(self):
        word_with_blanks = "Word:\n"
        for i in self.word:
            if i in self.guesses:
                word_with_blanks += i
            else:
                word_with_blanks += '_'

        guesses_trimmed = [i for i in self.guesses if i in self.word]

        guesses_print = "\nGuesses:\n"
        for i in range(len(self.guesses)):
            guesses_print += self.guesses[i]
            if i != len(self.guesses)-1:
                guesses_print += ', '

        if set(guesses_trimmed) == set(self.word):
            print("  ____                         ___                 _ \n / ___| __ _ _ __ ___   ___   / _ \__   _____ _ __| |\n| |  _ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__| |\n| |_| | (_| | | | | | |  __/ | |_| |\ V /  __/ |  |_|\n \____|\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|  (_)\n\n__   __           __        ___       _ \n\ \ / /__  _   _  \ \      / (_)_ __ | |\n \ V / _ \| | | |  \ \ /\ / /| | '_ \| |\n  | | (_) | |_| |   \ V  V / | | | | |_|\n  |_|\___/ \__,_|    \_/\_/  |_|_| |_(_)\n")
            print("Word: \n" + self.word)
            self.game_over = True

        elif self.lives == 4:
            print(" ⎹--------\n ⎹       |\n O       |\n-⎹-      |\n ⎹       |\n /\\      |\n       -----\n")
            print(word_with_blanks)
            print(guesses_print)
        elif self.lives == 3:
            print(" ⎹--------\n ⎹       |\n O       |\n-⎹-      |\n ⎹       |\n /       |\n       -----\n")
            print(word_with_blanks)
            print(guesses_print)
        elif self.lives == 2:
            print(" ⎹--------\n ⎹       |\n O       |\n-⎹-      |\n ⎹       |\n         |\n       -----\n")
            print(word_with_blanks)
            print(guesses_print)
        elif self.lives == 1:
            print(" ⎹--------\n ⎹       |\n O       |\n-⎹       |\n ⎹       |\n         |\n       -----\n")
            print(word_with_blanks)
            print(guesses_print)
        elif self.lives == 0:
            print(" ⎹--------\n ⎹       |\n O       |\n ⎹       |\n ⎹       |\n         |\n       -----\n")
            print(word_with_blanks)
            print(guesses_print)
        else:
            print("  ____                         ___                 _ \n / ___| __ _ _ __ ___   ___   / _ \__   _____ _ __| |\n| |  _ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__| |\n| |_| | (_| | | | | | |  __/ | |_| |\ V /  __/ |  |_|\n \____|\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|  (_)\n\n__   __            _                   _\n\ \ / /__  _   _  | |    ___  ___  ___| |\n \ V / _ \| | | | | |   / _ \/ __|/ _ \ |\n  | | (_) | |_| | | |__| (_) \__ \  __/_|\n  |_|\___/ \__,_| |_____\___/|___/\___(_)\n")
            print("Word: \n" + self.word)
            self.game_over = True

    def __init__(self, word):
        if not word.isalpha():
            print("Invalid word")
            self.game_over = True
            return

        self.word = word.upper()
        self.lives = 4
        self.guesses = []
        self.game_over = False

        self.print_hangman()

    def guess(self, letter):
        if (len(letter) != 1) or (not letter.isalpha()):
            self.print_hangman()
            print("\nYour guess was not one letter")
            return
        if letter in self.guesses:
            self.print_hangman()
            print("\nYou already guessed that letter")
            return
        letter = letter.upper()
        self.guesses.append(letter)
        if letter not in self.word:
            self.lives -= 1
        self.print_hangman() 

word = input("What's your word: ")
for i in range(100):
    print('\n\n\n')
hangman = Hangman(word)
while not hangman.game_over:
    guess = input("Your guess: ")
    hangman.guess(guess)
