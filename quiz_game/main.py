name = input("Welcome to the quiz game, what is your name? ")
want_to_play = input(f"Thank you, {name}, do you want to play? ").lower()

if want_to_play != "yes":
    quit()

print("Great, let's get started! 🙂")
print()
score = 0

question_1 = input("What is the capital of California? ").capitalize()

if question_1 != "Sacramento":
    print(f"Sorry, the correct answer is Sacramento")
    print()
else:
    print("Correct! You must be a west coast native 🐻")
    print()
    score += 1

question_2 = input("What continent is Libya in? ").capitalize()

if question_2 != "Africa":
    print("Sorry, the correct answer is Africa")
    print()
else:
    print("Correct! Have you been to the desert? 🐫")
    print()
    score += 1

question_3 = input("What ocean is the bermuda triangle in? ").capitalize()

if question_3 != "Atlantic":
    print("Sorry, the correct answer is the Atlantic Ocean")
    print()
else:
    print("Correct! Do you believe in conspiracy theories? 😱")
    print()
    score += 1

question_4 = input("What is the largest country in South America? ").capitalize()

if question_4 != "Brazil":
    print("Sorry, the correct answer is Brazil")
    print()
else:
    print("Correct! E aí galera 🇧🇷")
    print()
    score += 1

question_5 = input("What leaf is on the flag of Canada? ").capitalize()

if question_5 != "Maple":
    print("Sorry, the correct answer is Maple")
    print()
else:
    print("Correct! Maple syrup is my favorite. What about you? 🍁")
    print()
    score += 1

print(f"Thank you for playing! Your score is {score}/5")
