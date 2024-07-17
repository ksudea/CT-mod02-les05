# Task 1
my_shopping_list = []

def addToList(*args):
    for a in args:
        my_shopping_list.append(a)

# Task 2
def removeFromList(*args):
    for a in args:
        my_shopping_list.remove(a)
    
#Task 3
def printList():
    print("Here is your shopping cart! \n There are {} items.".format(len(my_shopping_list)))
    for item in my_shopping_list:
        print(item + "\n")


go = True
while go:
    print("Welcome back. You can add to, remove from, or print your shopping cart. \n")
    command = input("add, remove, or print?")

    if(command == "add"):
        continue_adding = True
        while continue_adding:
            item = input("Add new item: ")
            addToList(item)
            choose_to_continue = input("Continue adding? [y/n]")
            if choose_to_continue != "y":
                continue_adding = False
                break

    if(command == "remove"):
        continue_removing = True
        while continue_removing:
            item = input("Remove new item: ")
            removeFromList(item)
            choose_to_continue = input("Continue removing? [y/n]")
            if choose_to_continue != "y":
                continue_removing = False
                break

    if(command == "print"):
        printList()

    quit = input("Would you like to quit? [y/n]")

    if quit == "y":
        go = False
    
    