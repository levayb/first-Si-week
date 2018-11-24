# Story
# You have a brilliant mind and you come up with better 
# and better ideas every day. The problem is, you would forget them quickly, 
# so you decide to write an app that helps you keep track of them.

# Description
# Write an application that can save the given text into a local file. 
# After saving the idea, it should show the existing ideas as well. 
# The app should append the new idea into the file, to allow multiple ideas to be saved.

# Ideabank
# 2018.10.31.
# A kiíratásnál még kiír egy üres sort!!!!!


import sys

def user_input_ide():
    with open("data.txt", "r") as f:
        idea_list = f.read()
    if sys.argv[1] == "del":
        if int(sys.argv[2]) <= len(idea_list):
            chosen = int(sys.argv[2])
            chosen -= 1
            return chosen
        else:
            return "" # a list hozzáadva de valami kínja van!
    elif sys.argv[1] == "list":
        print_ideas()
    else:
        return None


def user_input():
    user_idea = input(str("What is your new idea?: "))
    if user_idea != "":
        return user_idea
    else:
        print_ideas()


def write_into_file(user_idea):
    with open("data.txt", 'a')as f:
        f.write("{}\n".format(user_idea))
       

def print_ideas():
    count = 1
    print("\n" + "Your ideabank: ")
    with open("data.txt", "r") as f:
        for line in f:
            print(str(count) + ". " + line.strip())
            count += 1


def del_an_idea(idea_num):
    #idea_num -= 1
    with open("data.txt", "r") as f:
        list_of_ideas = f.readlines()
    del list_of_ideas[idea_num] 
    with open("data.txt", "w") as f:
        f.writelines(list_of_ideas)
    for i in range(len(list_of_ideas)):
        count = list_of_ideas[i]
        i += 1


def main():
    if len(sys.argv) > 1:
        num = user_input_ide()
        del_an_idea(num)
        print_ideas()
    else:
        idea = user_input()
        write_into_file(idea)
        print_ideas()      

    
if __name__ == '__main__':
        main()
