shopping_list = []


def remove_item(idx):
    index = int(idx) - 1
    item = shopping_list.pop(index)
    print "Removed {}".format(item)

def show_help():
    print "\nSeperate each item with a comma."
    print "\nType DONE to quit, SHOW to see the current list,REMOVE to delete a specific item,\
     and HELP to get this message."


def show_list():
    count = 1
    for item in shopping_list:
        print "{}: {}".format(count,item)
        count += 1


print "Give me a list of things you want to shop for."
show_help()

while True:
    new_stuff = raw_input(">>: ")
    if new_stuff == "DONE":
        print "Here's your list:"
        show_list()
        break
    elif new_stuff == "HELP":
        show_help()
        continue
    elif new_stuff == "SHOW":
        show_list()
        continue
    elif new_stuff == "REMOVE":
        show_list()
        idx = raw_input("Which item? Tell me the number:  ")
        remove_item(idx)
    else:
        new_list = new_stuff.split(",")
        index = raw_input("Add this at a certain spot? Press enter for the end of the list,\
        \nor give me a number. Currently {} items in the list.".format(len(shopping_list)))

        if index:
            try:
                spot = int(index) - 1
            except ValueError:
                "Oops, it's look like you entered an invalid number, {}".format(index)
                continue
            else:
                for item in new_list:
                    shopping_list.insert(spot, item.strip())
                    spot += 1
        else:
            for item in new_list:
                shopping_list.append(item.strip())

