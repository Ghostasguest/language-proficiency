import random
import os


words = ["apple", "breeze", "compass", "drum", "emerald", "forest", "galaxy", "horizon", "iceberg", "jigsaw", "kite", "lantern", "melody", "notebook", "ocean", "puzzle", "quasar", "rocket", "sunset", "tango", "umbrella", "velvet", "whisper", "xylophone", "yawn", "zebra", "artist", "balloon", "canyon", "dandelion", "eclipse", "feather", "giraffe", "hammock", "illusion", "jungle", "kaleidoscope", "lighthouse", "moonlight", "nectar", "oasis", "paint", "quill", "river"]
hangman_stages = [
    """
  +---------|
        |   |
    (╥﹏╥)  |
    / | \\   |
   /  |  \\  |
      |     |
     / \\    |
    /   \\   |
            |  
    ========== 
    """,

    """
  +---------|
      O     |
    / | \\   |
   /  |  \\  |
      |     |
     /      |
    /       |
            |  
    ==========
    """,

    """
  +---------|
      O     |
    / | \\   |
   /  |  \\  |
            |
            |
            |
            |  
    ========== 
    """,

    """
  +---------|
      O     |
      | \\   |
         \\  |
            |
            |
            |
            |  
    ========== 
    """,

    """
  +---------|
      O     |
      |     |
            |
            |
            |
            |
            |  
    ========== 
    """,

    """
  +---------|
            |
            |
            |
            |
            |
            |
            |  
    ==========
    """
]
attempts = 5
correct = 0
word = ""
display_word = []

def choose_word():
    global word
    global display_word
    word = random.choice(words)

    display_word = ["_" for _ in word]
choose_word()


def display_hangman():
    os.system("clear")
    print("\n******** Welcome to HANGMAN ********\n")
    print(f"Number of attempts = {attempts}")
    print(hangman_stages[attempts])
    print(display_word)
    print(word)

def check_letter(letter, word):
    for i, char in enumerate(word):
        if char == letter:
            if display_word[i] == letter:
                continue
            else:
                return i
    return -1

def update_hangman():
    global attempts
    attempts -= 1
    display_hangman()

def check_win_status():
    if correct == len(display_word):
        return True

