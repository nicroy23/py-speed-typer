import time
from random import randrange

word_list_file = open("words_alpha.txt", "r")
word_list_content = word_list_file.read()
word_list = word_list_content.splitlines()


# Main game logic
def start_game():
    try:
        word_num = int(input("Enter how many words to test (default 10): "))

    except ValueError:
        print("Expected a number but got another character")
        return

    first_timestamp = time.time()

    for i in range(word_num):
        correct = False
        rand_num = randrange(0, len(word_list))
        word = word_list[rand_num]

        while not correct:
            print(user_progress(i, word_num))
            user_attempt = input("(" + word + "): ")

            if word == user_attempt:
                correct = True

    second_timestamp = time.time()
    total_time = int(second_timestamp - first_timestamp)
    print("\nTotal time: " + str(total_time) + " seconds.")


# Calculates and displays the user's progress
def user_progress(curr_index, total_word_count):
    progress_line = "["

    for i in range(curr_index):
        progress_line = progress_line + "#"

    for j in range(total_word_count - curr_index):
        progress_line = progress_line + " "

    progress_line = progress_line + "]"

    return "\nProgress: " + progress_line + " -> " + str((curr_index / total_word_count) * 100) + " %"


# TODO: Display current time total.
# TODO: Calculate stats on user inputs and errors etc.


# Main function
if __name__ == '__main__':
    start_game()
