SNOWMAN_MIN_WORD_LENGTH = 5
SNOWMAN_MAX_WORD_LENGTH = 8
SNOWMAN_MAX_WRONG_GUESSES = 7

SNOWMAN_IMAGE = [
    '*   *   *  ',
    ' *   _ *   ',
    '   _[_]_ * ',
    '  * (")    ',
    '  \( : )/ *',
    '* (_ : _)  ',
    '-----------',
]


def snowman(snowman_word):
    snowman_letters_guessed = build_word_dict(snowman_word)
    wrong_letters = []

    while True:
        print(build_game_board(snowman_word, snowman_letters_guessed))
        user_letter = get_letter_from_user(
            snowman_letters_guessed, wrong_letters)

        if user_letter in snowman_letters_guessed:
            print(f"Correct! {user_letter} is in the word!")
            snowman_letters_guessed[user_letter] = True
        else:
            print(f"Sorry! {user_letter} isn't in the word!")
            add_wrong_letter(wrong_letters, user_letter)

        if is_word_guessed(snowman_letters_guessed):
            # show a winning message along with the full word
            print(f"Congratulations, you win! The word was {snowman_word}")
            return

        print(build_snowman_graphic(len(wrong_letters)))
        print_wrong_letters(wrong_letters)
        print_guesses_remaining(wrong_letters)

        if len(wrong_letters) == SNOWMAN_MAX_WRONG_GUESSES:
            # show a losing message along with the full word
            print(f"Sorry, you lose! The word was {snowman_word}")
            return


def build_snowman_graphic(num_wrong_guesses):
    """This function extracts a portion of the 
    snowman depending on the number of 
    wrong guesses and converts it to a single string
    """

    # get the part of the snowman for the number of wrong guesses
    lines = []
    for line_no in range(num_wrong_guesses):
        lines.append(SNOWMAN_IMAGE[line_no])

    return "\n".join(lines)


# There are no issues in this function
def get_letter_from_user(word_dict, wrong_letters):
    valid_input = False
    user_input_string = None
    while not valid_input:
        user_input_string = input("Guess a letter: ")
        if not user_input_string.isalpha():
            print("You must input a letter!")
        elif len(user_input_string) > 1:
            print("You can only input one letter at a time!")
        elif user_input_string in word_dict and word_dict[user_input_string]:
            print("You already guessed that letter and it's in the word!")
        elif user_input_string in wrong_letters:
            print("You already guessed that letter and it's not in the word!")
        else:
            valid_input = True

    return user_input_string


def build_word_dict(word):
    word_dict = {}
    for letter in word:
        if letter.isalpha():
            # keep track of any character a player might guess (alphabetic)
            word_dict[letter] = False

    return word_dict


def is_word_guessed(word_dict):
    for guessed in word_dict.values():
        # if any letter hasn't been guessed, the word hasn't been guessed
        if not guessed:
            return False

    # all letters were guessed (or we'd have returned) so the word is guessed!
    return True


def build_game_board(word, word_dict):
    output_letters = []
    for elem in word:
        if elem not in word_dict:
            # automatically add any character a player wouldn't be able to guess
            output_letters += elem
        elif word_dict[elem]:
            # add any letters the player has guessed
            output_letters += elem
        else:
            # add a blank for any letter not yet guessed
            output_letters += "_"

    return " ".join(output_letters)


def add_wrong_letter(wrong_letters, letter):
    # track the wrong guesses in alphabetical order
    wrong_letters.append(letter)
    wrong_letters.sort()


# There are no issues in this function
def print_wrong_letters(wrong_letters):
    if not wrong_letters:
        return

    print(f"Wrong letters: {' '.join(wrong_letters)}")


# There are no issues in this function
def print_guesses_remaining(wrong_letters):
    if not wrong_letters:
        return

    print(f"Wrong guesses left: {SNOWMAN_MAX_WRONG_GUESSES - len(wrong_letters)}")