while True:
        if "_" not in display_word:
            print(" You saved him buddy ")
        if attempts <= 0:
            print("\nYou Killed the man! (╥﹏╥)\n")
            print("""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⡤⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣠⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⠁⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠊⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠖⠀⠸⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣵⣇⣠⠂⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠣⡋⠛⠛⠗⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡿⠓⠶⡞⠛⠦⠈⠠⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠫⠹⣏⣙⠛⢅⠀⠀⠀⠐⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣌⢉⡀⠀⠑⡀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢏⠜⠀⣠⡇⡀⠰⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢫⡆⠀⣰⣿⣾⡇⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⢫⠄⢀⣼⣿⣿⣿⣧⣾⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡿⢁⠄⢀⣼⣿⣿⣿⣿⣿⣷⢰⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡿⠡⠄⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣄⡆⠀⠙⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⢳⠖⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣥⣴⠀⠙⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠃⠖⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣠⠀⠘⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡏⠞⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣠⠀⠹⣿⣿⣿⣿
⣿⣿⣿⣿⠡⠆⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡀⠀⢻⣿⣿⣿
⣿⣿⣿⣿⠔⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⢸⣿⣿⣿
⣿⣿⣿⣿⠖⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠚⠀⢸⣿⣿⣿
⣿⣿⣿⣿⣠⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠖⠀⢸⣿⣿⣿
⣿⣿⣿⣿⣧⡄⠀⠸⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠱⠂⠀⣾⣿⣿⣿
⣿⣿⣿⣿⣿⣧⡆⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢛⡴⠛⢀⣾⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣷⣼⡀⡄⠈⠉⠻⠿⠿⠿⠿⢟⣛⡉⠴⠋⢁⣰⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣌⣢⡐⠄⠐⠤⠕⠒⠈⣉⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣾⣿⣿⣯⣿⣿⣽⣿⣟⣷⣾⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿

            """)
            choice = input("Wanna try again?('y' or 'n'): ")
            print()
            if choice == "y":
                attempts = 5
                choose_word()

            else:
                print("Bye then!\n")
                break
        display_hangman()

        letter = input("Enter a letter: ")
        index = check_letter(letter, word)
        if index == -2:
            display_hangman()
        if index == -1:
            update_hangman()

        else:
            display_word[index] = letter
            correct += 1
            display_hangman()
        if check_win_status():
            os.system("clear")
            print("\nYou saved the man! \n")
            print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⢾⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡔⠋⣀⣼⡏⣼⣏⣹⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣶⣿⣿⣿⣡⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡤⢾⣿⣿⣿⣿⣟⠋⣉⣉⠙⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠴⠚⠁⣀⣴⣿⣿⣿⠿⢿⣿⠿⣿⣿⠟⢸⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⠔⠚⠛⣇⣀⣠⣴⣿⠿⠋⠹⣿⣤⣾⣿⡦⣽⠇⠀⡴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣤⣶⣿⠋⠀⢸⣿⣿⣿⣾⡟⠋⠉⠁⠀⠀⠀⢹⣿⣿⠛⠛⠂⢀⣼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣴⡟⢹⣿⠇⠀⣠⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣶⣿⣴⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣾⠋⠠⡿⠋⣠⣾⣿⣿⣿⣿⣡⣤⣤⣄⡤⣊⣭⣿⣿⣿⣮⣍⣿⡿⠛⠉⢀⣸⣧⠤⣄⣀⠀⠀⠀⠀⠀⠀⠀
⢻⣷⡆⠀⠀⣈⠁⠀⠴⠿⠿⠿⠿⣿⢿⣿⣿⣿⡿⠛⠛⠛⢿⣿⣿⣷⠴⣾⣿⣿⣿⣷⣦⡄⠑⢤⡀⠀⠀⠀⠀
⠈⠻⣿⣿⣿⣿⣿⣗⣀⣠⣤⣤⡀⠀⢀⣿⣿⣯⣀⣠⡆⠀⠈⢿⠋⠀⠾⠿⠿⠿⣿⣿⣿⣿⣶⣾⡿⠳⡀⠀⠀
⠀⠀⠈⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣶⣤⣼⠀⢰⠀⠀⠀⠉⢁⡀⠀⠘⣿⡿⣁⠴⢳⣄⠀
⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⡦⢬⡛⠻⠿⣿⣿⣿⡄⢾⣶⣶⣾⣯⣿⡆⠀⠀⡉⠁⠹⣷⣿⢿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣿⣿⣿⣿⡇⢸⣷⣄⣀⣠⣼⣿⠃⣰⣿⣿⣿⣿⣿⣷⡀⢠⣇⠀⢰⣿⣿⣌⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣧⣾⣿⣿⣿⣿⣿⡿⡄⢻⣿⣿⣿⡉⢻⣿⣷⣸⣿⢠⡟⠀⠙⢿⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⡿⢀⣷⢸⣿⣿⣿⣷⣾⣿⣿⣿⣿⡿⠀⣤⠀⠘⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠟⣠⣾⣇⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣾⣿⠀⠀⣇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣏⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⡴⢀⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠏⠙⠒⠒⠛⠿⢿⣿⣿⣿⣿⣟⡛⠛⠿⠿⣿⣿⣿⣿⣿⡿⣡⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣷⣶⣤⣤⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⠟⢿⣿⣿⣿⠟⢻⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣴⣼⣿⣿⣿⠀⣋⣿⠀⠀⠀⠀
            """)
            choice = input("Wanna save a life again?('y' or 'n'): ")
            print()
            if choice == "y":
                attempts = 5
                correct = 0
                choose_word()

            else:
                print("Bye then!\n")
                break