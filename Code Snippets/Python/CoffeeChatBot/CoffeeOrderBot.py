# Define your functions
def print_message():
    print(
        "I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.\n"
    )


def get_size():
    res = input(
        "What size drink can I get for you?\n[a] Small\n[b] Medium\n[c] Large\n> "
    )
    if res == "a":
        return "small"
    elif res == "b":
        return "medium"
    elif res == "c":
        return "large"
    else:
        print_message()
        return get_size()


def get_drink_type():
    res = input(
        "What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte\n> "
    )
    if res == "a":
        return "Brewed Coffee"
    elif res == "b":
        return "Mocha"
    elif res == "c":
        return "Latte with " + order_latte()
    else:
        print_message()
        return get_drink_type()


def order_latte():
    res = input(
        "And what kind of milk for your latte?\n[a] 2% Milk\n[b] Non-Fat Milk\n[c] Soy Milk\n> "
    )
    if res == "a":
        return "2% Milk"
    elif res == "b":
        return "Non-Fat Milk"
    elif res == "c":
        return "Soy Milk"
    else:
        print_message()
        return order_latte()


def ask_name():
    res = input("Can I have your name please?\n> ")
    print("Thanks! " + res + ", your order will be ready soon!\n")


def coffee_bot():
    print("Welcome to the cafe!")
    size = get_size()
    drink_type = get_drink_type()
    print("Alright, that's a " + str(size) + " " + str(drink_type))
    ask_name()


coffee_bot()
