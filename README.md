# Snowbug

## Goal

There are 5 bugs in this implementation of snowman. Practice using your debugging skills to locate, diagnose, and fix the bugs. For each bug note:

1. In which function it was found
1. The line (or lines) causing the problem
1. What about the line was causing the problem
1. What needed to be done to fix the problem
1. How you located the bug
   
## Activity Setup

Follow these directions once, at the beginning of the activity:

1. Navigate to your projects folder named `projects`

   ```bash
   $ cd ~/Developer/projects
   ```

1. If you would like to be able to keep your work in GitHub, click on the "Fork" button on the GitHub to fork the repository to your GitHub account.  

1. "Clone" (download a copy of this project) into your projects folder. This command makes a new folder called `snowbug`, and then puts the activity into this new folder.  If you forked the activity, be sure to clone from your forked copy.

   ```bash
   $ git clone ...
   ```

   Use `ls` to confirm there's a new activity folder

1. Move your location into this activity folder

   ```bash
   $ cd snowbug
   ```

1. Create a virtual environment named `venv` for this activity:

   ```bash
   $ python3 -m venv venv
   ```

1. Activate this environment:

   ```bash
   $ source venv/bin/activate
   ```

   Verify that you're in a python3 virtual environment by running:

   - `$ python --version` should output a Python 3 version
   - `$ pip --version` should output that it is working with Python 3

1. Install dependencies once at the beginning of this project with

   ```bash
   # Must be in activated virtual environment
   $ pip install -r requirements.txt
   ```

Summary of one-time project setup:

- [ ] `cd` into your `projects` folder
- [ ] Clone the activity onto your machine
- [ ] `cd` into the `snowbug` folder
- [ ] Create the virtual environment `venv`
- [ ] Activate the virtual environment `venv`
- [ ] Install the dependencies with `pip`

## Getting Started

1. While in the activity directory, launch VS Code.

   ```bash
   $ code .
   ```

1. Perform test configuration by going to the Testing panel (shaped like a beaker) and clicking Configure Python Tests. Select pytest as the framework and tests as the location of the tests.

1. Run the tests using the VS Code testing tools.

1. Focus on the top test failure. Read through the test failure, and understand why the failure is happening.

1. Make a plan to fix the test failure.

1. Write code to fix the test failure.

1. Re-run the tests.

1. Continue running tests until all bugs have been fixed.

## Activity Completion

Make note of your investigation, especially the 5 questions in the goal, and be prepared to share your findings with your classmates!

## Solutions

### build_word_dict

Error in how the word dictionary was being built. It should filter out any non-alpha letters from its representation, so that only letters the player can actually guess are tracked.

```
def build_word_dict(word):
   word_dict = {}
   for letter in word:
       # keep track of any character a player might guess (alphabetic)
       word_dict[letter] = False


   return word_dict
```

could resemble

```
def build_word_dict(word):
   word_dict = {}
   for letter in word:
       # keep track of any character a player might guess (alphabetic)
       if letter.isalpha():
           word_dict[letter] = False


   return word_dict
```

### build_game_board

Error in how the current guessed letters are displayed to the user. It currently reverses the sense of checking for whether a letter is in the dict at all.

Recall that non-alpha characters won't be added, so if a character is found that is not in the dict at all, we should add that character to the output. If the character is in the dict, we need to check the value for truthiness. True means the letter was guessed, so we should add it to the output. False indicates it has NOT been guessed, so use the underscore placeholder.

```
def build_game_board(word, word_dict):
   output_letters = []
   for elem in word:
       if elem in word_dict:
           # automatically add any character a player wouldn't be able to guess
           output_letters += elem
       elif word_dict[elem]:
           # add any letters the player has guessed
           output_letters += elem
       else:
           # add a blank for any letter not yet guessed
           output_letters += "_"

   return " ".join(output_letters)
```

could resemble

```
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
```

### build_snowman_graphic

This function has an off-by-one in how it is picking the lines from the snowman image.

```
def build_snowman_graphic(num_wrong_guesses):
   """This function extracts a portion of the
   snowman depending on the number of
   wrong guesses and converts it to a single string
   """

   # get the part of the snowman for the number of wrong guesses
   lines = []
   for line_no in range(num_wrong_guesses - 1):
       lines.append(SNOWMAN_IMAGE[line_no])

   return "\n".join(lines)
```

could resemble

```
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
```

### add_wrong_letter

The related unit test wants this result to be sorted (to help users see which letters they've already guessed).

```
def add_wrong_letter(wrong_letters, letter):
   # track the wrong guesses in alphabetical order
   wrong_letters.append(letter)
```

could resemble

```
def add_wrong_letter(wrong_letters, letter):
   # track the wrong guesses in alphabetical order
   wrong_letters.append(letter)
   wrong_letters.sort()
```

### snowman

The error message display logic in snowman has a variable name typo. Instead of the correct snowman_word, it prints snowman, a reference to the function itself, resulting in output like "Sorry, you lose! The word was <function snowman at 0x10687da60>" appearing in the terminal.

```
       if len(wrong_letters) == SNOWMAN_MAX_WRONG_GUESSES:
           # show a losing message along with the full word
           print(f"Sorry, you lose! The word was {snowman}")
           return
```

could resemble

```
       if len(wrong_letters) == SNOWMAN_MAX_WRONG_GUESSES:
           # show a losing message along with the full word
           print(f"Sorry, you lose! The word was {snowman_word}")
           return
```
