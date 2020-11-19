import time
from random import randrange

# Read word file and keep it in a big array
word_list_file = open("words_alpha.txt", "r")
word_list_content = word_list_file.read()
word_list = word_list_content.splitlines()

# Global variables used to keep user's attempts and mistakes
user_errors = 0
user_attempts = 0


# Main game logic
def start_game():
    try:
        word_num = int(input("Enter how many words to test (default 10): "))
    except ValueError:
        print("Expected a number but got another character.")
        return

    first_timestamp = time.time()

    for i in range(word_num):
        # Use global variable instead of new ones.
        global user_attempts
        global user_errors

        correct = False
        rand_num = randrange(0, len(word_list))
        word = word_list[rand_num]

        while not correct:
            print(user_progress(i, word_num))
            user_attempt = input("(" + word + "): ")
            user_attempts = user_attempts + 1

            if word == user_attempt:
                correct = True
            else:
                user_errors = user_errors + 1

    second_timestamp = time.time()
    total_time = int(second_timestamp - first_timestamp)
    print("\nTotal time: " + str(total_time) + " seconds.")
    print(user_stats())


# Calculates and displays the user's progress
def user_progress(curr_index, total_word_count):
    progress_line = "["

    for _ in range(curr_index):
        progress_line = progress_line + "#"

    for _ in range(total_word_count - curr_index):
        progress_line = progress_line + " "

    progress_line = progress_line + "]"

    return "\nProgress: " + progress_line + " -> " + str(int((curr_index / total_word_count) * 100)) + " %"


# Displays the user's stats -> How many word were mispelled, etc...
def user_stats():
    stats = "You missed {} out of {} attempts. That's a {} % mistake rate.".format(
        str(user_errors), str(user_attempts), str(int(user_errors/user_attempts)))
    return stats


# Main function
if __name__ == '__main__':
    start_game()
