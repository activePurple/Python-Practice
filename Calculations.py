# Calculations.py
# Electrical calculations functions
# Voltage

def get_voltage():
    amps = input("What is your current in Amps?\n> ")
    resistance = input("What is your resistance in Ohms?\n> ")

    return float(amps) * float(resistance)

def get_watts():
    voltage = input("What's the voltage?\n> ")
    resistance = input("What's the resistance?\n> ")

    return float(voltage) * float(resistance)

def get_current():
    voltage = input("What's the voltage?\n> ")
    resistance = input("What's the resistance?\n> ")

    return float(voltage) / float(resistance)

def get_resistance():
    voltage = input("What's the voltage?\n> ")
    amps = input("What's the current in amps?\n> ")

    return float(voltage) / float(amps)


# Menu for operations
def menu_select():
    select = input("Please select what calculation you want to perform:\n[a] Voltage\n[b] Watts\n[c] Amps\n[d] Resistance\n> ")
    if select == "a":
        voltage = get_voltage()
        print("Voltage is Amps multiplied by resistance in Ohms")
        print("Voltage is " + str(voltage) + "V")
    elif select == "b":
        watts = get_watts()
        print("Power is voltage multipled by resistance in Ohms in Watts")
        print("Watts is " + str(watts) + "W")
    elif select == "c":
        current = get_current()
        print("Current is voltage divided by resistance")
        print("Current is " + str(current) + "A")
    elif select == "d":
        resistance = get_resistance()
        print("Resistance is voltage divided by amps")
        print("Resistance is " + str(resistance) + "Ohms")
    else:
        print("There was an error with selection")

print("Hello and welcome to Tyler's Totally Terrific Chatbot or the TTC!")
print("Right now it just does some basic calculations with more functions to come through.\n")
print(menu_select())



