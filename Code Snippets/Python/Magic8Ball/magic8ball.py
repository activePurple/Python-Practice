# Using this for the randint() function
import random

name = ""

question = ""

answer = ""

# Inclusive number generator from 1 to 9
random_number = random.randint(1, 9)

if random_number == 1:
    answer = "Yes - definitely"
elif random_number == 2:
    answer = "It is decidedly so"
elif random_number == 3:
    answer = "Without a doubt"
elif random_number == 4:
    answer = "Reply hazy, try again"
elif random_number == 5:
    answer = "Ask again later"
elif random_number == 6:
    answer = "Better not tell you now"
elif random_number == 7:
    answer = "My sources say no"
elif random_number == 8:
    answer = "Outlook not so good"
elif random_number == 9:
    answer = "Very doubtful"
else:
    print("Error with number generator")

if not question:
    print("What is your question? ")
    question = input()
else:
    question = question

if not name:
    print("Name Please: ")
    name = input()

    print(name + " asks: " + question)
    print("Magic 8 Ball Says: " + answer)
else:
    print(name + " asks: " + question)
    print("Magic 8 Ball Says: " + answer)
