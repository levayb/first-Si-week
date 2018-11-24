# Idea bank application!
# 2018.11.01

import sys


def printed_the_list_from_commandline():
    if sys.argv[1] == "--list":
        print_idea_bank()


def delete_from_list():
    if sys.argv[1] == "--del" and sys.argv[2] > 1:
        num = int(sys.argv[2])
    with open("ideabank.txt", "r") as open_file:
        remove = open_file.readlines()
    del remove[num]
    with open("ideabank.txt", "w") as open_file:
        open_file.write(remove)
    print_idea_bank()


def user_input():
    new_idea = input("What is your new idea: ")
    return new_idea


def save_user_new_idea(new_idea):
    if new_idea != "":
        with open("ideabank.txt", "a+") as open_file:
            open_file.write(new_idea + "\n")
    print("Your new idea has been added to your list." + "\n")


def print_idea_bank():
    with open("ideabank.txt", "r") as open_file:
        your_ideas = open_file.readlines()
    print("Your ideabank:")
    for i in range(0, len(your_ideas)):
        print(str(i+1) + ". " + your_ideas[i].strip())


def main():
    if len(sys.argv) > 2:
        delete_from_list()

    if len(sys.argv) > 1:
        printed_the_list_from_commandline()

    else:
        new_idea = user_input()
        save_user_new_idea(new_idea)
        print_idea_bank()


if __name__ == '__main__':
        main()
